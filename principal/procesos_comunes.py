import fitz
import os
import logging
import shutil
import re
import datetime
import calendar
import sys
from xml.etree import ElementTree
import itertools
import pandas as pd
import xlrd
from principal import listas_comunes
import requests
import xml.dom.minidom
import PyPDF2
import pytesseract
from PIL import Image
import io
from pdf2image import convert_from_path

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
    #parentDir = os.getcwd()
    parentDir = os.path.dirname(os.path.abspath('D:/EMR_Auditorias_Python/automatizacion_emr.exe'))
    rutas_base = dict()
    rutas_base['ruta_base'] = parentDir
    rutas_base['ruta_auditoria'] = os.path.join(parentDir, auditoria_carpeta)
    rutas_base['ruta_ficheros_respaldo'] = os.path.join(parentDir, ficheros_respaldo_carpeta)
    rutas_base['ruta_logs'] = os.path.join(parentDir, logs_carpeta)
    print(rutas_base)
    return rutas_base


# obtiene los datos de catastro desde la api
def consulta_api_catastro(RC):
    # creacion de estructura de respuesta
    datos_catastro = dict()
    datos_catastro['nombre_provincia'] = ''
    datos_catastro['nombre_municipio'] = ''
    datos_catastro['tipo_via'] = ''
    datos_catastro['nombre_via'] = ''
    datos_catastro['numero_portal'] = ''
    datos_catastro['OK_KO'] = 'OK'
    datos_catastro['ERROR'] = ''

    # consulta de api
    URL = 'https://ovc.catastro.meh.es/ovcservweb/OVCSWLocalizacionRC/OVCCallejero.asmx/Consulta_DNPRC'
    Provincia = ''
    Municipio = ''
    # RC = '9500111YJ2790B0001HR'
    PARAMS = {'Provincia': Provincia, 'Municipio': Municipio, 'RC': RC}
    try:
        response = requests.get(url=URL, params=PARAMS)
        # print(response.content)
        # guardar fichero temporal
        #parentDir = os.getcwd()
        parentDir = os.path.dirname(os.path.abspath('D:/EMR_Auditorias_Python/automatizacion_emr.exe'))
        fichero_xml = os.path.join(parentDir, 'Consulta_DNPRC.xml')
        with open(fichero_xml, 'wb') as f:
            f.write(response.content)

        # se obtienen los datos del xml
        doc = xml.dom.minidom.parse(fichero_xml)
        for elemento in doc.getElementsByTagName('cudnp'):
            datos_catastro['cantidad_predios'] = elemento.firstChild.data
        for elemento in doc.getElementsByTagName('np'):
            datos_catastro['nombre_provincia'] = elemento.firstChild.data
        for elemento in doc.getElementsByTagName('nm'):
            datos_catastro['nombre_municipio'] = elemento.firstChild.data
        for elemento in doc.getElementsByTagName('tv'):
            datos_catastro['tipo_via'] = elemento.firstChild.data
        for elemento in doc.getElementsByTagName('nv'):
            datos_catastro['nombre_via'] = elemento.firstChild.data
        for elemento in doc.getElementsByTagName('pnp'):
            datos_catastro['numero_portal'] = elemento.firstChild.data
        if int(datos_catastro['cantidad_predios']) > 1:
            datos_catastro['OK_KO'] = 'KO'
            datos_catastro['ERROR'] = 'La referencia catastral retorna mas de un predio, ' \
                                      'debe validar visualmente los datos '
    except Exception as e:
        datos_catastro['nombre_provincia'] = ''
        datos_catastro['nombre_municipio'] = ''
        datos_catastro['tipo_via'] = ''
        datos_catastro['nombre_via'] = ''
        datos_catastro['numero_portal'] = ''
        datos_catastro['OK_KO'] = 'KO'
        datos_catastro['ERROR'] = e

    # borrar fichero temporal
    os.remove(fichero_xml)

    # retorna datos
    return datos_catastro


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


# Función para ubicar cada pdf, retorna una lista
def lista_pdf(rootDir):
    # r=>root, d=>directories, f=>files
    files_in_dir = []
    for r, d, f in os.walk(rootDir):
        for item in f:
            if '.pdf' in item:
                files_in_dir.append(os.path.join(r, item))
    return files_in_dir


