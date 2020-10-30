from xml.etree import ElementTree
import os
from principal import reglas_validacion_new
from principal import procesos_comunes
from principal import listas_comunes
import datetime
import logging
import pandas as pd
import shutil

#rootDir = 'D:/EMR_Auditorias_Python/Auditorias/LU7385/Carpeta_de_Trabajo/'
#rootResultados = 'D:/EMR_Auditorias_Python/Auditorias/LU7385/Reporte_Estado_Auditoria/'
#nameFile = 'LU7385'


def principal_ant(rootDir, rootResultados, nameFile, ficheros_respaldo):
    d = dict()

    for fichero in procesos_comunes.lista_xml(rootDir):
        logging.debug("Analizando fichero : " + fichero)
        # CREA EL DIRECTORIO SI NO EXISTE
        if not os.path.exists(os.path.join(rootResultados, nameFile + '_analisis_inidvidual_xml/')):
            os.makedirs(os.path.join(rootResultados, nameFile + '_analisis_inidvidual_xml/'))

        fichero_nombre, fichero_extension = os.path.splitext(os.path.basename(fichero))
        #print(fichero_nombre, fichero_extension)
        analisis = pd.DataFrame(columns=('Etiqueta', 'Valor', 'OK_KO', 'Validacion', 'Fecha_Hora', 'Comparacion'))

        for e in listas_comunes.lista_completa:
            tree = ElementTree.parse(fichero)
            root = tree.getroot()
            for each in root.findall(e['Etiqueta']):
                # print(each.text)
                try:
                    dv = reglas_validacion_new.reglas_validacion_individual(e['Etiqueta'], e['Regla'],
                                                                            '' if each is None else each.text,
                                                                            fichero, ficheros_respaldo, rootDir)
                    analisis = analisis.append(dv, ignore_index=True)
                except Exception as err:
                    print('Error en ' + e['Etiqueta'] + '   ' + err)
                    logging.debug('Error en ' + e['Etiqueta'] + '   ' + err)

        writer = pd.ExcelWriter(
            os.path.join(rootResultados, nameFile + '_analisis_inidvidual_xml/', fichero_nombre + "_analisis.xlsx"))
        analisis.to_excel(writer, 'Analisis_XML')
        writer.save()
        logging.debug("Analizando fichero : " + fichero + "   se ha grabado en: " + os.path.join(rootResultados,
                                                                                                 nameFile + '_analisis_inidvidual_xml/',
                                                                                                 fichero_nombre + "_analisis.xlsx"))

    # Retorna resultado del proceso
    r = dict()
    r['Etapa_Validacion'] = 'Proceso de validación de XML individual'
    r['Resultado'] = 'Finalizado'
    r['Fecha'] = datetime.datetime.now()
    return r

def genera_fichero_texto_desde_pdf_cap(rootDir, rootResultados, nameFile, ficheros_respaldo):
    fichero_cap=procesos_comunes.busca_cap_pdf(rootDir)
    if len(fichero_cap)>0:
        r = procesos_comunes.fichero_cap_a_texto(fichero_cap, ficheros_respaldo, rootDir, nameFile)


