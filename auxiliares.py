import shutil
import zipfile
import os

# DECLARACION DE VARIABLES GLOBALES
nameZip = "BX0309"
rootDir = "D:\EMR_Auditorias_Python\Auditorias\Resultado\Temporal\\"
nameFile = "CATT0309Z_CATR0309Z_ER1_A_ARCA_103945_1"
correctosDir = "D:\EMR_Auditorias_Python\Auditorias\Resultado\Correctos\\"
rechazosDir = "D:\EMR_Auditorias_Python\Auditorias\Resultado\Rechazos\\"
reparosDir = "D:\EMR_Auditorias_Python\Auditorias\Resultado\Reparos\\"
bandera_mover = 2

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
