import xml.etree.ElementTree as ET
import csv
from datetime import date
import xlsxwriter
import shutil
import zipfile
import os
from principal import reglas_validacion

# DECLARACION DE VARIABLES GLOBALES
nameZip = "BX0309"
rootDir = "D:\EMR_Auditorias_Python\Auditorias\Resultado\Temporal\\"
nameFile = "CATT0309Z_CATR0309Z_ER1_A_ARCA_103945_1"
correctosDir = "D:\EMR_Auditorias_Python\Auditorias\Resultado\Correctos\\"
rechazosDir = "D:\EMR_Auditorias_Python\Auditorias\Resultado\Rechazos\\"
reparosDir = "D:\EMR_Auditorias_Python\Auditorias\Resultado\Reparos\\"
bandera_mover = 1
vOK_KO = "KO"
vValidacion = ""


# DECOMPRIMIR PRIMER ZIP
shutil.copyfile("D:\OCAMPOS\PYTHON_AUTOMATIZACION\BX0309.zip", rootDir + nameZip + ".zip")
filename = os.path.basename("D:\OCAMPOS\PYTHON_AUTOMATIZACION\BX0309.zip")
(carpeta, ext) = os.path.splitext(filename)
with zipfile.ZipFile("D:\OCAMPOS\PYTHON_AUTOMATIZACION\BX0309.zip", 'r') as zip_ref:
    zip_ref.extractall(rootDir + carpeta)


# LISTAR Y DESCOMPRIMIR SEGUNDO ZIP
directories = os.listdir(rootDir + carpeta)
for file in directories:
    if file.endswith("zip"):
        print(file)
        with zipfile.ZipFile(rootDir + carpeta + "\\" + file, 'r') as zip_ref:
            zip_ref.extractall(rootDir + carpeta)


# OBTENER NOMBRE FICHERO XML
directories = os.listdir(rootDir + carpeta)
for file in directories:
    if file.endswith("xml"):
        nameFile = file
        print(nameFile)


# OBTIENE FICHERO XML
tree = ET.parse(rootDir + carpeta + "\\" + nameFile)
root = tree.getroot()