def principal(rootDir, rootResultados, nameFile, ficheros_respaldo):
    d = dict()
    fichero_texto_cap = ''
    fichero_tecnico = ''

    # GENERA FICHERO DE TEXTO DESDE PDF CAP
    try:
        fichero_cap = procesos_comunes.busca_cap_pdf(rootDir)
        if len(fichero_cap) > 0:
            print("Inicia conversión a texto de fichero: " + fichero_cap[0])
            logging.debug("Inicia conversión a texto de fichero: " + fichero_cap[0])
            fichero_texto_cap = procesos_comunes.fichero_pdf_imagen_texto(fichero_cap[0], ficheros_respaldo, rootDir, 'Conversion_Fichero_CAP')['Fichero_Texto']
            print("Finaliza conversión a texto de fichero: " + fichero_cap[0])
            logging.debug("Finaliza conversión a texto de fichero: " + fichero_cap[0])
        else:
            fichero_texto_cap = ''
        # ----
        #fichero_texto_cap = dict()
        #fichero_texto_cap['Fichero_Texto']= r'D:\EMR_Auditorias_Python\Conversion_Fichero_CAP\s0700_n0001_r00_GAL6100_JUMPING_CAP_V1\s0700_n0001_r00_GAL6100_JUMPING_CAP_V1_text.txt'
        #fichero_texto_cap['Error']=''
    except Exception as e:
        print("Error en conversión de fichero CAP: ")
        logging.debug("Error en conversión de fichero CAP: ")
        #logging.debug('Error en '  + e)

    # Obtiene datos de Tecnico Competente
    try:
        r_datos_pdf = procesos_comunes.compara_tecnico_competente_pdf_texto(rootDir)
    except Exception as e2:
        print("Error en conversión de fichero TECNICO: ")
        logging.debug("Error en conversión de fichero TECNICO: ")
        #logging.debug('Error en ' + e2)

    for fichero in procesos_comunes.lista_xml(rootDir):
        logging.debug("Analizando fichero : " + fichero)
        # CREA EL DIRECTORIO SI NO EXISTE
        if not os.path.exists(os.path.join(rootResultados, nameFile + '_analisis_inidvidual_xml/')):
            os.makedirs(os.path.join(rootResultados, nameFile + '_analisis_inidvidual_xml/'))

        fichero_nombre, fichero_extension = os.path.splitext(os.path.basename(fichero))
        #print(fichero_nombre, fichero_extension)
        analisis = pd.DataFrame(columns=('Etiqueta', 'Valor', 'OK_KO', 'Validacion', 'Fecha_Hora', 'Comparacion'))

        pdf_texto = ""
        try:
            # TRATAMIENTO DE IMÁGENES
            epdf = procesos_comunes.extrae_imagenes_pdf(fichero, rootDir)
            pdf_texto = procesos_comunes.extrae_texto_imagen(fichero, rootDir)['Texto']
        except Exception as e3:
            print("Error en el Tratamiento de imágenes: ")
            logging.debug("Error en el Tratamiento de imágenes: ")
            #logging.debug('Error en ' + e3)


        # GENERA FICHERO DE TEXTO DESDE PDF TECNICO
        print("Inicia conversión a texto de fichero: " + fichero.replace('xml', 'pdf'))
        fichero_tecnico = procesos_comunes.fichero_pdf_imagen_texto(fichero.replace('xml', 'pdf'), ficheros_respaldo, rootDir , 'Conversion_Fichero_Tecnico')['Fichero_Texto']
        print("Finaliza conversión a texto de fichero: " + fichero.replace('xml', 'pdf'))
        # ---
        #fichero_tecnico = dict()
        #fichero_tecnico['Fichero_Texto']=os.path.join(r'D:\EMR_Auditorias_Python','Conversion_Fichero_Tecnico', fichero_nombre, fichero_nombre + '_text.txt')
        #fichero_tecnico['Error']=''



        lista = procesos_comunes.estructura_xml_completa(fichero)
        for elemento in lista:
            try:
                dv = reglas_validacion_new.reglas_validacion_individual(elemento['Etiqueta'], elemento['Regla'],
                                                                        '' if elemento['Valor'] is None else elemento['Valor'],
                                                                        fichero, ficheros_respaldo, rootDir, pdf_texto,
                                                                        fichero_texto_cap, fichero_tecnico, r_datos_pdf)
                # Se agrega comparación desde el listado
                for completa in listas_comunes.lista_completa :
                    if completa['Etiqueta'] == elemento['Etiqueta']:
                        dv['Comparacion']=completa['Comparacion']
                        break
                # -----------------------------------------------

                analisis = analisis.append(dv, ignore_index=True)
            except Exception as err:
                print('Error en ' + elemento['Etiqueta'] + '   ' + err)
                logging.debug('Error en ' + elemento['Etiqueta'] + '   ' + err)

        # ELIMINAR TEMPORALES
        if os.path.exists(epdf['DirTemporal']):
            shutil.rmtree(epdf['DirTemporal'], ignore_errors=True)

        # GRABACION EN EL EXCEL
        writer = pd.ExcelWriter(
            os.path.join(rootResultados, nameFile + '_analisis_inidvidual_xml/', fichero_nombre + "_analisis.xlsx"))
        analisis.to_excel(writer, 'Analisis_XML')
        writer.save()
        logging.debug("Analizando fichero : " + fichero + "   se ha grabado en: " + os.path.join(rootResultados,
                                                                                                 nameFile + '_analisis_inidvidual_xml/',
                                                                                                 fichero_nombre + "_analisis.xlsx"))

    # Retorna resultado del proceso
    r = dict()
    r['Etapa_Validacion'] = 'Proceso de validación de XML individual'
    r['Resultado'] = 'Finalizado'
    r['Fecha'] = datetime.datetime.now()
    return r


