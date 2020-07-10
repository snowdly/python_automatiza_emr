import os
import shutil
import glob
import zipfile
import pandas as pd
import rarfile
import datetime

log = pd.DataFrame(columns=('Etiqueta', 'Valor', 'OK_KO', 'Validacion', 'Fecha_Hora'))

rootDir = 'D:/EMR_Auditorias_Python/'
rootDirAuditoria = os.path.join(rootDir, 'Auditorias/')


def audita_basi(rootDir):
    # leemos los zip del directorio
    for archivo in glob.glob(rootDir + "*.*"):
        # declaraco de variables
        f_zip = 'no'
        f_rar = 'no'
        f_pdf = 'no'
        # sacamos nombre de fichero
        nombre = archivo.split("\\")
        nombre = nombre[1]
        # quitamos extenxion a nombre de fichero
        nombresin = nombre.split(".")
        nombresin = nombresin[0]
        print(nombre)
        # discriminamos tipo de fichero
        # se comprueba si estipo .zip
        if (archivo.count('.zip') > 0 or archivo.count('.ZIP')) > 0:
            print("es un zip")
            # leemos e fichero zip
            archivo_zip = zipfile.ZipFile(archivo)

            # recorremos lista de ficheros de zip

            for n in archivo_zip.namelist():
                if (n.count('.zip') > 0 or n.count('.ZIP') > 0 or f.filename.count('.rar') > 0 or f.filename.count(
                        '.RAR') > 0):
                    f_zip = 'ok'
            for n in archivo_zip.namelist():
                if (n.count('.pdf') > 0 or n.count('.PDF') > 0):
                    f_pdf = 'ok'
            # cerramos el fichero zip
            archivo_zip.close()
            # comprobmos estructura
            if (f_zip.count('ok') > 0 and f_pdf.count('ok') > 0):
                print("estructura fichero EMR ok")
                # dejamos fichero en temporal
                shutil.move(archivo, 'D:/EMR_Auditorias_Python/Auditorias/Resultado/Carpeta_de_Trabajo/')


            else:
                print("estructura fichero EMR no ok")
                # dejamos fichero en rechazos
                shutil.move(archivo, 'D:/EMR_Auditorias_Python/Auditorias/Resultado/Reporte_Estado_Auditoria/')
                # fichero log excel de rechazo
                # guardar log
                writer = pd.ExcelWriter(
                    'D:/EMR_Auditorias_Python/Auditorias/Resultado/Reporte_Estado_Auditoria/' + nombresin + '_Estructura_Ficheros_Rechazo.xlsx')
                log.to_excel(writer, 'sheet1')
                writer.save()

        # archivo_zip.extractall('./Auditorias/Resultado/TEMPORAL')

        # se comprueba si es tipo rar
        elif (archivo.count('.RAR') > 0 or archivo.count('.rar')) > 0:
            print("es un rar")
            # descoprimir en temporal

            rarfile.UNRAR_TOOL = 'D:/EMR_Auditorias_Python/Ficheros_Respaldo/UnRAR.exe'
            # archivo='a6.rar'
            rf = rarfile.RarFile(archivo)
            for f in rf.infolist():

                if (f.filename.count('.rar') > 0 or f.filename.count('.RAR') > 0 or f.filename.count(
                        '.zip') > 0 or f.filename.count('.ZIP') > 0):
                    f_rar = 'ok'

                elif (f.filename.count('.pdf') > 0 or f.filename.count('.PDF') > 0):
                    f_pdf = 'ok'

            # comprobmos estructura
            if (f_rar.count('ok') > 0 and f_pdf.count('ok') > 0):
                print("estructura fichero EMR ok")
            # dejamos fichero en temporal
            # shutil.move(archivo, 'D:/EMR_Auditorias_Python/Auditorias/Resultado/Carpeta_de_Trabajo/')

            else:
                print("estructura fichero EMR no ok")
                # dejamos fichero en rechazos
                # shutil.move(archivo, './Auditorias/Resultado/Rechazos')
                # fichero log excel de rechazo
                # guardar log
                writer = pd.ExcelWriter(
                    'D:/EMR_Auditorias_Python/Auditorias/Resultado/Reporte_Estado_Auditoria/' + nombresin + '_Estructura_Ficheros_Rechazo.xlsx')
                log.to_excel(writer, 'sheet1')
                writer.save()

        # RarFile(archivo).extract('.')

        # se compruba si hay introducido otro tipo de fichero
        else:
            print("fichero con extension diferente de .zip o .rar")
            # shutil.move(archivo, './Auditorias/Resultado/Rechazos')
            # fichero log excel de rechazo
            # guardar log
            writer = pd.ExcelWriter(
                'D:/EMR_Auditorias_Python/Auditorias/Resultado/Reporte_Estado_Auditoria/' + nombresin + '_Estructura_Ficheros_Rechazo.xlsx')
            log.to_excel(writer, 'sheet1')
            writer.save()

    # Retorna resultado del proceso
    r = dict()
    r['Etapa_Validacion'] = 'Descomprime correctamente los ficheros'
    r['Resultado'] = 'Finalizado'
    r['Fecha'] = datetime.datetime.now()
    return r


def audita_principal_old(rootDirAuditoria):
    directories = os.listdir(rootDirAuditoria)
    for file in directories:
        if file.endswith("zip"):
            shutil.copyfile(os.path.join(rootDirAuditoria, file),
                            os.path.join(rootDirAuditoria, 'Resultado/Carpeta_de_Trabajo/', file))
            # logging.debug("El fichero a ser analizado es " + file)
            break
    # Retorna resultado del proceso
    r = dict()
    r['Etapa_Validacion'] = 'Proceso de revisión de estructura de ficheros'
    r['Resultado'] = 'Finalizado'
    r['Fecha'] = datetime.datetime.now()
    return r

def audita_principal():
    # Retorna resultado del proceso
    r = dict()
    r['Etapa_Validacion'] = 'Proceso de revisión de estructura de ficheros'
    r['Resultado'] = 'Finalizado'
    r['Fecha'] = datetime.datetime.now()
    return r

# audita_principal(rootDirAuditoria)