# Función para ubicar cada fichero con un extension determinada, retorna una lista
def lista_extension(rootDir, extension):
    # r=>root, d=>directories, f=>files
    files_in_dir = []
    for r, d, f in os.walk(rootDir):
        for item in f:
            if '.' + extension in item:
                files_in_dir.append(os.path.join(r, item))
    return files_in_dir


# Función para ubicar cada fichero con un extension determinada, retorna una lista
def lista_extension_primero(rootDir, extension):
    # r=>root, d=>directories, f=>files
    files_in_dir = []
    for r, d, f in os.walk(rootDir):
        for item in f:
            if '.' + extension in item:
                files_in_dir.append(os.path.join(r, item))
                break
    return files_in_dir


# Funcion para preparar carpetas de trabajo
def prepara_carpetas_trabajo(rootDir):
    fichero_auditable = obtiene_fichero_auditable(rootDir)
    carpeta_file = os.path.splitext(fichero_auditable)[0]
    # borrar directorio en caso de existir
    if os.path.exists(os.path.join(rootDir, carpeta_file)):
        shutil.rmtree(os.path.join(rootDir, carpeta_file), ignore_errors=True)
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
        if b - a < 7:
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
    grupo_r = []
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
                r[
                    'Child'] = './/Informe_Medidas/Informe_Medidas_Fase1/Medicion_Fase1/Medida_Fase1/Valor_Medido_Promediado_Vm'
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


# Validaciones de Medida Fase
def validaciones_real_medida_fase(fichero, etiqueta):
    valor_umbral = valor_elemento_xml(fichero, './/Informe_Medidas/Informe_Medidas_Fase1/Equipos_Medida_Fase1'
                                               '/Equipo_Medida_Fase1/Umbral_Deteccion_Vm')
    try:
        vu = valor_umbral['Valor']
    except:
        vu = 0.0
    tree = ElementTree.parse(fichero)
    root = tree.getroot()
    grupo_r = []
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


# Convierte coordenadas ETRS89 en UTM
def coordenadas_ETRS89(Longitud, Latitud):
    # convertivos coordenadas en grados a coordenadas en decimal
    signo = -1
    # sustituir tanto en ingles como en español
    if Latitud.find('N') > 0:
        Latitud = Latitud.replace('N', '-')

    else:
        Latitud = Latitud.replace('S', '-')

    Latitud = Latitud[:5] + "-" + Latitud[5:]
    Latitud = Latitud.replace(',', '.')

    if Longitud.find('W') > 0:
        Longitud = Longitud.replace('W', '-')

    elif Longitud.find('O') > 0:
        Longitud = Longitud.replace('O', '-')

    elif Longitud.find('E') > 0:
        Longitud = Longitud.replace('E', '-')
        signo = 1

    Longitud = Longitud[:5] + "-" + Longitud[5:]
    Longitud = Longitud.replace(',', '.')

    deg, minutes, seconds = re.split('-', Latitud)
    CoordenadaY = float(deg) + float(minutes) / 60 + float(seconds) / (60 * 60)

    deg, minutes, seconds = re.split('-', Longitud)
    CoordenadaX = (float(deg) + float(minutes) / 60 + float(seconds) / (60 * 60)) * signo

    return (CoordenadaX, CoordenadaY)


# Obtiene datos de INE incluyendo la población
def obtiene_datos_ine(fichero, Cod_Municipio_Ine, Cod_Provincia_INE, ficheros_respaldo):
    r = dict()
    df_sheet = pd.read_excel(os.path.join(ficheros_respaldo, 'cod_provincia.xlsx'), sheet_name='Hoja1')
    cod_provincia = df_sheet['Cod_Provincia_INE'] == int(Cod_Provincia_INE)
    cod_municipio = df_sheet['Cod_Municipio_Ine'] == Cod_Municipio_Ine
    df_encontrado = df_sheet[cod_provincia & cod_municipio]
    r['Cod_Provincia_INE'] = df_encontrado['Cod_Provincia_INE'].to_string(index=False).strip()
    r['Cod_Municipio_Ine'] = df_encontrado['Cod_Municipio_Ine'].to_string(index=False).strip()
    r['Nombre_Municipio_Catastro'] = df_encontrado['Nombre Municipio_Catastro'].to_string(index=False).strip()
    r['Cod_Municipio_Catastro'] = df_encontrado['Cod_Municipio_Catastro'].to_string(index=False).strip()
    r['Cod_Provincia_Catastro'] = df_encontrado['Cod_Provincia_Catastro'].to_string(index=False).strip()
    r['Nombre_Provincia'] = df_encontrado['Nombre Provincia'].to_string(index=False).strip()
    return r


