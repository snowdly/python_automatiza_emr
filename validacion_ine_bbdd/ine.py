import xml.etree.ElementTree as ET

import csv

from datetime import date

import pandas as pd



'''
# DECLARACION DE VARIABLES

rootDir = "D:\EMR_Auditorias_Python\Auditorias\ANDE6887A_ANDR6887A_ER1_A_ARCA_117274_1.xml"





def codigo_ine(rootDir):


	# DECLARACION DE VARIABLES
	Cod_Municipio = pd.DataFrame()
	Nombre_Municipio=''
	Log = pd.DataFrame(columns=('Etiqueta', 'Valor', 'OK_KO', 'Validacion', 'Fecha_Hora'))
	
	#sacamos nombre de fichero
	nombre= archivo.split("\\")
	for n in nombre:
   		if n.find(".xml") > 0:
   			Nombre_fichero=n


	# OBTIENE FICHERO XML

	tree = ET.parse(rootDir)

	root = tree.getroot()


	for each in root.findall('.//Datos_Emplazamiento'):


	    dato_Cod_INE_Termino_Municipal = each.find('.//Cod_INE_Termino_Municipal')

	    dato_Cod_INE_Provincia = each.find('.//Cod_INE_Provincia')

	    

	for each in root.findall('.//Calle'):

	    dato_Poblacion = each.find('.//Poblacion')


	#IMPORTAMOS CSV INE

	Cod_Municipio = pd.read_csv('Ficheros_Respaldo\Cod_Municipio_Prov.csv', sep=';',encoding ='latin1')


	#FILTRAMOS DATEFRAME CON CODIGOS INE EN BASE A DATOS XML 
	Cod_Municipio = Cod_Municipio[Cod_Municipio['Cod_Municipio_Ine']== dato_Cod_INE_Termino_Municipal.text]

	#SI DATEFRAME VACIO NO EXIXTE CODIGO INE MUNICIPIO
	if Cod_Municipio.empty:
	    #GENERAR CSV RECHAZO COD MUNICIPIO INE

	    Log=['Cod_Municipio', dato_Cod_INE_Termino_Municipal.text, 'KO', '', date.today()] 
	   	#GUARDAR LOG
		writer = pd.ExcelWriter('./Auditorias/Resultado/Reporte_Estado_Auditoria/'+Reporte_Estado_Auditoria+'_RECHAZO.xlsx')
		log.to_excel(writer,'sheet1')
		writer.save()


	Cod_Municipio = Cod_Municipio[Cod_Municipio['Cod_Provincia_INE']== int(dato_Cod_INE_Provincia.text)]

	#SI DATEDRAME VACIO EL CODIGO DE PROVINCIA NO EXISTE EN RELACION CON CODIGO MUNICIPIO

	if Cod_Municipio.empty:
	    #GENERAR CSV RECHAZO COD PROVINCIA MUNICIPIO
		Log=['Cod_provincia', dato_Cod_INE_Provincia.text, 'KO', '', date.today()]
	   	#GUARDAR LOG
		writer = pd.ExcelWriter('./Auditorias/Resultado/Reporte_Estado_Auditoria/'+Reporte_Estado_Auditoria+'_RECHAZO.xlsx')
		log.to_excel(writer,'sheet1')
		writer.save()

	#sacamos municipio y provincia 

	for municipio in Cod_Municipio['Nombre Municipio_Ine']: 
		Nombre_Municipio=municipio

		if (Nombre_Municipio!=dato_Poblacion.text):
			#GENERAR CSV RECHAZO NOMBRE MUNICIPIO
			Log=['Poblacion',Nombre_Municipio+'||'+ dato_Poblacion.text, 'KO', '', date.today()]

		   	#GUARDAR LOG
			writer = pd.ExcelWriter('./Auditorias/Resultado/Reporte_Estado_Auditoria/'+Reporte_Estado_Auditoria+'_RECHAZO.xlsx')
			log.to_excel(writer,'sheet1')
			writer.save()
	return
		


		

'''

   