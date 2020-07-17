import os
import logging
import shutil
import re
import datetime
import calendar
import sys
from xml.etree import ElementTree
import itertools

# rootDir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(rootDir)
# rootDirAuditoria = os.path.join(rootDir, 'Auditorias/')

# Configura log
'''
rootLog = os.path.join(rootDir, 'Logs/')
logging.basicConfig(level=logging.DEBUG
                    , filename=os.path.join(rootLog, 'EMR_log.log'), filemode='w',
                    format='%(asctime)s - %(levelname)s - %(message)s')
'''


def genera_rutas_trabajo():
    auditoria_carpeta = 'Auditorias/'
    ficheros_respaldo_carpeta = 'Ficheros_Respaldo/'
    logs_carpeta = 'Logs/'
    # fileDir = os.path.dirname(os.path.abspath(__file__))
    parentDir = os.path.dirname(os.path.abspath('D:/EMR_Auditorias_Python/automatizacion_emr.exe'))
    rutas_base = dict()
    rutas_base['ruta_base'] = parentDir
    rutas_base['ruta_auditoria'] = os.path.join(parentDir, auditoria_carpeta)
    rutas_base['ruta_ficheros_respaldo'] = os.path.join(parentDir, ficheros_respaldo_carpeta)
    rutas_base['ruta_logs'] = os.path.join(parentDir, logs_carpeta)
    print(rutas_base)
    return rutas_base


# Función para obtener el fichero auditable
def obtiene_fichero_auditable(rootDir):
    logging.debug("Directorio actual " + rootDir)
    directories = os.listdir(rootDir)
    for file in directories:
        if file.endswith(".zip") or file.endswith(".rar"):
            logging.debug("El fichero a ser analizado es " + file)
            # return os.path.splitext(file)[0]
            return file
            break


def crear_carpeta_fichero_trabajo_old(rootDir):
    # logging.debug("Directorio actual " + rootDir)
    nameFile = obtiene_fichero_auditable(rootDir)
    if not os.path.exists(os.path.join(rootDir, nameFile)):
        os.makedirs(os.path.join(rootDir, nameFile))


def crear_carpeta_fichero_trabajo(fichero_trabajo):
    # logging.debug("Directorio actual " + fichero_trabajo)
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

    # print(rutas)
    logging.debug("Se ha creado la carpeta: " + os.path.join(rootDir, carpeta_file, 'Carpeta_de_Trabajo'))
    logging.debug("Se ha creado la carpeta: " + os.path.join(rootDir, carpeta_file, 'Reporte_Estado_Auditoria'))
    return rutas


# Funcion que convierte string en fecha
def string_to_date(dato):
    date_time_obj = datetime.datetime.strptime(dato, '%Y-%m-%d')
    print('Date:', date_time_obj.date())


# funcion para agregar meses
def add_months(sourcedate, months):
    month = sourcedate.month - 1 + months
    year = sourcedate.year + month // 12
    month = month % 12 + 1
    day = min(sourcedate.day, calendar.monthrange(year, month)[1])
    # print(datetime.date(year, month, day))
    return datetime.date(year, month, day)


# Funcion que retorna la cantidad de elmentos de una etiqueta
def cantidad_elementos_xml(fichero, etiqueta):
    cantidad_etiquetas = 0
    r = dict()
    tree = ElementTree.parse(fichero)
    root = tree.getroot()
    for each in root.findall(etiqueta):
        cantidad_etiquetas = cantidad_etiquetas + 1
    r['Fichero'] = fichero
    r['Etiqueta'] = etiqueta
    r['Cantidad'] = cantidad_etiquetas
    return r


# Función que retorna el valor de un elemento xml
def valor_elemento_xml(fichero, etiqueta):
    r = dict()
    valor = '0'
    tree = ElementTree.parse(fichero)
    root = tree.getroot()
    for each in root.findall(etiqueta):
        valor = each.text
    r['Fichero'] = fichero
    r['Etiqueta'] = etiqueta
    r['Valor'] = valor
    return r