# Obtiene datos de INE incluyendo la población
def obtiene_datos_ine_p(fichero, Cod_Municipio_Ine, Cod_Provincia_INE, Poblacion, ficheros_respaldo):
    r = dict()
    df_sheet = pd.read_excel(os.path.join(ficheros_respaldo, 'cod_provincia.xlsx'), sheet_name='Hoja1')
    cod_provincia = df_sheet['Cod_Provincia_INE'] == int(Cod_Provincia_INE)
    cod_municipio = df_sheet['Cod_Municipio_Ine'] == Cod_Municipio_Ine
    municipio_catastro = df_sheet['Nombre Municipio_Catastro'] == Poblacion
    df_encontrado = df_sheet[cod_provincia & cod_municipio]
    if len(df_encontrado) > 1:
        df_encontrado_p = df_sheet[cod_provincia & cod_municipio & municipio_catastro]
        r['Cod_Provincia_INE'] = df_encontrado_p['Cod_Provincia_INE'].to_string(index=False).strip()
        r['Cod_Municipio_Ine'] = df_encontrado_p['Cod_Municipio_Ine'].to_string(index=False).strip()
        r['Nombre_Municipio_Catastro'] = df_encontrado_p['Nombre Municipio_Catastro'].to_string(index=False).strip()
        r['Cod_Municipio_Catastro'] = df_encontrado_p['Cod_Municipio_Catastro'].to_string(index=False).strip()
        r['Cod_Provincia_Catastro'] = df_encontrado_p['Cod_Provincia_Catastro'].to_string(index=False).strip()
        r['Nombre_Provincia'] = df_encontrado_p['Nombre Provincia'].to_string(index=False).strip()
    else:
        r['Cod_Provincia_INE'] = df_encontrado['Cod_Provincia_INE'].to_string(index=False).strip()
        r['Cod_Municipio_Ine'] = df_encontrado['Cod_Municipio_Ine'].to_string(index=False).strip()
        r['Nombre_Municipio_Catastro'] = df_encontrado['Nombre Municipio_Catastro'].to_string(index=False).strip()
        r['Cod_Municipio_Catastro'] = df_encontrado['Cod_Municipio_Catastro'].to_string(index=False).strip()
        r['Cod_Provincia_Catastro'] = df_encontrado['Cod_Provincia_Catastro'].to_string(index=False).strip()
        r['Nombre_Provincia'] = df_encontrado['Nombre Provincia'].to_string(index=False).strip()
    return r


def obtiene_datos_antenas(fichero, Cod_Municipio_Ine, Cod_Provincia_INE):
    r = dict()
    df_sheet = pd.read_excel('D:/EMR_Auditorias_Python/Ficheros_Respaldo/cod_provincia.xlsx', sheet_name='Hoja1')
    # print(df_sheet_index.where(df_sheet_index['Cod_Provincia_INE']==36))
    cod_provincia = df_sheet['Cod_Provincia_INE'] == int(Cod_Provincia_INE)
    cod_municipio = df_sheet['Cod_Municipio_Ine'] == Cod_Municipio_Ine
    df_encontrado = df_sheet[cod_provincia & cod_municipio]
    print(df_sheet[cod_provincia & cod_municipio])
    r['Fichero'] = fichero
    r['Cod_Provincia_INE'] = df_encontrado['Cod_Provincia_INE'].to_string(index=False).strip()
    r['Cod_Municipio_Ine'] = df_encontrado['Cod_Municipio_Ine'].to_string(index=False).strip()
    r['Nombre Municipio_Catastro'] = df_encontrado['Nombre Municipio_Catastro'].to_string(index=False).strip()
    return r


