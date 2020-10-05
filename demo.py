import os
import pandas as pd
import datetime
import itertools
from xml.etree import ElementTree
from principal import listas_comunes
from principal import procesos_comunes

fichero_xml = r'D:/EMR_Auditorias_Python/Auditorias/PO6100/Carpeta_de_Trabajo/23207/GALB6100E_GALR6100E_ER1_M_ARCA_112601_1.xml'
rootDir = r'D:/EMR_Auditorias_Python/Auditorias/PO6100/Reporte_Estado_Auditoria/PO6100_analisis_inidvidual_xml/'
rootDira = r'D:/EMR_Auditorias_Python/Auditorias/PO6100/'
etiqueta_xml = ['.//Datos_Certificacion/'
    , './/Datos_Certificacion/Datos_Visado/'
    , './/Datos_Certificacion/Tecnico_Competente/'
    , './/Estacion_Certificada/Datos_Emplazamiento/'
    , './/Estacion_Certificada/Datos_Emplazamiento/Calle/'
    , './/Estacion_Certificada/Datos_Estacion/'
    , './/Estacion_Certificada/Datos_Estacion/Sectores/Sector/'
    , './/Estacion_Certificada/Datos_Estacion/Sectores/Sector/Antena_Directiva/'
    , './/Estacion_Certificada/Datos_Estacion/Sectores/Sector/Volumen_Referencia/'
    , './/Informe_Medidas/Puntos_Medida/Punto_Medida/'
    , './/Informe_Medidas/Puntos_Medida/Punto_Sensible/'
    , './/Informe_Medidas/Informe_Medidas_Fase1/Datos_Medicion/'
    , './/Informe_Medidas/Informe_Medidas_Fase1/Equipos_Medida_Fase1/Equipo_Medida_Fase1/'
    , './/Informe_Medidas/Informe_Medidas_Fase1/Equipos_Medida_Fase1/Equipo_Medida_Fase1/Medidor/'
    , './/Informe_Medidas/Informe_Medidas_Fase1/Equipos_Medida_Fase1/Equipo_Medida_Fase1/Antena/'
    , './/Informe_Medidas/Informe_Medidas_Fase1/Medicion_Fase1/Medida_Fase1/'
    , './/Documentos/Informacion_Adicional/Documento/'
                ]


lista_etiquetas=[]
l = procesos_comunes.lista_extension_primero(rootDir, 'xlsx')
#print(len(l))
if len(l) == 1:
    df = pd.read_excel(l[0])
    for index, row in df.iterrows():
        #print(row['Etiqueta'], row['Valor'], row['OK_KO'])
        lista_etiquetas.append(row['Etiqueta'])

d = dict()
log = pd.DataFrame(columns=('Etiqueta', 'Valor', 'OK_KO', 'Validacion', 'Fecha_Hora', 'Bandera'))
aa=[]
for e in lista_etiquetas:
    datos = []
    for item in procesos_comunes.lista_xml(rootDira):
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
            #log = log.append(d, ignore_index=True)
            aa.append(d)

for ele in aa:
    print(ele)
'''
#Guardamos en un array todos los datos de los excel
array_df=[]
for fichero in procesos_comunes.lista_extension(rootDir, 'xlsx'):
    fichero_nombre, fichero_extension = os.path.splitext(os.path.basename(fichero))
    df = pd.read_excel(fichero, na_values=[''])
    array_df.append(df)


# Recorremos el listado en el orden que queremos
valores=[]
l = procesos_comunes.lista_extension_primero(rootDir, 'xlsx')
print(len(l))
if len(l) == 1:
    df = pd.read_excel(l[0])
    for index, row in df.iterrows():
        #print(row['Etiqueta'], row['Valor'], row['OK_KO'])
        for elemento_df in array_df:
            a = elemento_df.loc[elemento_df['Etiqueta'] == row['Etiqueta']]
            valores.append(a)
print(valores)
'''


# Recorrer cada fichero excel
# for fichero in procesos_comunes.lista_extension_primero(rootDir, 'xlsx'):
#    fichero_nombre, fichero_extension = os.path.splitext(os.path.basename(fichero))
#    print(fichero)
# df = pd.read_excel(fichero)
# a=df.loc[df['Etiqueta'] == './/Datos_Certificacion/Titular_Nombre_Razon_Social']["Valor"]
# print(str(a))
# print(df)
