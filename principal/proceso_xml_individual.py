from xml.etree import ElementTree
import csv
import xlsxwriter
import shutil
import zipfile
import os
from principal import reglas_validacion_new
from principal import procesos_comunes
from principal import listas_comunes
import datetime
import logging
import pandas as pd

rootDir = 'D:/EMR_Auditorias_Python/Auditorias/LU7385/Carpeta_de_Trabajo/'
rootResultados = 'D:/EMR_Auditorias_Python/Auditorias/LU7385/Reporte_Estado_Auditoria/'
nameFile = 'LU7385'

# Configura log
rootLog = 'D:/EMR_Auditorias_Python/Logs/'
logging.basicConfig(level=logging.DEBUG
                    , filename=os.path.join(rootLog, 'EMR_log.log'), filemode='w',
                    format='%(asctime)s - %(levelname)s - %(message)s')


def principal(rootDir, rootResultados, nameFile):
    d = dict()

    for fichero in procesos_comunes.lista_xml(rootDir):
        logging.debug("Analizando fichero : " + fichero)
        # CREA EL DIRECTORIO SI NO EXISTE
        if not os.path.exists(os.path.join(rootResultados, nameFile + '_analisis_inidvidual_xml/')):
            os.makedirs(os.path.join(rootResultados, nameFile + '_analisis_inidvidual_xml/'))

        fichero_nombre, fichero_extension = os.path.splitext(os.path.basename(fichero))
        #print(fichero_nombre, fichero_extension)
        analisis = pd.DataFrame(columns=('Etiqueta', 'Valor', 'OK_KO', 'Validacion', 'Fecha_Hora'))

        for e in listas_comunes.lista_completa:
            tree = ElementTree.parse(fichero)
            root = tree.getroot()
            for each in root.findall(e['Etiqueta']):
                # print(each.text)
                dv = reglas_validacion_new.reglas_validacion_individual(e['Etiqueta'], e['Regla'],
                                                                        '' if each is None else each.text,
                                                                        fichero_nombre)
                analisis = analisis.append(dv, ignore_index=True)

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



'''    
   




for e in listas_comunes.lista_completa:
    #print(e['Etiqueta'])
    #print(e['Regla'])
    datos = []
    for item in procesos_comunes.lista_xml(rootDir):
        tree = ElementTree.parse(item)
        root = tree.getroot()
        for each in root.findall(e['Etiqueta']):
            #print(each.text)
            dv = reglas_validacion_new.reglas_validacion_individual(e['Etiqueta'], e['Regla'],  '' if each is None else each.text)

'''