# Validacion de Medida Fase por etiqueta
def validaciones_real_medida_fase_etiqueta(fichero, etiqueta):
    # fichero='D:/EMR_Auditorias_Python/Auditorias/PO6100/Carpeta_de_Trabajo/23207/GALN6100E_GALR6100E_ER1_M_ARCA_112601_1' \
    #        '.xml '
    dr = dict()
    dr['OK_KO'] = 'OK'
    dr['Error'] = ''

    # etiqueta = './/Informe_Medidas/Informe_Medidas_Fase1/Medicion_Fase1/Medida_Fase1/Nivel_Referencia_Vm'
    r = validaciones_real_medida_fase(fichero,
                                      './/Informe_Medidas/Informe_Medidas_Fase1/Medicion_Fase1/Medida_Fase1/', )
    for i in r:
        # print(i)
        if etiqueta == './/Informe_Medidas/Informe_Medidas_Fase1/Medicion_Fase1/Medida_Fase1/Nivel_Decision_Vm':
            if round((float(i['Nivel_Referencia_Vm']) / 2), 2) != round(float(i['Nivel_Decision_Vm']), 2):
                dr['OK_KO'] = 'KO'
                dr['Error'] = 'Nivel de Decision NO es la mitad del Nivel de Referencia'
        elif etiqueta == './/Informe_Medidas/Informe_Medidas_Fase1/Medicion_Fase1/Medida_Fase1/Valor_Calculado_Vm':
            if round(float(i['Valor_Calculado_Vm']), 2) < round(float(i['Valor_Medido_Promediado_Vm']), 2):
                dr['OK_KO'] = 'KO'
                dr['Error'] = 'El Valor_Calculado_Vm NO puede ser ' \
                              'inferior a Valor_Medido_Promediado_Vm '
        elif etiqueta == './/Informe_Medidas/Informe_Medidas_Fase1/Medicion_Fase1/Medida_Fase1/Diferencia_Vm':
            diferencia = round(round(float(i['Nivel_Decision_Vm']), 2) - round(float(i['Valor_Calculado_Vm']), 2), 2)
            if round(float(i['Diferencia_Vm']), 2) != diferencia:
                dr['OK_KO'] = 'KO'
                dr['Error'] = 'Debe ser el Nivel_Decision_Vm menos el Valor_Calculado_Vm'
        elif etiqueta == './/Informe_Medidas/Informe_Medidas_Fase1/Medicion_Fase1/Medida_Fase1' \
                         '/Valor_Medido_Promediado_Vm':
            valor_umbral = valor_elemento_xml(fichero, './/Informe_Medidas/Informe_Medidas_Fase1/Equipos_Medida_Fase1'
                                                       '/Equipo_Medida_Fase1/Umbral_Deteccion_Vm')
            try:
                vu = valor_umbral['Valor']
            except:
                vu = 0.0
            try:
                vp = round(float(i['Valor_Medido_Promediado_Vm']), 2)
                if vp < float(vu):
                    dr['OK_KO'] = 'KO'
                    dr['Error'] = ' Debe ponerse <U'
            except:
                vp = 0

    return dr


def obtine_letra_expediente_concesional(fichero):
    fichero_nombre, fichero_extension = os.path.splitext(os.path.basename(fichero))
    fichero_nombre_dividido = fichero_nombre.split('_')
    r = dict()
    r['Letra'] = ''
    r['OK_KO'] = 'KO'
    try:
        # print(fichero_nombre_dividido[0][3])
        for letra in listas_comunes.expediente_concesional:
            if letra['LETRA'] == fichero_nombre_dividido[0][3]:
                r['Letra'] = letra['LETRA']
                r['OK_KO'] = 'OK'
    except:
        r['Letra'] = ''
        r['OK_KO'] = 'KO'
    return r


def obtiene_primer_xml(rootDir):
    r = dict()
    r['Fichero'] = ''
    r['OK_KO'] = 'KO'
    fichero = ''
    for fichero_obtenido in lista_xml(rootDir):
        fichero = fichero_obtenido
        break
    if fichero != '':
        r['Fichero'] = fichero
        r['OK_KO'] = 'OK'
    else:
        r['Fichero'] = ''
        r['OK_KO'] = 'KO'
    return r


def obtiene_pdf_tecnico_competente(carpeta_trabajo):
    pdf_tecnico_competente = ""
    r = lista_pdf(carpeta_trabajo)
    if len(r) > 0:
        encontrado = 0
        for documento in r:
            try:
                pdf = open(documento, "rb")
                pdf_reader = PyPDF2.PdfFileReader(pdf, strict=False)
                if pdf_reader.numPages == 1:
                    pdf_tecnico_competente = documento
                pdf.close()
                if encontrado >= 1: break
            except:
                pdf_tecnico_competente = ""
    else:
        pdf_tecnico_competente = ""
    return pdf_tecnico_competente


