import os
import logging
import shutil
import re
import datetime
import calendar

rootDir = 'D:/EMR_Auditorias_Python/'
rootDirAuditoria = os.path.join(rootDir, 'Auditorias/')

# Configura log
rootLog = 'D:/EMR_Auditorias_Python/Logs/'
logging.basicConfig(level=logging.DEBUG
                    , filename=os.path.join(rootLog, 'EMR_log.log'), filemode='w',
                    format='%(asctime)s - %(levelname)s - %(message)s')


# Función para obtener el fichero auditable
def obtiene_fichero_auditable(rootDir):
    logging.debug("Directorio actual " + rootDir)
    directories = os.listdir(rootDir)
    for file in directories:
        if file.endswith("zip") or file.endswith("rar"):
            logging.debug("El fichero a ser analizado es " + file)
            # return os.path.splitext(file)[0]
            return file
            break


def crear_carpeta_fichero_trabajo_old(rootDir):
    logging.debug("Directorio actual " + rootDir)
    nameFile = obtiene_fichero_auditable(rootDir)
    if not os.path.exists(os.path.join(rootDir, nameFile)):
        os.makedirs(os.path.join(rootDir, nameFile))


def crear_carpeta_fichero_trabajo(fichero_trabajo):
    # logging.debug("Directorio actual " + fichero_trabajo)
    logging.debug("Directorio actual " + fichero_trabajo)
    directories = os.listdir(fichero_trabajo)
    # print(directories)
    # Se captura el primer fichero del directorio
    for file in directories:
        if file.endswith("zip") or file.endswith("rar"):
            logging.debug("Fichero a trabajar: " + file)
            carpeta_file = os.path.splitext(file)[0]
            break
    # Creamos una nueva carpeta si no existe
    if not os.path.exists(os.path.join(fichero_trabajo, carpeta_file)):
        os.makedirs(os.path.join(fichero_trabajo, carpeta_file))
        logging.debug("Se ha creado el directorio: " + os.path.join(fichero_trabajo, carpeta_file))
        # Movemos el fichero dentro de la subcarpeta
        # shutil.move(os.path.join(fichero_trabajo, file), os.path.join(fichero_trabajo, carpeta_file, file))
        # logging.debug("Se ha movido el fichero a: " + os.path.join(fichero_trabajo, carpeta_file, file))


# Función para ubicar cada xml, retorna una lista
def lista_xml(rootDir):
    # r=>root, d=>directories, f=>files
    files_in_dir = []
    for r, d, f in os.walk(rootDir):
        for item in f:
            if '.xml' in item:
                files_in_dir.append(os.path.join(r, item))
    return files_in_dir


# Funcion para preparar carpetas de trabajo
def prepara_carpetas_trabajo(rootDir):
    fichero_auditable = obtiene_fichero_auditable(rootDir)
    carpeta_file = os.path.splitext(fichero_auditable)[0]
    # borrar directorio en caso de existir
    if os.path.exists(os.path.join(rootDir, carpeta_file)):
        shutil.rmtree(os.path.join(rootDir, carpeta_file))
        logging.debug("Se ha borrado la carpeta: " + os.path.join(rootDir, carpeta_file))

    # crea carpeta
    crear_carpeta_fichero_trabajo(rootDir)

    # crea estructura de ficheros de trabajo
    if not os.path.exists(os.path.join(rootDir, carpeta_file, 'Carpeta_de_Trabajo')):
        os.makedirs(os.path.join(rootDir, carpeta_file, 'Carpeta_de_Trabajo'))
    if not os.path.exists(os.path.join(rootDir, carpeta_file, 'Reporte_Estado_Auditoria')):
        os.makedirs(os.path.join(rootDir, carpeta_file, 'Reporte_Estado_Auditoria'))

    # mueve fichero a ser auditado dentro de Carpeta_trabajo
    shutil.move(os.path.join(rootDir, fichero_auditable),
                os.path.join(rootDir, carpeta_file, 'Carpeta_de_Trabajo', fichero_auditable))
    logging.debug(
        "Se ha movido el fichero a: " + os.path.join(rootDir, carpeta_file, 'Carpeta_de_Trabajo', fichero_auditable))

    # Retorna variables de trabajo de rutas
    rutas = dict()
    rutas['ruta_auditoria_carpeta'] = os.path.join(rootDir, carpeta_file)
    rutas['ruta_auditoria_carpeta_trabajo'] = os.path.join(rootDir, carpeta_file, 'Carpeta_de_Trabajo')
    rutas['ruta_auditoria_carpeta_reporte'] = os.path.join(rootDir, carpeta_file, 'Reporte_Estado_Auditoria')

    print(rutas)
    logging.debug("Se ha creado la carpeta: " + os.path.join(rootDir, carpeta_file, 'Carpeta_de_Trabajo'))
    logging.debug("Se ha creado la carpeta: " + os.path.join(rootDir, carpeta_file, 'Reporte_Estado_Auditoria'))
    return rutas


def string_to_date(dato):
    date_time_obj = datetime.datetime.strptime(dato, '%Y-%m-%d')
    print('Date:', date_time_obj.date())


def add_months(sourcedate, months):
    month = sourcedate.month - 1 + months
    year = sourcedate.year + month // 12
    month = month % 12 + 1
    day = min(sourcedate.day, calendar.monthrange(year, month)[1])
    #print(datetime.date(year, month, day))
    return datetime.date(year, month, day)


# crear_carpeta_mover_fichero_trabajo(os.path.join(rootDirAuditoria, 'resultado/Carpeta_de_Trabajo/'))
# prepara_carpetas_trabajo(rootDirAuditoria)
# string_to_date('2020-07-02')
#if add_months(datetime.datetime.strptime('2020-01-16', '%Y-%m-%d').date(), 24) < datetime.date.today():
#    print(str(add_months(datetime.datetime.strptime('2020-01-16', '%Y-%m-%d').date(), 3)) + " es mayor a " + str(datetime.date.today()))
