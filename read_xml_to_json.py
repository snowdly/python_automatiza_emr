# import json module and xmltodict
# module provided by python
import json
import xmltodict
import xlsxwriter


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
# open the input xml file and read
# data in form of python dictionary
# using xmltodict module
with open("D:\OCAMPOS\PYTHON_AUTOMATIZACION\CATT0309Z_CATR0309Z_ER1_A_ARCA_103945_1.xml") as xml_file:
    data_dict = xmltodict.parse(xml_file.read())
    xml_file.close()

    # generate the object using json.dumps()
    # corresponding to json data

    json_data = json.dumps(data_dict)
    # print(json_data)

    # Write the json data to output
    # json file
    with open("D:\OCAMPOS\PYTHON_AUTOMATIZACION\CATT0309Z_CATR0309Z_ER1_A_ARCA_103945_1.json", "w") as json_file:
        json_file.write(json_data)
        json_file.close()