def compara_tecnico_competente_pdf_texto(carpeta_trabajo):
    responsable_pdf = dict()
    responsable_pdf['Fichero'] = ''
    responsable_pdf['Paginas'] = 0
    responsable_pdf['OK_KO'] = 'OK'
    responsable_pdf['Error'] = ''
    responsable_pdf['Texto'] = ''
    r = lista_pdf(carpeta_trabajo)
    if len(r) > 0:
        encontrado = 0
        for documento in r:
            try:
                pdf = open(documento, "rb")
                pdf_reader = PyPDF2.PdfFileReader(pdf, strict=False)
                if pdf_reader.numPages == 1:
                    responsable_pdf['Paginas'] = pdf_reader.numPages
                    fichero_nombre, fichero_extension = os.path.splitext(os.path.basename(documento))
                    # print("Fichero a ser analizado: " + fichero_nombre + fichero_extension)
                    responsable_pdf['Fichero'] = documento
                    page = pdf_reader.getPage(0)
                    texto = page.extractText().replace('\n', '')
                    if texto == '':
                        responsable_pdf['OK_KO'] = 'KO'
                        responsable_pdf[
                            'Error'] = 'El fichero PDF: ' + fichero_nombre + fichero_extension + ', no se han podido procesar'
                    else:
                        responsable_pdf['Texto'] = texto
                        encontrado = encontrado + 1
                # Closing the object.
                pdf.close()
                if encontrado >= 1: break
            except:
                responsable_pdf['OK_KO'] = 'KO'
                responsable_pdf['Error'] = 'No se han podido procesar los ficheros pdf'
    else:
        responsable_pdf['OK_KO'] = 'KO'
        responsable_pdf['Error'] = 'No se han podido encontrar ningún pdf, que contengan las características de ' \
                                   'una Declaración de Responsable'
    return responsable_pdf


def compara_tecnico_competente_pdf(Dato, texto, documento):
    responsable_pdf = dict()
    responsable_pdf = dict()
    responsable_pdf['Fichero'] = ''
    responsable_pdf['Paginas'] = 0
    responsable_pdf['Dato'] = Dato
    responsable_pdf['OK_KO'] = 'OK'
    responsable_pdf['Error'] = ''
    try:
        fichero_nombre, fichero_extension = os.path.splitext(os.path.basename(documento))
        if texto == '':
            responsable_pdf['OK_KO'] = 'KO'
            responsable_pdf[
                'Error'] = 'El fichero PDF: ' + fichero_nombre + fichero_extension + ', no se han podido procesar'
        else:
            if not re.findall(Dato, texto):
                responsable_pdf['OK_KO'] = 'KO'
                responsable_pdf['Error'] = 'Documento Revisado: ' + responsable_pdf[
                    'Fichero'] + ': No coincide el dato del ' \
                                 'Técnico Competente'
            else:
                responsable_pdf['Error'] = 'Fichero analizado: ' + responsable_pdf['Fichero']

    except:
        responsable_pdf['OK_KO'] = 'KO'
        responsable_pdf['Error'] = 'No se han podido procesar los ficheros pdf'

    return responsable_pdf


def compara_tecnico_competente_pdf_old(carpeta_trabajo, Dato):
    responsable_pdf = dict()
    responsable_pdf['Fichero'] = ''
    responsable_pdf['Paginas'] = 0
    responsable_pdf['Dato'] = Dato
    responsable_pdf['OK_KO'] = 'OK'
    responsable_pdf['Error'] = ''
    r = lista_pdf(carpeta_trabajo)
    if len(r) > 0:
        encontrado = 0
        for documento in r:
            try:
                pdf = open(documento, "rb")
                pdf_reader = PyPDF2.PdfFileReader(pdf, strict=False)
                if pdf_reader.numPages == 1:
                    responsable_pdf['Paginas'] = pdf_reader.numPages
                    fichero_nombre, fichero_extension = os.path.splitext(os.path.basename(documento))
                    # print("Fichero a ser analizado: " + fichero_nombre + fichero_extension)
                    responsable_pdf['Fichero'] = fichero_nombre + fichero_extension
                    page = pdf_reader.getPage(0)
                    texto = page.extractText().replace('\n', '')
                    if texto == '':
                        responsable_pdf['OK_KO'] = 'KO'
                        responsable_pdf[
                            'Error'] = 'El fichero PDF: ' + fichero_nombre + fichero_extension + ', no se han podido procesar'
                    else:
                        if not re.findall(Dato, texto):
                            responsable_pdf['OK_KO'] = 'KO'
                            responsable_pdf['Error'] = 'Documento Revisado: ' + responsable_pdf[
                                'Fichero'] + ': No coincide el dato del ' \
                                             'Técnico Competente'
                        else:
                            encontrado = encontrado + 1
                            responsable_pdf['Error'] = 'Fichero analizado: ' + responsable_pdf['Fichero']
                # Closing the object.
                pdf.close()
                if encontrado >= 1: break
            except:
                responsable_pdf['OK_KO'] = 'KO'
                responsable_pdf['Error'] = 'No se han podido procesar los ficheros pdf'
    else:
        responsable_pdf['OK_KO'] = 'KO'
        responsable_pdf['Error'] = 'No se han podido encontrar ningún pdf, que contengan las características de ' \
                                   'una Declaración de Responsable'
    return responsable_pdf


