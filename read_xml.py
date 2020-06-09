import xml.etree.ElementTree as ET
import xlsxwriter
import csv
from datetime import date


# CREACION DE FICHERO DE VALIDACION XLSX
workbook = xlsxwriter.Workbook(
    'D:\OCAMPOS\PYTHON_AUTOMATIZACION\CATT0309Z_CATR0309Z_ER1_A_ARCA_103945_1_VALIDACION.xlsx')
worksheet = workbook.add_worksheet()
worksheet.write(0, 0, "Etiqueta")
worksheet.write(0, 1, "Valor")
worksheet.write(0, 2, "OK_KO")
worksheet.write(0, 3, "Validación")
worksheet.write(0, 4, "Fecha_Hora")
workbook.close()

# OBTIENE FICHERO XML
tree = ET.parse('D:\OCAMPOS\PYTHON_AUTOMATIZACION\CATT0309Z_CATR0309Z_ER1_A_ARCA_103945_1.xml')
root = tree.getroot()

# CREACION DE FICHERO DE VALIDACION CSV
with open('D:\OCAMPOS\PYTHON_AUTOMATIZACION\CATT0309Z_CATR0309Z_ER1_A_ARCA_103945_1_VALIDACION.csv', 'w', newline='') as csvfile:
    validacsv = csv.writer(csvfile, delimiter=';',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    validacsv = csv.writer(csvfile, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    validacsv.writerow(['Etiqueta', 'Valor', 'OK_KO', 'Validacion', 'Fecha_Hora'])

    # VALIDACIÓN Y ESCRITURA PARA CADA ETIQUETA DEL XML
    for each in root.findall('.//Datos_Certificacion'):
        dato_Tipo_Certificacion = each.find('.//Tipo_Certificacion')
        print('' if dato_Tipo_Certificacion is None else dato_Tipo_Certificacion.text)
        validacsv.writerow(['Datos_Certificacion', dato_Tipo_Certificacion.text, '', '', date.today()])

        dato_Tipo_Solicitud = each.find('.//Tipo_Solicitud')
        print('' if dato_Tipo_Solicitud is None else dato_Tipo_Solicitud.text)
        validacsv.writerow(['Tipo_Solicitud', dato_Tipo_Solicitud.text, '', '', date.today()])

        dato_Titular_Nombre_Razon_Social = each.find('.//Titular_Nombre_Razon_Social')
        print('' if dato_Titular_Nombre_Razon_Social is None else dato_Titular_Nombre_Razon_Social.text)
        validacsv.writerow(['Titular_Nombre_Razon_Social', dato_Titular_Nombre_Razon_Social.text, '', '', date.today()])

        dato_Expediente_Concesional = each.find('.//Expediente_Concesional')
        print('' if dato_Expediente_Concesional is None else dato_Expediente_Concesional.text)
        validacsv.writerow(['Expediente_Concesional', dato_Expediente_Concesional.text, '', '', date.today()])

    for each in root.findall('.//Datos_Visado'):
        dato_Numero_Visado = each.find('.//Numero_Visado')
        print('' if dato_Numero_Visado is None else dato_Numero_Visado.text)
        validacsv.writerow(['Numero_Visado', dato_Numero_Visado.text, '', '', date.today()])

        dato_Fecha_Visado = each.find('.//Fecha_Visado')
        print('' if dato_Fecha_Visado is None else dato_Fecha_Visado.text)
        validacsv.writerow(['Fecha_Visado', dato_Fecha_Visado.text, '', '', date.today()])

        dato_Numero_Colegiado = each.find('.//Numero_Colegiado')
        print('' if dato_Numero_Colegiado is None else dato_Numero_Colegiado.text)
        validacsv.writerow(['Numero_Colegiado', dato_Numero_Colegiado.text, '', '', date.today()])

        dato_Colegio_Profesional = each.find('.//Colegio_Profesional')
        print('' if dato_Colegio_Profesional is None else dato_Colegio_Profesional.text)
        validacsv.writerow(['Colegio_Profesional', dato_Colegio_Profesional.text, '', '', date.today()])

    for each in root.findall('.//Tecnico_Competente'):
        dato_NIF_NIE = each.find('.//NIF_NIE')
        print('' if dato_NIF_NIE is None else dato_NIF_NIE.text)
        validacsv.writerow(['NIF_NIE', dato_NIF_NIE.text, '', '', date.today()])

        dato_Nombre = each.find('.//Nombre')
        print('' if dato_Nombre is None else dato_Nombre.text)
        validacsv.writerow(['Nombre', dato_Nombre.text, '', '', date.today()])

        dato_Apellido1 = each.find('.//Apellido1')
        print('' if dato_Apellido1 is None else dato_Apellido1.text)
        validacsv.writerow(['Apellido1', dato_Apellido1.text, '', '', date.today()])

        dato_Apellido2 = each.find('.//Apellido2')
        print('' if dato_Apellido2 is None else dato_Apellido2.text)
        validacsv.writerow(['Apellido2', dato_Apellido2.text, '', '', date.today()])
