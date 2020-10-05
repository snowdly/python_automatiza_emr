from xml.etree import ElementTree
import os
from principal import reglas_validacion_new
from principal import procesos_comunes
from principal import listas_comunes
import datetime
import logging
import pandas as pd

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

def principal(rootDir, rootResultados, nameFile, ficheros_respaldo):
    d = dict()

    for fichero in procesos_comunes.lista_xml(rootDir):
        logging.debug("Analizando fichero : " + fichero)
        # CREA EL DIRECTORIO SI NO EXISTE
        if not os.path.exists(os.path.join(rootResultados, nameFile + '_analisis_inidvidual_xml/')):
            os.makedirs(os.path.join(rootResultados, nameFile + '_analisis_inidvidual_xml/'))

        fichero_nombre, fichero_extension = os.path.splitext(os.path.basename(fichero))
        #print(fichero_nombre, fichero_extension)
        analisis = pd.DataFrame(columns=('Etiqueta', 'Valor', 'OK_KO', 'Validacion', 'Fecha_Hora', 'Comparacion'))

        lista = procesos_comunes.estructura_xml_completa(fichero)
        for elemento in lista:
            try:
                dv = reglas_validacion_new.reglas_validacion_individual(elemento['Etiqueta'], elemento['Regla'],
                                                                        elemento['Valor'],
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
        df = pd.read_excel(fichero, na_values=[''], ignore_index=True)
        array_df.append(df)

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