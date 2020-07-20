import xml.etree.ElementTree as ET
from selenium import webdriver
import re
import json
import requests
import os
import sys
sys.path.insert(0, '../')
from principal import procesos_comunes


"""
rootDir = "ANDE6887A_ANDR6887A_ER1_A_ARCA_117274_1.xml"

# OBTIENE FICHERO XML

tree = ET.parse(rootDir)

root = tree.getroot()

#Abrimos XML
for each in root.findall('.//Datos_Emplazamiento'):

    Latitud = each.find('.//Latitud')

    Longitud = each.find('.//Longitud')


for each in root.findall('.//Calle'):

    dato_Nombre_Via = each.find('.//Nombre_Via')


#sacamos los datos en formato texto
calle=dato_Nombre_Via.text
Latitud=Latitud.text
Longitud=Longitud.text
"""

"""
print(Latitud)
print(Longitud)
"""



def obtiene_datos(Longitud,Latitud,ficheros_respaldo):

	#convertivos coordenadas en grados a coordenadas en decimal ETRS89
	CoordenadaX,CoordenadaY=procesos_comunes.coordenadas_ETRS89(Longitud,Latitud)

	#calculamos los puntos de la diagonal
	#factor 0.0005 equivale a 5 segundos, la diagonal sera de 10 segundos en total
	# si se pone 2 segundos de factor no trae datos en el ejemplo
	factor=0.0003
	Punto1X=CoordenadaX-factor#mayorX
	Punto1Y=CoordenadaY-factor#menorY

	Punto2X=CoordenadaX+factor#menorX
	Punto2Y=CoordenadaY+factor#mayorY



	#cambiar  descarga firefox  por scrapy

	#descagamos el json mirar de que sea sin abrir el firefox
	#driver =webdriver.Firefox(executable_path= os.path.join(ficheros_respaldo,'geckodriver.exe'))
	#driver.maximize_window()
	#driver.get('https://geoportal.minetur.gob.es/VCTEL/infoantenasGeoJSON.do?bbox='+str(Punto1X)+'%2C'+str(Punto1Y)+'%2C'+str(Punto2X)+'%2C'+str(Punto2Y)+'&zoom=3')

	#obtenemos los datos con la api
	urls=[]
	response = requests.get('https://geoportal.minetur.gob.es/VCTEL/infoantenasGeoJSON.do?bbox='+str(Punto1X)+'%2C'+str(Punto1Y)+'%2C'+str(Punto2X)+'%2C'+str(Punto2Y)+'&zoom=3')

	pestana = 0
	driver = webdriver.Firefox(executable_path=os.path.join(ficheros_respaldo, 'geckodriver.exe'))
	for feature in response.json()['features']:
		print(feature)
		print(feature['properties']['Detalle'].replace('@@<url-aplicacion>', ''))
		Url_Estacion = feature['properties']['Detalle'].replace('@@<url-aplicacion>', '')

		if pestana == 0:
			# abrir firefox
			#driver.maximize_window()
			driver.get('https://geoportal.minetur.gob.es/VCTEL/' + Url_Estacion)
		else:
			#abre demas links
			# Opens a new tab
			driver.execute_script("window.open()")
			# Switch to the newly opened tab
			driver.switch_to.window(driver.window_handles[pestana])
			# Navigate to new URL in new tab
			driver.get('https://geoportal.minetur.gob.es/VCTEL/' + Url_Estacion)
		pestana = pestana + 1




#al poner las coordenadas separar minutos de segundos con un  espacio
#infoantenas(longitud','latitud','json')

