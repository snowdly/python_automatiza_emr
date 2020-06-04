import xml.etree.ElementTree as ET

tree = ET.parse('D:\OCAMPOS\PYTHON_AUTOMATIZACION\CATT0309Z_CATR0309Z_ER1_A_ARCA_103945_1.xml')
root = tree.getroot()

''''
for neighbor in root.iter('Datos_Certificacion'):
    print(neighbor.tag)
'''

for each in root.findall('.//Datos_Certificacion'):
    dato_Tipo_Certificacion = each.find('.//Tipo_Certificacion')
    print('' if dato_Tipo_Certificacion is None else dato_Tipo_Certificacion.text)
    dato_Tipo_Solicitud = each.find('.//Tipo_Solicitud')
    print('' if dato_Tipo_Solicitud is None else dato_Tipo_Solicitud.text)
    dato_Titular_Nombre_Razon_Social = each.find('.//Titular_Nombre_Razon_Social')
    print('' if dato_Titular_Nombre_Razon_Social is None else dato_Titular_Nombre_Razon_Social.text)
    dato_Expediente_Concesional = each.find('.//Expediente_Concesional')
    print('' if dato_Expediente_Concesional is None else dato_Expediente_Concesional.text)

for each in root.findall('.//Datos_Visado'):
    dato_Numero_Visado = each.find('.//Numero_Visado')
    print('' if dato_Numero_Visado is None else dato_Numero_Visado.text)
    dato_Fecha_Visado = each.find('.//Fecha_Visado')
    print('' if dato_Fecha_Visado is None else dato_Fecha_Visado.text)
    dato_Numero_Colegiado = each.find('.//Numero_Colegiado')
    print('' if dato_Numero_Colegiado is None else dato_Numero_Colegiado.text)
    dato_Colegio_Profesional = each.find('.//Colegio_Profesional')
    print('' if dato_Colegio_Profesional is None else dato_Colegio_Profesional.text)