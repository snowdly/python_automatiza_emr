import os
import zipfile
import rarfile
import logging
import datetime
from principal import valida_xml_individual_base
from principal import procesos_comunes
#from pyunpack import Archive
import patoolib

# DECLARACION DE VARIABLES GLOBALES
#nameZip = ""
#rootDir = "D:/EMR_Auditorias_Python/Auditorias/Resultado/Carpeta_de_Trabajo"
#rarfile.UNRAR_TOOL = 'D:/EMR_Auditorias_Python/Ficheros_Respaldo/UnRAR.exe'

'''
# Configura log
rootLog = 'D:/EMR_Auditorias_Python/Logs/'
logging.basicConfig(level=logging.DEBUG
                    , filename=os.path.join(rootLog, 'EMR_log.log'), filemode='w', format='%(asctime)s - %(levelname)s - %(message)s')
'''

def extrae_datos(rootDir):
    # procesos_comunes.crear_carpeta_fichero_trabajo(rootDir)
    rootCarpetaTrabajo= rootDir
    logging.debug("Directorio actual " + rootDir)
    directories = os.listdir(rootDir)
    rootDir_sub = rootDir
    for file in directories:
        if os.path.isdir(os.path.join(rootDir, file)):
            logging.debug("Carpeta: " + rootDir + file)
            #print("Es una carpeta: " + rootDir + file)
            filename = os.path.basename(file)
            (carpeta, ext) = os.path.splitext(filename)
            rootDir_sub = rootDir_sub + "/" + file
            extrae_datos(rootDir_sub)
        else:
            if file.endswith(".zip"):
                logging.debug("Es un zip: " + rootDir + '/' + file)
                #print("Es un zip: " + rootDir + '/' + file)
                (carpeta_zip, ext_zip) = os.path.splitext(file)
                with zipfile.ZipFile(rootDir + '/' + file, 'r') as zip_ref_zip:
                    zip_ref_zip.extractall(rootCarpetaTrabajo)
            elif file.endswith(".rar"):
                logging.debug("Es un rar: " + rootDir + '/' + file)
                (carpeta_rar, ext_rar) = os.path.splitext(file)
                r = rarfile.RarFile(rootDir + '/' + file)
                r.extractall(rootCarpetaTrabajo)
                r.close()
            elif file.endswith(".7z"):
                logging.debug("Es un 7z: " + rootDir + '/' + file)
                (carpeta_7z, ext_7z) = os.path.splitext(file)
                #Archive(rootDir + '/' + file).extractall(rootCarpetaTrabajo)
                patoolib.extract_archive(rootDir + '/' + file, outdir=rootCarpetaTrabajo)

def extrae_datos_recursivo(rootDir, nivel):
    for i in range(nivel):
        try:
            extrae_datos(rootDir)
        except:
            print("Finalizado por Carpeta")


def descomprime_todos_ficheros(rootDir, ruta_ficheros_respaldo):
    rarfile.UNRAR_TOOL = os.path.join(ruta_ficheros_respaldo, 'UnRAR.exe')
    # Llamada principal
    r = dict()
    directories = os.listdir(rootDir)
    for file in directories:
        extrae_datos_recursivo(rootDir, 7)

    #Retorna resultado del proceso
    r['Etapa_Validacion'] = 'Proceso de descompresión de ficheros'
    r['Resultado'] = 'Finalizado'
    r['Fecha'] = datetime.datetime.now()
    return r

# descomprime_todos_ficheros('D:/EMR_Auditorias_Python/Auditorias/IB0641/Carpeta_de_Trabajo/')