def principal_refactor(rootDir, rootResultados, nameFile, ficheros_respaldo):
    d = dict()
    fichero_texto_cap = ''
    fichero_tecnico_competente = ''
    fichero_tecnico = ''

    # 1. FICHERO CAB - TRATAMIENTO
    # -------------------------------------------------------
    try:
        fichero_cap = procesos_comunes.busca_cap_pdf(rootDir)
        if len(fichero_cap) > 0:
            print("Inicia conversión a texto de fichero: " + fichero_cap[0])
            logging.debug("Inicia conversión a texto de fichero: " + fichero_cap[0])
            fichero_texto_cap = procesos_comunes.fichero_pdf_imagen_texto(fichero_cap[0], ficheros_respaldo, rootDir, 'Conversion_Fichero_CAP')['Fichero_Texto']
            print("Finaliza conversión a texto de fichero: " + fichero_cap[0])
            logging.debug("Finaliza conversión a texto de fichero: " + fichero_cap[0])
        else:
            fichero_texto_cap = ''
    except Exception as e:
        print("Error en conversión de fichero CAP: ")
        logging.debug("Error en conversión de fichero CAP: ")
        # logging.debug('Error en '  + e)
    # --------------------------------------------------------

    # 2. FICHERO TÉCNICO COMPETENTE -TRATAMIENTO
    # --------------------------------------------------------
    try:
        r_datos_pdf = procesos_comunes.compara_tecnico_competente_pdf_texto(rootDir)
    except Exception as e2:
        print("Error en conversión de fichero TECNICO: ")
        logging.debug("Error en conversión de fichero TECNICO: ")
        #logging.debug('Error en ' + e2)
    # --------------------------------------------------------

    # 3. TRAMIENTO DE XML Y PDF TECNICO COMPETENTE
    #   RECORRE TODOS LOS FICHEROS XML
    for fichero in procesos_comunes.lista_xml(rootDir):
        logging.debug("Analizando fichero : " + fichero)
        # CREA EL DIRECTORIO SI NO EXISTE
        if not os.path.exists(os.path.join(rootResultados, nameFile + '_analisis_inidvidual_xml/')):
            os.makedirs(os.path.join(rootResultados, nameFile + '_analisis_inidvidual_xml/'))
        fichero_nombre, fichero_extension = os.path.splitext(os.path.basename(fichero))

        # ANALISIS DE CADA PDF
        pdf_texto = ""
        try:
            # TRATAMIENTO DE IMÁGENES
            epdf = procesos_comunes.extrae_imagenes_pdf(fichero, rootDir)
            if epdf['Fichero'] != '':
                pdf_texto = procesos_comunes.extrae_texto_imagen(fichero, rootDir)['Texto']
            else:
                pdf_texto = ''
        except Exception as e3:
            print("Error en el Tratamiento de imágenes: ")
            logging.debug("Error en el Tratamiento de imágenes: ")
            # logging.debug('Error en ' + e3)




        # GENERA FICHERO DE TEXTO DESDE PDF TECNICO
        if os.path.exists(fichero.replace('xml', 'pdf')):
            print("Inicia conversión a texto de fichero: " + fichero.replace('xml', 'pdf'))
            fichero_tecnico = procesos_comunes.fichero_pdf_imagen_texto(fichero.replace('xml', 'pdf'), ficheros_respaldo, rootDir , 'Conversion_Fichero_Tecnico')['Fichero_Texto']
            print("Finaliza conversión a texto de fichero: " + fichero.replace('xml', 'pdf'))
        else:
            fichero_tecnico  = ""
        # --------------------------------------------------------------------------------------

        # print(fichero_nombre, fichero_extension)
        analisis = pd.DataFrame(columns=('Etiqueta', 'Valor', 'OK_KO', 'Validacion', 'Fecha_Hora', 'Comparacion'))

        lista = procesos_comunes.estructura_xml_completa(fichero)
        for elemento in lista:
            try:
                dv = reglas_validacion_new.reglas_validacion_individual(elemento['Etiqueta'], elemento['Regla'],
                                                                        '' if elemento['Valor'] is None else elemento['Valor'],
                                                                        fichero, ficheros_respaldo, rootDir, pdf_texto,
                                                                        fichero_texto_cap, fichero_tecnico, r_datos_pdf)
                # Se agrega comparación desde el listado
                for completa in listas_comunes.lista_completa :
                    if completa['Etiqueta'] == elemento['Etiqueta']:
                        dv['Comparacion']=completa['Comparacion']
                        break
                # -----------------------------------------------

                analisis = analisis.append(dv, ignore_index=True)
            except Exception as err:
                print('Error en ' + elemento['Etiqueta'] + '   ' + err)
                logging.debug('Error en ' + elemento['Etiqueta'] + '   ' + err)

        # ELIMINAR TEMPORALES
        if os.path.exists(epdf['DirTemporal']):
            shutil.rmtree(epdf['DirTemporal'], ignore_errors=True)

        # GRABACION EN EL EXCEL
        writer = pd.ExcelWriter(
            os.path.join(rootResultados, nameFile + '_analisis_inidvidual_xml/', fichero_nombre + "_analisis.xlsx"))
        analisis.to_excel(writer, 'Analisis_XML')
        writer.save()
        logging.debug("Analizando fichero : " + fichero + "   se ha grabado en: " + os.path.join(rootResultados,
                                                                                                 nameFile + '_analisis_inidvidual_xml/',
                                                                                                 fichero_nombre + "_analisis.xlsx"))

    # Retorna resultado del proceso
    r = dict()
    r['Etapa_Validacion'] = 'Proceso de validación de XML individual'
    r['Resultado'] = 'Finalizado'
    r['Fecha'] = datetime.datetime.now()
    return r