def estructura_xml_completa(fichero_xml):
    lista_d_xml = []
    try:
        tree = ElementTree.parse(fichero_xml)
        root = tree.getroot()
        for elemento in listas_comunes.etiqueta_xml:
            for child in root.findall(elemento):
                try:
                    if not child.text == '\n':
                        d_xml = dict()
                        d_xml['Etiqueta'] = elemento + child.tag
                        res = next(
                            (sub for sub in listas_comunes.lista_completa if sub['Etiqueta'] == elemento + child.tag),
                            None)
                        d_xml['Regla'] = str(res['Regla'])
                        d_xml['Valor'] = child.text
                        # print(d_xml)
                        lista_d_xml.append(d_xml)
                except Exception as e:
                    print("Error en " + elemento + child.tag)
                    print(e)
    except Exception as er:
        print(
            "No es posible procesar el fichero " + fichero_xml + " , revise si la esctructura y/o nombre son correctos")
    return lista_d_xml


def extrae_imagenes_pdf(fichero, rootDir):
    d = dict()
    d['Fichero'] = ''
    d['DirTemporal'] = ''
    d['Imagenes'] = ''
    d['Error'] = ''
    fichero_nombre, fichero_extension = os.path.splitext(os.path.basename(fichero))
    fichero_pdf = (os.path.splitext(fichero)[0] + '.pdf').replace('/', '\\')
    # fichero_pdf = fichero.replace('/', '\\')
    if os.path.exists(fichero_pdf):
        d['Fichero'] = fichero_pdf
        try:
            print(fichero_pdf)
            pdf_file = fitz.open(fichero_pdf)
            # print(pdf_file.pageCount)
            V = []
            for x in range(pdf_file.pageCount - 2, pdf_file.pageCount):

                # print(x)
                page = pdf_file[x]
                image_list = page.getImageList()
                for image_index, img in enumerate(page.getImageList(), start=1):

                    # get the XREF of the image
                    xref = img[0]
                    # extract the image bytes
                    base_image = pdf_file.extractImage(xref)
                    image_bytes = base_image["image"]
                    # get the image extension
                    image_ext = base_image["ext"]
                    # load it to PIL
                    image = Image.open(io.BytesIO(image_bytes))

                    # Creamos una nueva carpeta si no existe
                    if not os.path.exists(os.path.join(rootDir, 'Temporal_base', fichero_nombre)):
                        os.makedirs(os.path.join(rootDir, 'Temporal_base', fichero_nombre))

                    # save it to local disk
                    ruta_graba = os.path.join(rootDir, 'Temporal_base', fichero_nombre,
                                              'image_' + str(x) + '.' + image_ext)
                    image.save(open(ruta_graba, 'wb'))
                    V.append(ruta_graba)
            V = list(dict.fromkeys(V))
            d['DirTemporal'] = os.path.join(rootDir, 'Temporal_base')
            d['Imagenes'] = V
        except Exception as e:
            d['DirTemporal'] = ''
            d['Imagenes'] = ''
            d['Error'] = 'Error al intentar extraer imágenes del fichero pdf ' + fichero + '  ' + e
    else:
        d['Error'] = 'No existe fichero ' + fichero_pdf

    return d