#infoantenas('04W54 53,63','37N51 01,13','{"type":"FeatureCollection","features":[{"type":"Feature","geometry":{"type":"Point","coordinates":[-4.914917,37.850277]},"properties":{"Gis_Latitud":"37.850278","Gis_Longitud":"-4.914917","Gis_ID":"001736","Gis_Etiqueta":"Estación de telefonía móvil","Gis_Estilo":"vcne.estaciones","Gis_Codigo":"VODAFONE ESPAÑA, S.A. - 001736","Tipo":"Estación de telefonía móvil","Código":"VODAFONE ESPAÑA, S.A. - 001736","Dirección":"CL carretera Palma del rio A-431 Km 11,5, s\/n. CÓRDOBA, CÓRDOBA","Detalle":"@@<url-aplicacion>\/detalleEstacion.do?emplazamiento=001736"},"id":"001736"},{"type":"Feature","geometry":{"type":"Point","coordinates":[-4.912792,37.850864]},"properties":{"Gis_Latitud":"37.850864","Gis_Longitud":"-4.912792","Gis_ID":"01736","Gis_Etiqueta":"Estación de telefonía móvil","Gis_Estilo":"vcne.estaciones","Gis_Codigo":"VODAFONE ESPAÑA, S.A. - 01736","Tipo":"Estación de telefonía móvil","Código":"VODAFONE ESPAÑA, S.A. - 01736","Dirección":"CR A-431 CO-PALMA DEL RIO (VILLARRUBIA), 12. CÓRDOBA, CÓRDOBA","Detalle":"@@<url-aplicacion>\/detalleEstacion.do?emplazamiento=01736"},"id":"01736"},{"type":"Feature","geometry":{"type":"Point","coordinates":[-4.9149,37.850323]},"properties":{"Gis_Latitud":"37.850322","Gis_Longitud":"-4.914900","Gis_ID":"1400453","Gis_Etiqueta":"Estación de telefonía móvil","Gis_Estilo":"vcne.estaciones","Gis_Codigo":"TELEFONICA MOVILES ESPAÑA, S.A.U. - 1400453","Tipo":"Estación de telefonía móvil","Código":"TELEFONICA MOVILES ESPAÑA, S.A.U. - 1400453","Dirección":"VP Villarrubia, S\/N. CÓRDOBA, CÓRDOBA","Detalle":"@@<url-aplicacion>\/detalleEstacion.do?emplazamiento=1400453"},"id":"1400453"},{"type":"Feature","geometry":{"type":"Point","coordinates":[-4.9149,37.850323]},"properties":{"Gis_Latitud":"37.850322","Gis_Longitud":"-4.914900","Gis_ID":"1736","Gis_Etiqueta":"Estación de telefonía móvil","Gis_Estilo":"vcne.estaciones","Gis_Codigo":"VODAFONE ESPAÑA, S.A. - 1736","Tipo":"Estación de telefonía móvil","Código":"VODAFONE ESPAÑA, S.A. - 1736","Dirección":"CR PALMA DEL RIO, 12. CÓRDOBA, CÓRDOBA","Detalle":"@@<url-aplicacion>\/detalleEstacion.do?emplazamiento=1736"},"id":"1736"},{"type":"Feature","geometry":{"type":"Point","coordinates":[-4.9149,37.850323]},"properties":{"Gis_Latitud":"37.850322","Gis_Longitud":"-4.914900","Gis_ID":"1B5CO2738","Gis_Etiqueta":"Estación de telefonía móvil","Gis_Estilo":"vcne.estaciones","Gis_Codigo":"XFERA MOVILES, S.A. - 1B5CO2738","Tipo":"Estación de telefonía móvil","Código":"XFERA MOVILES, S.A. - 1B5CO2738","Dirección":"CR PALMA DEL RIO, 12(K). CÓRDOBA, CÓRDOBA","Detalle":"@@<url-aplicacion>\/detalleEstacion.do?emplazamiento=1B5CO2738"},"id":"1B5CO2738"},{"type":"Feature","geometry":{"type":"Point","coordinates":[-4.9235,37.843552]},"properties":{"Gis_Latitud":"37.843553","Gis_Longitud":"-4.923500","Gis_ID":"ANDR6803B","Gis_Etiqueta":"Estación de telefonía móvil","Gis_Estilo":"vcne.estaciones","Gis_Codigo":"ORANGE ESPAGNE, SAU - ANDR6803B","Tipo":"Estación de telefonía móvil","Código":"ORANGE ESPAGNE, SAU - ANDR6803B","Dirección":"CL H PP-V.1 222(M) Suelo PP V1 M222 VPO, S\/N. CÓRDOBA, CÓRDOBA","Detalle":"@@<url-aplicacion>\/detalleEstacion.do?emplazamiento=ANDR6803B"},"id":"ANDR6803B"}]}',)

#obtiene_datos('02E0851,63','41N2229,75','{"type":"Feature","geometry":{"type":"Point","coordinates":[2.144789,41.375168]},"properties":{"Gis_Latitud":"41.375167","Gis_Longitud":"2.144789","Gis_ID":"0801040","Gis_Etiqueta":"Estación de telefonía móvil","Gis_Estilo":"vcne.estaciones","Gis_Codigo":"TELEFONICA MOVILES ESPAÑA, S.A.U. - 0801040","Tipo":"Estación de telefonía móvil","Código":"TELEFONICA MOVILES ESPAÑA, S.A.U. - 0801040","Dirección":"CL Creu Coberta, 83. BARCELONA, BARCELONA","Detalle":"@@<url-aplicacion>\/detalleEstacion.do?emplazamiento=0801040"},"id":"0801040"')
