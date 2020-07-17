import os
from xml.etree import ElementTree
import itertools
import pandas as pd
import datetime
import logging

# Variables Globales
#rootDir = "D:/EMR_Auditorias_Python/Auditorias/Resultado/Carpeta_de_Trabajo/"
#nameFile = 'HX9419'
#rootDirResultados = 'D:/EMR_Auditorias_Python/Auditorias/Resultado/Reporte_Estado_Auditoria/'
'''
# Configura log
rootLog = 'D:/EMR_Auditorias_Python/Logs/'
logging.basicConfig(level=logging.DEBUG
                    , filename=os.path.join(rootLog, 'EMR_log.log'), filemode='w',
                    format='%(asctime)s - %(levelname)s - %(message)s')
'''
lista_etiquetas = [
    './/Datos_Certificacion/Tipo_Certificacion'
    , './/Datos_Certificacion/Tipo_Solicitud'
    , './/Datos_Certificacion/Titular_Nombre_Razon_Social'
    , './/Datos_Certificacion/Expediente_Concesional' # NO
    , './/Datos_Certificacion/Datos_Visado/Numero_Visado'
    , './/Datos_Certificacion/Datos_Visado/Fecha_Visado'
    , './/Datos_Certificacion/Datos_Visado/Numero_Colegiado'
    , './/Datos_Certificacion/Datos_Visado/Colegio_Profesional'
    , './/Datos_Certificacion/Tecnico_Competente/NIF_NIE'
    , './/Datos_Certificacion/Tecnico_Competente/Nombre'
    , './/Datos_Certificacion/Tecnico_Competente/Apellido1'
    , './/Datos_Certificacion/Tecnico_Competente/Apellido2'

    , './/Estacion_Certificada/Datos_Emplazamiento/Codigo_Emplazamiento'
    , './/Estacion_Certificada/Datos_Emplazamiento/Emplazamiento_Compartido'
    , './/Estacion_Certificada/Datos_Emplazamiento/Cod_INE_Termino_Municipal'
    , './/Estacion_Certificada/Datos_Emplazamiento/Cod_INE_Provincia'
    , './/Estacion_Certificada/Datos_Emplazamiento/Latitud'
    , './/Estacion_Certificada/Datos_Emplazamiento/Longitud'
    , './/Estacion_Certificada/Datos_Emplazamiento/Datum'
    , './/Estacion_Certificada/Datos_Emplazamiento/Referencia_Catastral'
    , './/Estacion_Certificada/Datos_Emplazamiento/Cota_Terreno_Sobre_Nivel_Mar'
    , './/Estacion_Certificada/Datos_Emplazamiento/Calle/Poblacion'
    , './/Estacion_Certificada/Datos_Emplazamiento/Calle/Tipo_Via'
    , './/Estacion_Certificada/Datos_Emplazamiento/Calle/Nombre_Via'
    , './/Estacion_Certificada/Datos_Emplazamiento/Calle/Numero_Portal'
    , './/Estacion_Certificada/Datos_Emplazamiento/Calle/Situacion'

    # , './/Estacion_Certificada/Datos_Estacion/Codigo_Estacion'
    # , './/Estacion_Certificada/Datos_Estacion/Tipo_Sistema'  #no
    , './/Estacion_Certificada/Datos_Estacion/Tipo_Estacion'
    , './/Estacion_Certificada/Datos_Estacion/Entorno_Sensible'
    , './/Estacion_Certificada/Datos_Estacion/Num_Sectores_Interiores'
    , './/Estacion_Certificada/Datos_Estacion/Num_Sectores_Exteriores'

    , './/Estacion_Certificada/Datos_Estacion/Sectores/Sector/Tipo_Potencia_Radiada'
    # ,'.//Estacion_Certificada/Datos_Estacion/Sectores/Sector/Potencia_Maxima_Total' #no
    , './/Estacion_Certificada/Datos_Estacion/Sectores/Sector/Unidad_Potencia_Maxima_Total'
    , './/Estacion_Certificada/Datos_Estacion/Sectores/Sector/Localizacion_Antena'
    , './/Estacion_Certificada/Datos_Estacion/Sectores/Sector/Tipo_Antena'
    , './/Estacion_Certificada/Datos_Estacion/Sectores/Sector/Polarizacion'
    , './/Estacion_Certificada/Datos_Estacion/Sectores/Sector/Altura_Antena_Sobre_Terreno'
    #, './/Estacion_Certificada/Datos_Estacion/Sectores/Sector/Inclinacion_Haz_Sobre_Horizontal'

    , './/Estacion_Certificada/Datos_Estacion/Sectores/Sector/Antena_DirectivaForma_Volumen'
    , './/Estacion_Certificada/Datos_Estacion/Sectores/Sector/Antena_DirectivaDistancia_Referencia'
    , './/Estacion_Certificada/Datos_Estacion/Sectores/Sector/Antena_DirectivaCoeficiente_Reflexion'

    # , './/Informe_Medidas/Puntos_Medida/Punto_Medida/IdPunto'
    # , './/Informe_Medidas/Puntos_Medida/Punto_Medida/Distancia'
    # , './/Informe_Medidas/Puntos_Medida/Punto_Medida/Acimut'

    # , './/Informe_Medidas/Puntos_Medida/Punto_Medida/Punto_Sensible/Situacion'
    # , './/Informe_Medidas/Puntos_Medida/Punto_Medida/Punto_Sensible/Tipo_Espacio_Sensible'
    # , './/Informe_Medidas/Puntos_Medida/Punto_Medida/Punto_Sensible/Tipo_Via'
    # , './/Informe_Medidas/Puntos_Medida/Punto_Medida/Punto_Sensible/Nombre_Via'
    # , './/Informe_Medidas/Puntos_Medida/Punto_Medida/Punto_Sensible/Numero_Portal'
    # , './/Informe_Medidas/Puntos_Medida/Punto_Medida/Punto_Sensible/Codigo_Postal'
    # , './/Informe_Medidas/Puntos_Medida/Punto_Medida/Punto_Sensible/Poblacion'
    # , './/Informe_Medidas/Puntos_Medida/Punto_Medida/Punto_Sensible/Cod_INE_Termino_Municipal'
    # , './/Informe_Medidas/Puntos_Medida/Punto_Medida/Punto_Sensible/Cod_INE_Provincia'

    , './/Informe_Medidas/Informe_Medidas_Fase1/Datos_Medicion/Tecnico_Responsable'
    , './/Informe_Medidas/Informe_Medidas_Fase1/Datos_Medicion/Fecha_Medicion'

    , './/Informe_Medidas/Informe_Medidas_Fase1/Equipos_Medida_Fase1/Equipo_Medida_Fase1/IdEquipo'
    , './/Informe_Medidas/Informe_Medidas_Fase1/Equipos_Medida_Fase1/Equipo_Medida_Fase1/Fecha_Ultima_Calibracion'
    , './/Informe_Medidas/Informe_Medidas_Fase1/Equipos_Medida_Fase1/Equipo_Medida_Fase1/Umbral_Deteccion_Vm'
    , './/Informe_Medidas/Informe_Medidas_Fase1/Equipos_Medida_Fase1/Equipo_Medida_Fase1/Longitud_Cable'

    , './/Informe_Medidas/Informe_Medidas_Fase1/Equipos_Medida_Fase1/Equipo_Medida_Fase1/Medidor/Marca_Medidor'
    , './/Informe_Medidas/Informe_Medidas_Fase1/Equipos_Medida_Fase1/Equipo_Medida_Fase1/Medidor/Modelo_Medidor'
    , './/Informe_Medidas/Informe_Medidas_Fase1/Equipos_Medida_Fase1/Equipo_Medida_Fase1/Medidor/Numero_Serie_Medidor'
    , './/Informe_Medidas/Informe_Medidas_Fase1/Equipos_Medida_Fase1/Equipo_Medida_Fase1/Antena/Marca_Antena'
    , './/Informe_Medidas/Informe_Medidas_Fase1/Equipos_Medida_Fase1/Equipo_Medida_Fase1/Antena/Modelo_Antena'
    , './/Informe_Medidas/Informe_Medidas_Fase1/Equipos_Medida_Fase1/Equipo_Medida_Fase1/Antena/Numero_Serie_Antena'

    # , './/Informe_Medidas/Informe_Medidas_Fase1/Medicion_Fase1/Medida_Fase1/IdPunto'
    # , './/Informe_Medidas/Informe_Medidas_Fase1/Medicion_Fase1/Medida_Fase1/IdEquipo'
    # , './/Informe_Medidas/Informe_Medidas_Fase1/Medicion_Fase1/Medida_Fase1/Hora_Inicio_Medicion'
    # , './/Informe_Medidas/Informe_Medidas_Fase1/Medicion_Fase1/Medida_Fase1/Nivel_Referencia_Vm'
    # , './/Informe_Medidas/Informe_Medidas_Fase1/Medicion_Fase1/Medida_Fase1/Nivel_Decision_Vm'
    # , './/Informe_Medidas/Informe_Medidas_Fase1/Medicion_Fase1/Medida_Fase1/Valor_Medido_Promediado_Vm'
    # , './/Informe_Medidas/Informe_Medidas_Fase1/Medicion_Fase1/Medida_Fase1/Valor_Calculado_Vm'
    # , './/Informe_Medidas/Informe_Medidas_Fase1/Medicion_Fase1/Medida_Fase1/Diferencia_Vm'

    , './/Documentos/Informacion_Adicional/Documento/Nombre'
    , './/Documentos/Informacion_Adicional/Documento/Extension'
    , './/Documentos/Informacion_Adicional/Documento/Codificacion'
    , './/Documentos/Informacion_Adicional/Documento/Contenido'

]