def extrae_texto_imagen(fichero, rootDir):
    d = dict()
    d['Texto'] = ''
    fichero_nombre, fichero_extension = os.path.splitext(os.path.basename(fichero))
    d['Fichero'] = fichero_nombre + '.pdf'
    d['Error'] = 'OK'
    try:
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
        ruta_imagen = os.path.join(rootDir, 'Temporal_base',
                                   fichero_nombre)  # r'D:/EMR_Auditorias_Python/Auditorias/PO6100/Carpeta_de_Trabajo\\Temporal_base\\GALE6100E_GALR6100E_ER1_M_ARCA_112601_1'
        texto_a_revisar = ''
        for imagen_pdf in lista_extension(ruta_imagen, 'jpeg'):
            texto_a_revisar = texto_a_revisar + '     ' + pytesseract.image_to_string(imagen_pdf)

        texto_a_revisar = texto_a_revisar.upper()
        d['Texto'] = texto_a_revisar
    except Exception as e:
        d['Texto'] = ''
        d['Error'] = 'Error al intentar leer imagen, verifique que se ha instalado en el equipo  el Tesseract-OCR' + e
    return d


# RETORNA EL FICHERO CAP
def busca_cap_pdf(rootDir):
    # r=>root, d=>directories, f=>files
    files_in_dir = []
    for r, d, f in os.walk(rootDir):
        for item in f:
            if '.pdf' in item:
                if item.upper().find('_CAP_') != -1:
                    files_in_dir.append(os.path.join(r, item))
    return files_in_dir


# TRANSFORMA UN PICHERO PDF EN TEXTO POR MEDIO DE OCR
def fichero_cap_a_texto(PDF_file, ficheros_respaldo, carpeta_trabajo, nameFile, nameTemp):
    d = dict()
    fichero_nombre, fichero_extension = os.path.splitext(os.path.basename(PDF_file))
    tempDir = os.path.join(carpeta_trabajo, nameTemp)
    if not os.path.exists(tempDir):
        os.makedirs(tempDir)
    try:
        '''
        Part #1 : Converting PDF to images
        '''
        # Store all the pages of the PDF in a variable
        pages = convert_from_path(PDF_file, poppler_path=os.path.join(ficheros_respaldo, 'poppler-0.68.0/bin'),
                                  strict=False)
        # Counter to store images of each page of PDF to image
        image_counter = 1
        # Iterate through all the pages stored above
        for page in pages:
            filename = "page_" + str(image_counter) + ".jpg"
            # Save the image of the page in system
            page.save(os.path.join(tempDir, nameFile + '_' + filename), 'JPEG')
            # Increment the counter to update filename
            image_counter = image_counter + 1

        ''' 
        Part #2 - Recognizing text from the images using OCR 
        '''
        # Variable to get count of total number of pages
        filelimit = image_counter - 1
        # Creating a text file to write the output
        outfile = os.path.join(tempDir, nameFile + "_text.txt")
        # Open the file in append mode so that
        # All contents of all images are added to the same file
        f = open(outfile, "a")
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
        # https://tesseract-ocr.github.io/tessdoc/4.0-with-LSTM.html#400-alpha-for-windows
        # https://github.com/UB-Mannheim/tesseract/wiki

        # Iterate from 1 to total number of pages
        for i in range(1, filelimit + 1):
            # Set filename to recognize text from
            # Again, these files will be:
            # page_1.jpg
            # page_2.jpg
            # ....
            # page_n.jpg
            filename = "page_" + str(i) + ".jpg"

            # Recognize the text as string in image using pytesserct
            text = str(((pytesseract.image_to_string(Image.open(os.path.join(tempDir, nameFile + '_' + filename))))))

            # The recognized text is stored in variable text
            # Any string processing may be applied on text
            # Here, basic formatting has been done:
            # In many PDFs, at line ending, if a word can't
            # be written fully, a 'hyphen' is added.
            # The rest of the word is written in the next line
            # Eg: This is a sample text this word here GeeksF-
            # orGeeks is half on first line, remaining on next.
            # To remove this, we replace every '-\n' to ''.
            text = text.replace('-\n', '')

            # Finally, write the processed text to the file.
            f.write(text)

        # Close the file after writing all the text.
        f.close()
        d['Fichero_Texto'] = outfile
        d['Error'] = ''

    except Exception as e:
        d['Fichero_Texto'] = ''
        d['Error'] = 'Error al convertir en texto el fichero ' + PDF_file + '   ' + e

    return d