def genera_resumen_xml(rootDirResultados, nameFile):
    # Se obtienen la lista de etiquetas
    lista_etiquetas = []
    l = procesos_comunes.lista_extension_primero(rootDirResultados, 'xlsx')
    # print(len(l))
    if len(l) == 1:
        df = pd.read_excel(l[0])
        for index, row in df.iterrows():
            # print(row['Etiqueta'], row['Valor'], row['OK_KO'])
            lista_etiquetas.append(row['Etiqueta'])

    # Guardamos en un array todos los datos de los excel
    array_df = []
    for fichero in procesos_comunes.lista_extension(rootDirResultados, 'xlsx'):
        fichero_nombre, fichero_extension = os.path.splitext(os.path.basename(fichero))
        #df = pd.read_excel(fichero, na_values=[''], ignore_index=True)
        df = pd.read_excel(fichero, na_values=[''])

        array_df.append(df)

    #Solo se realiza si existen 2 o mas excel
    if len(array_df)>=2:

        # Obtenemos cada fila de cada excel
        similares = pd.DataFrame(columns=('Etiqueta', 'Valor', 'OK_KO', 'Validacion', 'Comparacion'))
        d = dict()
        for i in range(len(lista_etiquetas) - 1):
            for elemento_df in array_df:
                d['Etiqueta'] = elemento_df.iloc[i]['Etiqueta']
                d['Valor'] = elemento_df.iloc[i]['Valor']
                d['OK_KO'] = elemento_df.iloc[i]['OK_KO']
                d['Validacion'] = elemento_df.iloc[i]['Validacion']
                d['Comparacion'] = elemento_df.iloc[i]['Comparacion']
                similares = similares.append(d, ignore_index=True)

        unicos = similares.drop_duplicates()
        if unicos['Etiqueta'].count() > 1:
            writer = pd.ExcelWriter(
                os.path.join(rootDirResultados, nameFile + '_analisis_inidvidual_xml/', nameFile + "_CONSOLIDADO_analisis.xlsx"))
            unicos.to_excel(writer, 'CONSOLIDADO_XML')
            writer.save()

    # Retorna resultado del proceso
    r = dict()
    r['Etapa_Validacion'] = 'Proceso de validación de XML individual'
    r['Resultado'] = 'Finalizado'
    r['Fecha'] = datetime.datetime.now()
    return r