# Función para ubicar cada xml, retorna una lista
def lista_xml(rootDir):
    # r=>root, d=>directories, f=>files
    files_in_dir = []
    for r, d, f in os.walk(rootDir):
        for item in f:
            if '.xml' in item:
                files_in_dir.append(os.path.join(r, item))
    return files_in_dir


# Funcion que compara los valores de una etiqueta
def compara_valores(etiqueta, datos):
    d = dict()
    v = ""
    for a, b in itertools.combinations(datos, 2):
        if a != b:
            print(a, b)
            d['Etiqueta'] = etiqueta
            d['Valor'] = v + " " + (a + " | " + b) + " "
            d['OK_KO'] = "KO"
            d['Validacion'] = "Valores distintos en la etiqueta: " + etiqueta
            d['Fecha_Hora'] = datetime.datetime.now()
            d['Bandera'] = 1
        else:
            d['Etiqueta'] = etiqueta
            d['Valor'] = a
            d['OK_KO'] = "OK"
            d['Fecha_Hora'] = datetime.datetime.now()
            d['Bandera'] = 0
    return d


def compara_xml_principal(rootDir, rootDirResultados, nameFile):
    # Proceso principal
    d = dict()
    log = pd.DataFrame(columns=('Etiqueta', 'Valor', 'OK_KO', 'Validacion', 'Fecha_Hora', 'Bandera'))

    for e in lista_etiquetas:
        datos = []
        for item in lista_xml(rootDir):
            # print("file in dir: ", item)
            tree = ElementTree.parse(item)
            root = tree.getroot()
            for each in root.findall(e):
                datos.append(each.text)

        for a, b in itertools.combinations(datos, 2):
            if a != b:
                # print(a, b)
                d['Etiqueta'] = e
                d['Valor'] = a + " | " + b
                d['OK_KO'] = "KO"
                d['Validacion'] = "Valores distintos en la etiqueta: " + e
                d['Fecha_Hora'] = datetime.datetime.now()
                d['Bandera'] = 1
                log = log.append(d, ignore_index=True)

    #print(log)
    logging.debug(log['Etiqueta'].count())
    if log['Etiqueta'].count() > 1:
        writer = pd.ExcelWriter(os.path.join(rootDirResultados, nameFile + '_Compara_XML_Analisis.xlsx'))
        log.to_excel(writer, 'sheet1')
        writer.save()

    # Retorna resultado del proceso
    r = dict()
    r['Etapa_Validacion'] = 'Proceso de comparación entre XML'
    r['Resultado'] = 'Finalizado'
    r['Fecha'] = datetime.datetime.now()
    return r



#compara_xml_principal(rootDir, nameFile, rootDirResultados)

'''
def difference(list1, list2):
    list_dif = [i for i in list1 + list2 if i not in list1 or i not in list2]
    return list_dif


# Initializing list 1 and list 2
x = [10, 15, 20, 25, 30, 35, 40]
y = [25, 40, 35]

print("List first: " + str(x))
print("List second: " + str(y))

# Take difference of list 1 and list 2
z = difference(x, y)

print("Difference of first and second String: " + str(z))

# if lists are equal
if not z:
    print("First and Second list are Equal")
# if lsts are not equal
else:
    print("First and Second list are Not Equal")
'''