# TRANSFORMA UN FICHERO PDF EN TEXTO POR MEDIO DE OCR
def fichero_pdf_imagen_texto(PDF_file, ficheros_respaldo, carpeta_trabajo, nameTemp):
    d = dict()
    fichero_nombre, fichero_extension = os.path.splitext(os.path.basename(PDF_file))
    tempDir = os.path.join(carpeta_trabajo, nameTemp, fichero_nombre)
    if not os.path.exists(tempDir):
        os.makedirs(tempDir)
    try:
        '''
        Part #1 : Converting PDF to images
        '''
        # Store all the pages of the PDF in a variable
        pages = convert_from_path(PDF_file, poppler_path=os.path.join(ficheros_respaldo, 'poppler-0.68.0/bin'),
                                  strict=False)
        # Counter to store images of each page of PDF to image
        image_counter = 1
        # Iterate through all the pages stored above
        for page in pages:
            filename = "page_" + str(image_counter) + ".jpg"
            # Save the image of the page in system
            page.save(os.path.join(tempDir, fichero_nombre + '_' + filename), 'JPEG')
            # Increment the counter to update filename
            image_counter = image_counter + 1

        ''' 
        Part #2 - Recognizing text from the images using OCR 
        '''
        # Variable to get count of total number of pages
        filelimit = image_counter - 1
        # Creating a text file to write the output
        outfile = os.path.join(tempDir, fichero_nombre + "_text.txt")
        # Open the file in append mode so that
        # All contents of all images are added to the same file
        f = open(outfile, "a")
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
        # https://tesseract-ocr.github.io/tessdoc/4.0-with-LSTM.html#400-alpha-for-windows
        # https://github.com/UB-Mannheim/tesseract/wiki

        # Iterate from 1 to total number of pages
        for i in range(1, filelimit + 1):
            # Set filename to recognize text from
            # Again, these files will be:
            # page_1.jpg
            # page_2.jpg
            # ....
            # page_n.jpg
            filename = "page_" + str(i) + ".jpg"

            # Recognize the text as string in image using pytesserct
            text = str(((pytesseract.image_to_string(
                Image.open(os.path.join(tempDir, fichero_nombre + '_' + filename)))))).upper()

            # The recognized text is stored in variable text
            # Any string processing may be applied on text
            # Here, basic formatting has been done:
            # In many PDFs, at line ending, if a word can't
            # be written fully, a 'hyphen' is added.
            # The rest of the word is written in the next line
            # Eg: This is a sample text this word here GeeksF-
            # orGeeks is half on first line, remaining on next.
            # To remove this, we replace every '-\n' to ''.
            text = text.replace('-\n', '')

            # Finally, write the processed text to the file.
            f.write(text)

        # Close the file after writing all the text.
        f.close()
        d['Fichero_Texto'] = outfile
        d['Error'] = ''

    except Exception as e:
        d['Fichero_Texto'] = ''
        d['Error'] = 'Error al convertir en texto el fichero ' + PDF_file + '   ' + e

    return d


# BUSCA DATOS EN EL TEXTO OBTENIDO POR IA
def busca_datos_pdf_texto(datoreg, filename):
    d = dict()
    lista_encontrados = []
    d['Error'] = ''
    try:
        pattern = re.compile(datoreg, re.IGNORECASE)
        with open(filename, "rt") as myfile:
            for line in myfile:
                if pattern.search(line) != None:
                    # print(line, end='')
                    lista_encontrados.append(line)
    except Exception as e:
        d['ListaEncontrados'] = lista_encontrados
        d['Error'] = 'Error al buscar datos en  ' + filename + '   ' + e
    d['ListaEncontrados'] = lista_encontrados
    return d

def busca_datos_pdf_texto_b(datoreg, filename):
    d = dict()
    lista_encontrados = []
    d['Error'] = ''
    try:
        pattern = re.compile(datoreg, re.IGNORECASE)
        with open(filename, "rt") as myfile:
            for line in myfile:
                if pattern.search(line) != None:
                    # print(line, end='')
                    lista_encontrados.append(line)
    except Exception as e:
        d['ListaEncontrados'] = lista_encontrados
        d['Error'] = 'Error al buscar datos en  ' + filename + '   ' + e
    d['ListaEncontrados'] = lista_encontrados
    return d
