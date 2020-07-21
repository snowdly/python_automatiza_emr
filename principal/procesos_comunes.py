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


# Obtiene datos de INE
def obtiene_datos_ine(fichero, Cod_Municipio_Ine, Cod_Provincia_INE, ficheros_respaldo):
    r = dict()
    df_sheet = pd.read_excel(os.path.join(ficheros_respaldo, 'cod_provincia.xlsx' ), sheet_name='Hoja1')
    cod_provincia = df_sheet['Cod_Provincia_INE'] == int(Cod_Provincia_INE)
    cod_municipio = df_sheet['Cod_Municipio_Ine'] == Cod_Municipio_Ine
    df_encontrado = df_sheet[cod_provincia & cod_municipio]
    # print(df_sheet[cod_provincia & cod_municipio])
    r['Fichero'] = fichero
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