# CREACION DE FICHERO DE VALIDACION CSV
with open(rootDir + nameZip + '.csv', 'w', newline='') as csvfile:
    validacsv = csv.writer(csvfile, delimiter=';',
                           quotechar='|', quoting=csv.QUOTE_MINIMAL)
    validacsv = csv.writer(csvfile, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    validacsv.writerow(['Etiqueta', 'Valor', 'OK_KO', 'Validacion', 'Fecha_Hora'])

    # VALIDACIÓN Y ESCRITURA PARA CADA ETIQUETA DEL XML
    for each in root.findall('.//Datos_Certificacion'):
        dato_Tipo_Certificacion = each.find('.//Tipo_Certificacion')
        print('' if dato_Tipo_Certificacion is None else dato_Tipo_Certificacion.text)
        validacsv.writerow(['Datos_Certificacion', dato_Tipo_Certificacion.text, reglas_validacion.R_Tipo_Certificacion(dato_Tipo_Certificacion.text).get("OK_KO"), reglas_validacion.R_Tipo_Certificacion(dato_Tipo_Certificacion.text).get("Validacion"), date.today()])

        dato_Tipo_Solicitud = each.find('.//Tipo_Solicitud')
        print('' if dato_Tipo_Solicitud is None else dato_Tipo_Solicitud.text)
        validacsv.writerow(['Tipo_Solicitud', dato_Tipo_Solicitud.text, reglas_validacion.R_Tipo_Solicitud(dato_Tipo_Solicitud.text).get("OK_KO"), reglas_validacion.R_Tipo_Solicitud(dato_Tipo_Solicitud.text).get("Validacion"), date.today()])

        dato_Titular_Nombre_Razon_Social = each.find('.//Titular_Nombre_Razon_Social')
        print('' if dato_Titular_Nombre_Razon_Social is None else dato_Titular_Nombre_Razon_Social.text)
        validacsv.writerow(['Titular_Nombre_Razon_Social', dato_Titular_Nombre_Razon_Social.text, reglas_validacion.R_Titular_Nombre_Razon_Social(dato_Titular_Nombre_Razon_Social.text).get("OK_KO"), reglas_validacion.R_Titular_Nombre_Razon_Social(dato_Titular_Nombre_Razon_Social.text).get("Validacion"), date.today()])

        dato_Expediente_Concesional = each.find('.//Expediente_Concesional')
        print('' if dato_Expediente_Concesional is None else dato_Expediente_Concesional.text)
        validacsv.writerow(['Expediente_Concesional', dato_Expediente_Concesional.text, reglas_validacion.debe_estar_lleno(dato_Expediente_Concesional.text).get("OK_KO"), reglas_validacion.debe_estar_lleno(dato_Expediente_Concesional.text).get("Validacion"), date.today()])

    for each in root.findall('.//Datos_Visado'):
        dato_Numero_Visado = each.find('.//Numero_Visado')
        print('' if dato_Numero_Visado is None else dato_Numero_Visado.text)
        validacsv.writerow(['Numero_Visado', dato_Numero_Visado.text, reglas_validacion.debe_estar_lleno(dato_Numero_Visado.text).get("OK_KO"), reglas_validacion.debe_estar_lleno(dato_Numero_Visado.text).get("Validacion"), date.today()])

        dato_Fecha_Visado = each.find('.//Fecha_Visado')
        print('' if dato_Fecha_Visado is None else dato_Fecha_Visado.text)
        validacsv.writerow(['Fecha_Visado', dato_Fecha_Visado.text, reglas_validacion.debe_estar_lleno(dato_Fecha_Visado.text).get("OK_KO"), reglas_validacion.debe_estar_lleno(dato_Fecha_Visado.text).get("Validacion"), date.today()])

        dato_Numero_Colegiado = each.find('.//Numero_Colegiado')
        print('' if dato_Numero_Colegiado is None else dato_Numero_Colegiado.text)
        validacsv.writerow(['Numero_Colegiado', dato_Numero_Colegiado.text, reglas_validacion.debe_estar_lleno(dato_Numero_Colegiado.text).get("OK_KO"), reglas_validacion.debe_estar_lleno(dato_Numero_Colegiado.text).get("Validacion"), date.today()])

        dato_Colegio_Profesional = each.find('.//Colegio_Profesional')
        print('' if dato_Colegio_Profesional is None else dato_Colegio_Profesional.text)
        validacsv.writerow(['Colegio_Profesional', dato_Colegio_Profesional.text, reglas_validacion.R_Colegio_Profesional(dato_Numero_Colegiado.text).get("OK_KO"), reglas_validacion.R_Colegio_Profesional(dato_Numero_Colegiado.text).get("Validacion"), date.today()])

    for each in root.findall('.//Tecnico_Competente'):
        dato_NIF_NIE = each.find('.//NIF_NIE')
        print('' if dato_NIF_NIE is None else dato_NIF_NIE.text)
        validacsv.writerow(['NIF_NIE', dato_NIF_NIE.text, reglas_validacion.R_NIF_NIE(dato_NIF_NIE.text).get("OK_KO"), reglas_validacion.R_NIF_NIE(dato_NIF_NIE.text).get("Validacion"), date.today()])

        dato_Nombre = each.find('.//Nombre')
        print('' if dato_Nombre is None else dato_Nombre.text)
        validacsv.writerow(['Nombre', dato_Nombre.text, reglas_validacion.debe_estar_lleno(dato_Nombre.text).get("OK_KO"), reglas_validacion.debe_estar_lleno(dato_Nombre.text).get("Validacion"), date.today()])

        dato_Apellido1 = each.find('.//Apellido1')
        print('' if dato_Apellido1 is None else dato_Apellido1.text)
        validacsv.writerow(['Apellido1', dato_Apellido1.text, reglas_validacion.debe_estar_lleno(dato_Apellido1.text).get("OK_KO"), reglas_validacion.debe_estar_lleno(dato_Apellido1.text).get("Validacion"), date.today()])

        dato_Apellido2 = each.find('.//Apellido2')
        print('' if dato_Apellido2 is None else dato_Apellido2.text)
        validacsv.writerow(['Apellido2', dato_Apellido2.text, reglas_validacion.debe_estar_lleno(dato_Apellido2.text).get("OK_KO"), reglas_validacion.debe_estar_lleno(dato_Apellido2.text).get("Validacion"), date.today()])

    for each in root.findall('.//Datos_Emplazamiento'):
        dato_Codigo_Emplazamiento = each.find('.//Codigo_Emplazamiento')
        print('' if dato_Codigo_Emplazamiento is None else dato_Codigo_Emplazamiento.text)
        validacsv.writerow(['Codigo_Emplazamiento', dato_Codigo_Emplazamiento.text, reglas_validacion.debe_estar_lleno(dato_Codigo_Emplazamiento.text).get("OK_KO"), reglas_validacion.debe_estar_lleno(dato_Codigo_Emplazamiento.text).get("Validacion"), date.today()])

        dato_Emplazamiento_Compartido = each.find('.//Emplazamiento_Compartido')
        print('' if dato_Emplazamiento_Compartido is None else dato_Emplazamiento_Compartido.text)
        validacsv.writerow(['Emplazamiento_Compartido', dato_Emplazamiento_Compartido.text, reglas_validacion.debe_estar_lleno(dato_Emplazamiento_Compartido.text).get("OK_KO"), reglas_validacion.debe_estar_lleno(dato_Emplazamiento_Compartido.text).get("Validacion"), date.today()])

        dato_Cod_INE_Termino_Municipal = each.find('.//Cod_INE_Termino_Municipal')
        print('' if dato_Cod_INE_Termino_Municipal is None else dato_Cod_INE_Termino_Municipal.text)
        validacsv.writerow(['Cod_INE_Termino_Municipal', dato_Cod_INE_Termino_Municipal.text, reglas_validacion.debe_estar_lleno(dato_Cod_INE_Termino_Municipal.text).get("OK_KO"), reglas_validacion.debe_estar_lleno(dato_Cod_INE_Termino_Municipal.text).get("Validacion"), date.today()])

        dato_Cod_INE_Provincia = each.find('.//Cod_INE_Provincia')
        print('' if dato_Cod_INE_Provincia is None else dato_Cod_INE_Provincia.text)
        validacsv.writerow(['Cod_INE_Provincia', dato_Cod_INE_Provincia.text, reglas_validacion.debe_estar_lleno(dato_Cod_INE_Provincia.text).get("OK_KO"), reglas_validacion.debe_estar_lleno(dato_Cod_INE_Provincia.text).get("Validacion"), date.today()])

        dato_Latitud = each.find('.//Latitud')
        print('' if dato_Latitud is None else dato_Latitud.text)
        validacsv.writerow(['Latitud', dato_Latitud.text, '', '', date.today()])

        dato_Latitud = each.find('.//Latitud')
        print('' if dato_Latitud is None else dato_Latitud.text)
        validacsv.writerow(['Latitud', dato_Latitud.text, '', '', date.today()])

        dato_Longitud = each.find('.//Longitud')
        print('' if dato_Longitud is None else dato_Longitud.text)
        validacsv.writerow(['Longitud', dato_Longitud.text, '', '', date.today()])

        dato_Datum = each.find('.//Datum')
        print('' if dato_Datum is None else dato_Datum.text)
        validacsv.writerow(['Datum', dato_Datum.text, '', '', date.today()])

        dato_Referencia_Catastral = each.find('.//Referencia_Catastral')
        print('' if dato_Referencia_Catastral is None else dato_Referencia_Catastral.text)
        validacsv.writerow(['Referencia_Catastral', dato_Referencia_Catastral.text, '', '', date.today()])

        dato_Cota_Terreno_Sobre_Nivel_Mar = each.find('.//Cota_Terreno_Sobre_Nivel_Mar')
        print('' if dato_Cota_Terreno_Sobre_Nivel_Mar is None else dato_Cota_Terreno_Sobre_Nivel_Mar.text)
        validacsv.writerow(
            ['Cota_Terreno_Sobre_Nivel_Mar', dato_Cota_Terreno_Sobre_Nivel_Mar.text, '', '', date.today()])

    for each in root.findall('.//Calle'):
        dato_Poblacion = each.find('.//Poblacion')
        print('' if dato_Poblacion is None else dato_Poblacion.text)
        validacsv.writerow(['Poblacion', dato_Poblacion.text, '', '', date.today()])

        dato_Tipo_Via = each.find('.//Tipo_Via')
        print('' if dato_Tipo_Via is None else dato_Tipo_Via.text)
        validacsv.writerow(['Tipo_Via', dato_Tipo_Via.text, '', '', date.today()])

        dato_Nombre_Via = each.find('.//Nombre_Via')
        print('' if dato_Nombre_Via is None else dato_Nombre_Via.text)
        validacsv.writerow(['Nombre_Via', dato_Nombre_Via.text, '', '', date.today()])

        dato_Numero_Portal = each.find('.//Numero_Portal')
        print('' if dato_Numero_Portal is None else dato_Numero_Portal.text)
        validacsv.writerow(['Numero_Portal', dato_Numero_Portal.text, '', '', date.today()])

        dato_Situacion = each.find('.//Situacion')
        print('' if dato_Situacion is None else dato_Situacion.text)
        validacsv.writerow(['Situacion', dato_Situacion.text, '', '', date.today()])

    for each in root.findall('.//Datos_Estacion'):
        dato_Codigo_Estacion = each.find('.//Codigo_Estacion')
        print('' if dato_Codigo_Estacion is None else dato_Codigo_Estacion.text)
        validacsv.writerow(['Codigo_Estacion', dato_Codigo_Estacion.text, '', '', date.today()])

        dato_Tipo_Sistema = each.find('.//Tipo_Sistema')
        print('' if dato_Tipo_Sistema is None else dato_Tipo_Sistema.text)
        validacsv.writerow(['Tipo_Sistema', dato_Tipo_Sistema.text, '', '', date.today()])

        dato_Tipo_Estacion = each.find('.//Tipo_Estacion')
        print('' if dato_Tipo_Estacion is None else dato_Tipo_Estacion.text)
        validacsv.writerow(['Tipo_Estacion', dato_Tipo_Estacion.text, '', '', date.today()])

        dato_Entorno_Sensible = each.find('.//Entorno_Sensible')
        print('' if dato_Entorno_Sensible is None else dato_Entorno_Sensible.text)
        validacsv.writerow(['Entorno_Sensible', dato_Entorno_Sensible.text, '', '', date.today()])

        dato_Num_Sectores_Interiores = each.find('.//Num_Sectores_Interiores')
        print('' if dato_Num_Sectores_Interiores is None else dato_Num_Sectores_Interiores.text)
        validacsv.writerow(['Num_Sectores_Interiores', dato_Num_Sectores_Interiores.text, '', '', date.today()])

        dato_Num_Sectores_Exteriores = each.find('.//Num_Sectores_Exteriores')
        print('' if dato_Num_Sectores_Exteriores is None else dato_Num_Sectores_Exteriores.text)
        validacsv.writerow(['Num_Sectores_Exteriores', dato_Num_Sectores_Exteriores.text, '', '', date.today()])

    for each in root.findall('.//Sector'):
        dato_Tipo_Potencia_Radiada = each.find('.//Tipo_Potencia_Radiada')
        print('' if dato_Tipo_Potencia_Radiada is None else dato_Tipo_Potencia_Radiada.text)
        validacsv.writerow(['Tipo_Potencia_Radiada', dato_Tipo_Potencia_Radiada.text, '', '', date.today()])

        dato_Potencia_Maxima_Total = each.find('.//Potencia_Maxima_Total')
        print('' if dato_Potencia_Maxima_Total is None else dato_Potencia_Maxima_Total.text)
        validacsv.writerow(['Potencia_Maxima_Total', dato_Potencia_Maxima_Total.text, '', '', date.today()])

        dato_Tipo_Potencia_Radiada = each.find('.//Tipo_Potencia_Radiada')
        print('' if dato_Tipo_Potencia_Radiada is None else dato_Tipo_Potencia_Radiada.text)
        validacsv.writerow(['Tipo_Potencia_Radiada', dato_Tipo_Potencia_Radiada.text, '', '', date.today()])

        dato_Unidad_Potencia_Maxima_Total = each.find('.//Unidad_Potencia_Maxima_Total')
        print('' if dato_Unidad_Potencia_Maxima_Total is None else dato_Unidad_Potencia_Maxima_Total.text)
        validacsv.writerow(
            ['Unidad_Potencia_Maxima_Total', dato_Unidad_Potencia_Maxima_Total.text, '', '', date.today()])

        dato_Localizacion_Antena = each.find('.//Localizacion_Antena')
        print('' if dato_Localizacion_Antena is None else dato_Localizacion_Antena.text)
        validacsv.writerow(['Localizacion_Antena', dato_Localizacion_Antena.text, '', '', date.today()])

        dato_Tipo_Antena = each.find('.//Tipo_Antena')
        print('' if dato_Tipo_Antena is None else dato_Tipo_Antena.text)
        validacsv.writerow(['Tipo_Antena', dato_Tipo_Antena.text, '', '', date.today()])

        dato_Polarizacion = each.find('.//Polarizacion')
        print('' if dato_Polarizacion is None else dato_Polarizacion.text)
        validacsv.writerow(['Polarizacion', dato_Polarizacion.text, '', '', date.today()])

        dato_Altura_Antena_Sobre_Terreno = each.find('.//Altura_Antena_Sobre_Terreno')
        print('' if dato_Altura_Antena_Sobre_Terreno is None else dato_Altura_Antena_Sobre_Terreno.text)
        validacsv.writerow(['Altura_Antena_Sobre_Terreno', dato_Altura_Antena_Sobre_Terreno.text, '', '', date.today()])

        dato_Inclinacion_Haz_Sobre_Horizontal = each.find('.//Inclinacion_Haz_Sobre_Horizontal')
        print('' if dato_Inclinacion_Haz_Sobre_Horizontal is None else dato_Inclinacion_Haz_Sobre_Horizontal.text)
        validacsv.writerow(
            ['Inclinacion_Haz_Sobre_Horizontal', dato_Inclinacion_Haz_Sobre_Horizontal.text, '', '', date.today()])

    for each in root.findall('.//Antena_Directiva'):
        dato_Tipo_Ganancia = each.find('.//Tipo_Ganancia')
        print('' if dato_Tipo_Ganancia is None else dato_Tipo_Ganancia.text)
        validacsv.writerow(['Tipo_Ganancia', dato_Tipo_Ganancia.text, '', '', date.today()])

        dato_Ganancia_Antena = each.find('.//Ganancia_Antena')
        print('' if dato_Ganancia_Antena is None else dato_Ganancia_Antena.text)
        validacsv.writerow(['Ganancia_Antena', dato_Ganancia_Antena.text, '', '', date.today()])

        dato_Apertura_Horizontal_Haz = each.find('.//Apertura_Horizontal_Haz')
        print('' if dato_Apertura_Horizontal_Haz is None else dato_Apertura_Horizontal_Haz.text)
        validacsv.writerow(['Apertura_Horizontal_Haz', dato_Apertura_Horizontal_Haz.text, '', '', date.today()])

        dato_Apertura_Vertical_Haz = each.find('.//Apertura_Vertical_Haz')
        print('' if dato_Apertura_Vertical_Haz is None else dato_Apertura_Vertical_Haz.text)
        validacsv.writerow(['Apertura_Vertical_Haz', dato_Apertura_Vertical_Haz.text, '', '', date.today()])

        dato_Acimut_Maxima_Radiacion = each.find('.//Acimut_Maxima_Radiacion')
        print('' if dato_Acimut_Maxima_Radiacion is None else dato_Acimut_Maxima_Radiacion.text)
        validacsv.writerow(['Acimut_Maxima_Radiacion', dato_Acimut_Maxima_Radiacion.text, '', '', date.today()])

        dato_Nivel_Lobulos_Secundarios = each.find('.//Nivel_Lobulos_Secundarios')
        print('' if dato_Nivel_Lobulos_Secundarios is None else dato_Nivel_Lobulos_Secundarios.text)
        validacsv.writerow(['Nivel_Lobulos_Secundarios', dato_Nivel_Lobulos_Secundarios.text, '', '', date.today()])

    for each in root.findall('.//Volumen_Referencia'):
        dato_Forma_Volumen = each.find('.//Forma_Volumen')
        print('' if dato_Forma_Volumen is None else dato_Forma_Volumen.text)
        validacsv.writerow(['Forma_Volumen', dato_Forma_Volumen.text, '', '', date.today()])

        dato_Distancia_Referencia = each.find('.//Distancia_Referencia')
        print('' if dato_Distancia_Referencia is None else dato_Distancia_Referencia.text)
        validacsv.writerow(['Distancia_Referencia', dato_Distancia_Referencia.text, '', '', date.today()])

        dato_Coeficiente_Reflexion = each.find('.//Coeficiente_Reflexion')
        print('' if dato_Coeficiente_Reflexion is None else dato_Coeficiente_Reflexion.text)
        validacsv.writerow(['Coeficiente_Reflexion', dato_Coeficiente_Reflexion.text, '', '', date.today()])

    for each in root.findall('.//Punto_Medida'):
        dato_IdPunto = each.find('.//IdPunto')
        print('' if dato_IdPunto is None else dato_IdPunto.text)
        validacsv.writerow(['IdPunto', dato_IdPunto.text, '', '', date.today()])

        dato_Distancia = each.find('.//Distancia')
        print('' if dato_Distancia is None else dato_Distancia.text)
        validacsv.writerow(['Distancia', dato_Distancia.text, '', '', date.today()])

        dato_Acimut = each.find('.//Acimut')
        print('' if dato_Acimut is None else dato_Acimut.text)
        validacsv.writerow(['Acimut', dato_Acimut.text, '', '', date.today()])

    for each in root.findall('.//Punto_Sensible'):
        dato_Situacion = each.find('.//Situacion')
        print('' if dato_Situacion is None else dato_Situacion.text)
        validacsv.writerow(['Situacion', dato_Situacion.text, '', '', date.today()])

        dato_Tipo_Espacio_Sensible = each.find('.//Tipo_Espacio_Sensible')
        print('' if dato_Tipo_Espacio_Sensible is None else dato_Tipo_Espacio_Sensible.text)
        validacsv.writerow(['Tipo_Espacio_Sensible', dato_Tipo_Espacio_Sensible.text, '', '', date.today()])

        dato_Tipo_Via = each.find('.//Tipo_Via')
        print('' if dato_Tipo_Via is None else dato_Tipo_Via.text)
        validacsv.writerow(['Tipo_Via', dato_Tipo_Via.text, '', '', date.today()])

        dato_Nombre_Via = each.find('.//Nombre_Via')
        print('' if dato_Nombre_Via is None else dato_Nombre_Via.text)
        validacsv.writerow(['Nombre_Via', dato_Nombre_Via.text, '', '', date.today()])

        dato_Codigo_Postal = each.find('.//Codigo_Postal')
        print('' if dato_Codigo_Postal is None else dato_Codigo_Postal.text)
        validacsv.writerow(['Codigo_Postal', dato_Codigo_Postal.text, '', '', date.today()])

        dato_Poblacion = each.find('.//Poblacion')
        print('' if dato_Poblacion is None else dato_Poblacion.text)
        validacsv.writerow(['Poblacion', dato_Poblacion.text, '', '', date.today()])

        dato_Cod_INE_Termino_Municipal = each.find('.//Cod_INE_Termino_Municipal')
        print('' if dato_Cod_INE_Termino_Municipal is None else dato_Cod_INE_Termino_Municipal.text)
        validacsv.writerow(['Cod_INE_Termino_Municipal', dato_Cod_INE_Termino_Municipal.text, '', '', date.today()])

        dato_Cod_INE_Provincia = each.find('.//Cod_INE_Provincia')
        print('' if dato_Cod_INE_Provincia is None else dato_Cod_INE_Provincia.text)
        validacsv.writerow(['Cod_INE_Provincia', dato_Cod_INE_Provincia.text, '', '', date.today()])

    for each in root.findall('.//Datos_Medicion'):
        dato_Tecnico_Responsable = each.find('.//Tecnico_Responsable')
        print('' if dato_Tecnico_Responsable is None else dato_Tecnico_Responsable.text)
        validacsv.writerow(['Tecnico_Responsable', dato_Tecnico_Responsable.text, '', '', date.today()])

        dato_Fecha_Medicion = each.find('.//Fecha_Medicion')
        print('' if dato_Fecha_Medicion is None else dato_Fecha_Medicion.text)
        validacsv.writerow(['Fecha_Medicion', dato_Fecha_Medicion.text, '', '', date.today()])

    for each in root.findall('.//Equipo_Medida_Fase1'):
        dato_IdEquipo = each.find('.//IdEquipo')
        print('' if dato_IdEquipo is None else dato_IdEquipo.text)
        validacsv.writerow(['IdEquipo', dato_IdEquipo.text, '', '', date.today()])

        dato_Fecha_Ultima_Calibracion = each.find('.//Fecha_Ultima_Calibracion')
        print('' if dato_Fecha_Ultima_Calibracion is None else dato_Fecha_Ultima_Calibracion.text)
        validacsv.writerow(['Fecha_Ultima_Calibracion', dato_Fecha_Ultima_Calibracion.text, '', '', date.today()])

        dato_Umbral_Deteccion_Vm = each.find('.//Umbral_Deteccion_Vm')
        print('' if dato_Umbral_Deteccion_Vm is None else dato_Umbral_Deteccion_Vm.text)
        validacsv.writerow(['Umbral_Deteccion_Vm', dato_Umbral_Deteccion_Vm.text, '', '', date.today()])

        dato_Longitud_Cable = each.find('.//Longitud_Cable')
        print('' if dato_Longitud_Cable is None else dato_Longitud_Cable.text)
        validacsv.writerow(['Longitud_Cable', dato_Longitud_Cable.text, '', '', date.today()])

    for each in root.findall('.//Medidor'):
        dato_Marca_Medidor = each.find('.//Marca_Medidor')
        print('' if dato_Marca_Medidor is None else dato_Marca_Medidor.text)
        validacsv.writerow(['Marca_Medidor', dato_Marca_Medidor.text, '', '', date.today()])

        dato_Modelo_Medidor = each.find('.//Modelo_Medidor')
        print('' if dato_Modelo_Medidor is None else dato_Modelo_Medidor.text)
        validacsv.writerow(['Modelo_Medidor', dato_Modelo_Medidor.text, '', '', date.today()])

        dato_Numero_Serie_Medidor = each.find('.//Numero_Serie_Medidor')
        print('' if dato_Numero_Serie_Medidor is None else dato_Numero_Serie_Medidor.text)
        validacsv.writerow(['Numero_Serie_Medidor', dato_Numero_Serie_Medidor.text, '', '', date.today()])

    for each in root.findall('.//Antena'):
        dato_Marca_Antena = each.find('.//Marca_Antena')
        print('' if dato_Marca_Antena is None else dato_Marca_Antena.text)
        validacsv.writerow(['Marca_Antena', dato_Marca_Antena.text, '', '', date.today()])

        dato_Modelo_Antena = each.find('.//Modelo_Antena')
        print('' if dato_Modelo_Antena is None else dato_Modelo_Antena.text)
        validacsv.writerow(['Modelo_Antena', dato_Modelo_Antena.text, '', '', date.today()])

        dato_Numero_Serie_Antena = each.find('.//Numero_Serie_Antena')
        print('' if dato_Numero_Serie_Antena is None else dato_Numero_Serie_Antena.text)
        validacsv.writerow(['Numero_Serie_Antena', dato_Numero_Serie_Antena.text, '', '', date.today()])

    for each in root.findall('.//Medida_Fase1'):
        dato_IdPunto = each.find('.//IdPunto')
        print('' if dato_IdPunto is None else dato_IdPunto.text)
        validacsv.writerow(['IdPunto', dato_IdPunto.text, '', '', date.today()])

        dato_IdEquipo = each.find('.//IdEquipo')
        print('' if dato_IdEquipo is None else dato_IdEquipo.text)
        validacsv.writerow(['IdEquipo', dato_IdEquipo.text, '', '', date.today()])

        dato_Hora_Inicio_Medicion = each.find('.//Hora_Inicio_Medicion')
        print('' if dato_Hora_Inicio_Medicion is None else dato_Hora_Inicio_Medicion.text)
        validacsv.writerow(['Hora_Inicio_Medicion', dato_Hora_Inicio_Medicion.text, '', '', date.today()])

        dato_Nivel_Referencia_Vm = each.find('.//Nivel_Referencia_Vm')
        print('' if dato_Nivel_Referencia_Vm is None else dato_Nivel_Referencia_Vm.text)
        validacsv.writerow(['Nivel_Referencia_Vm', dato_Nivel_Referencia_Vm.text, '', '', date.today()])

        dato_Nivel_Decision_Vm = each.find('.//Nivel_Decision_Vm')
        print('' if dato_Nivel_Decision_Vm is None else dato_Nivel_Decision_Vm.text)
        validacsv.writerow(['Nivel_Decision_Vm', dato_Nivel_Decision_Vm.text, '', '', date.today()])

        dato_Valor_Medido_Promediado_Vm = each.find('.//Valor_Medido_Promediado_Vm')
        print('' if dato_Valor_Medido_Promediado_Vm is None else dato_Valor_Medido_Promediado_Vm.text)
        validacsv.writerow(['Valor_Medido_Promediado_Vm', dato_Valor_Medido_Promediado_Vm.text, '', '', date.today()])

        dato_Valor_Calculado_Vm = each.find('.//Valor_Calculado_Vm')
        print('' if dato_Valor_Calculado_Vm is None else dato_Valor_Calculado_Vm.text)
        validacsv.writerow(['Valor_Calculado_Vm', dato_Valor_Calculado_Vm.text, '', '', date.today()])

        dato_Diferencia_Vm = each.find('.//Diferencia_Vm')
        print('' if dato_Diferencia_Vm is None else dato_Diferencia_Vm.text)
        validacsv.writerow(['Diferencia_Vm', dato_Diferencia_Vm.text, '', '', date.today()])

    for each in root.findall('.//Documento'):
        dato_Nombre = each.find('.//Nombre')
        print('' if dato_Nombre is None else dato_Nombre.text)
        validacsv.writerow(['Nombre', dato_Nombre.text, '', '', date.today()])

        dato_Extension = each.find('.//Extension')
        print('' if dato_Extension is None else dato_Extension.text)
        validacsv.writerow(['Extension', dato_Extension.text, '', '', date.today()])

        dato_Codificacion = each.find('.//Codificacion')
        print('' if dato_Codificacion is None else dato_Codificacion.text)
        validacsv.writerow(['Codificacion', dato_Codificacion.text, '', '', date.today()])

        dato_Contenido = each.find('.//Contenido')
        print('' if dato_Contenido is None else dato_Contenido.text)
        validacsv.writerow(['Contenido', dato_Contenido.text, '', '', date.today()])

# GRABACION EN DOCUMENTO EXCEL
wb = xlsxwriter.Workbook(rootDir + nameZip + '.xlsx')
sh = wb.add_worksheet('gkz')

with open(rootDir + nameZip + '.csv', 'r') as f:
    reader = csv.reader(f, delimiter=';', quotechar='|')
    for r, row in enumerate(reader):
        for c, val in enumerate(row):
            sh.write(r, c, val)

wb.close()

# MOVER FICHEROS
if bandera_mover == 0:  # No existen errores
    shutil.move(rootDir + nameZip + ".zip", correctosDir + nameZip + ".zip")
elif bandera_mover == 1:    # Existen reparos
    shutil.move(rootDir + nameZip + ".csv", reparosDir + nameZip + ".csv")
    shutil.move(rootDir + nameZip + ".xlsx", reparosDir + nameZip + ".xlsx")
    shutil.move(rootDir + nameZip + ".zip", reparosDir + nameZip + ".zip")
elif bandera_mover == 2:    # Existen rechazos
    shutil.move(rootDir + nameZip + ".csv", rechazosDir + nameZip + ".csv")
    shutil.move(rootDir + nameZip + ".xlsx", rechazosDir + nameZip + ".xlsx")
    shutil.move(rootDir + nameZip + ".zip", rechazosDir + nameZip + ".zip")

# ELIMINAR TEMPORALES
shutil.rmtree(rootDir + carpeta)