# Función que valida la diferencia de horas de medición
def horas_medicion_diferencia(fichero, etiqueta):
    datos = []
    datos_enteros = []
    r = dict()
    r['Fichero'] = fichero
    r['Etiqueta'] = etiqueta
    r['OK_KO'] = 'OK'
    r['Comentario'] = ''
    tree = ElementTree.parse(fichero)
    root = tree.getroot()
    for each in root.findall(etiqueta):
        # print(each.text)
        datos.append(each.text)
        horas = each.text.split(':')[0]
        minutos = each.text.split(':')[1]
        # print(horas, minutos)
        datos_enteros.append(int(horas) * 60 + int(minutos))

    for a, b in itertools.combinations(datos_enteros, 2):
        if b - a <= 7:
            r['OK_KO'] = 'KO'
            r['Comentario'] = 'Medición con diferencia de menos de 7 minutos'
            break
    return r


# Validaciones de Medida Fase
def validaciones_medida_fase(fichero, etiqueta):
    valor_umbral = valor_elemento_xml(fichero, './/Informe_Medidas/Informe_Medidas_Fase1/Equipos_Medida_Fase1'
                                               '/Equipo_Medida_Fase1/Umbral_Deteccion_Vm')
    try:
        vu = valor_umbral['Valor']
    except:
        vu = 0.0
    tree = ElementTree.parse(fichero)
    root = tree.getroot()
    grupo_r =[]
    r = dict()
    r['Fichero'] = fichero
    r['Etiqueta'] = etiqueta
    r['Child'] = ''
    r['OK_KO'] = 'OK'
    r['Comentario'] = ''
    medidas = dict()
    grupo_medidas = []
    cantidad = 0

    try:
        c = cantidad_elementos_xml(fichero, etiqueta)
        d = cantidad_elementos_xml(fichero, etiqueta + 'IdPunto/')
        calculo = c['Cantidad'] / d['Cantidad']
    except:
        calculo = 8
    for each in root.findall(etiqueta):
        cantidad = cantidad + 1
        medidas[each.tag] = each.text
        if cantidad == calculo:
            grupo_medidas.append(medidas)

            # Validacion de Nivel_Referencia_Vm
            if round((float(medidas['Nivel_Referencia_Vm']) / 2), 2) != round(float(medidas['Nivel_Decision_Vm']), 2):
                r['Child'] = './/Informe_Medidas/Informe_Medidas_Fase1/Medicion_Fase1/Medida_Fase1/Nivel_Referencia_Vm'
                r['OK_KO'] = 'KO'
                r['Comentario'] = 'Nivel de Decision NO es la mitad del Nivel de Referencia'
                grupo_r.append(r)

            # Validacion de Valor_Calculado_Vm
            if round(float(medidas['Valor_Calculado_Vm']), 2) < round(float(medidas['Valor_Medido_Promediado_Vm']), 2):
                r['Child'] = './/Informe_Medidas/Informe_Medidas_Fase1/Medicion_Fase1/Medida_Fase1/Valor_Medido_Promediado_Vm'
                r['OK_KO'] = 'KO'
                r['Comentario'] = 'El Valor_Calculado_Vm NO puede ser ' \
                                                                            'inferior a Valor_Medido_Promediado_Vm '
                grupo_r.append(r)

            # Validacion Diferencia_Vm
            if round(float(medidas['Diferencia_Vm']), 2) != (
                    round(float(medidas['Nivel_Decision_Vm']), 2) - round(float(medidas['Valor_Calculado_Vm']), 2)):
                r['Child'] = './/Informe_Medidas/Informe_Medidas_Fase1/Medicion_Fase1/Medida_Fase1/Nivel_Decision_Vm'
                r['OK_KO'] = 'KO'
                r['Comentario'] = 'Debe ser el Nivel_Decision_Vm menos el Valor_Calculado_Vm '
                grupo_r.append(r)
            # Validacion Valor_Medio_Promediado_Vm
            try:
                vp = round(float(medidas['Valor_Medido_Promediado_Vm']), 2)
                if vp < float(vu):
                    r['Child'] = './/Informe_Medidas/Informe_Medidas_Fase1/Medicion_Fase1/Medida_Fase1' \
                                 '/Valor_Medido_Promediado_Vm '
                    r['OK_KO'] = 'KO'
                    r['Comentario'] = ' Debe ponerse <U'
                    grupo_r.append(r)
            except:
                vp = 0

            cantidad = 0
            medidas = dict()
    return grupo_medidas


# Retona estructura de error
def estructura_respuesta_error(etapa):
    r = dict()
    r['Etapa_Validacion'] = etapa
    r['Resultado'] = 'Pendiente'
    r['Fecha'] = datetime.datetime.now()
    return r
