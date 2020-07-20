import os
import zipfile
import rarfile
from principal import valida_xml_individual_base

# DECLARACION DE VARIABLES GLOBALES
nameZip = ""
rootDir = "D:/EMR_Auditorias_Python/Auditorias/Resultado/Carpeta_de_Trabajo/"
rarfile.UNRAR_TOOL = 'D:/EMR_Auditorias_Python/Ficheros_Respaldo/UnRAR.exe'
dirRarFile='D:/EMR_Auditorias_Python/Auditorias/Resultado/Carpeta_de_Trabajo/IB0641/13520/s1700_n0001_r00_BAL0032V_BALR0032V_ER1_A_HUAWEI_103719_1.rar'

def extrae_datos(rootDir):
    directories = os.listdir(rootDir)
    rootDir_sub = rootDir
    for file in directories:
        if os.path.isdir(os.path.join(rootDir, file)):
            print("Es una carpeta: " + rootDir + file)
            filename = os.path.basename(file)
            (carpeta, ext) = os.path.splitext(filename)
            rootDir_sub = rootDir_sub + "/" + file
            extrae_datos(rootDir_sub)
        else:
            if file.endswith("zip"):
                print("Es un zip: " + rootDir + '/' + file)
                (carpeta_zip, ext_zip) = os.path.splitext(file)
                with zipfile.ZipFile(rootDir + '/' + file, 'r') as zip_ref_zip:
                    zip_ref_zip.extractall(rootDir) #zip_ref_zip.extractall(rootDir + "/" + carpeta_zip)
            elif file.endswith("rar"):
                print("Es un rar: " + rootDir + '/' + file)
                (carpeta_rar, ext_rar) = os.path.splitext(file)
                r = rarfile.RarFile(rootDir + '/' + file)
                r.extractall(rootDir) #r.extractall(rootDir + "/" + carpeta_rar)
                r.close()


def extrae_datos_recursivo(rootDir, nivel):
    for i in range(nivel):
        try:
            extrae_datos(rootDir)
        except:
            print("Finalizado por Carpeta")


# Llamada principal
directories = os.listdir(rootDir)
for file in directories:
    extrae_datos_recursivo(rootDir, 5)


'''
(fichero_rar, ext_rar) = os.path.splitext(os.path.basename(dirRarFile))
r = rarfile.RarFile(dirRarFile)
r.extractall('D:/EMR_Auditorias_Python/Auditorias/Resultado/Carpeta_de_Trabajo/IB0641/13520')
r.close()
'''

'''
    for files_sub in os.listdir(rootDir + carpeta):
        if os.path.isdir(os.path.join(rootDir + carpeta, files_sub)):
            print(files_sub)
            for files_sub_sub in os.listdir(rootDir + carpeta + "\\" + files_sub):
                if files_sub_sub.endswith("zip"):
                    (carpeta_sub_sub, ext_sub_sub) = os.path.splitext(files_sub_sub)
                    with zipfile.ZipFile(rootDir + carpeta + "\\" + files_sub + "\\" + files_sub_sub,
                                         'r') as zip_ref_sub_sub:
                        zip_ref_sub_sub.extractall(rootDir + carpeta + "\\" + files_sub + "\\" + carpeta_sub_sub)
        else:
            for files_sub_sub in os.listdir(rootDir + carpeta):
                if files_sub_sub.endswith("zip"):
                    (carpeta_sub_sub, ext_sub_sub) = os.path.splitext(files_sub_sub)
                    with zipfile.ZipFile(rootDir + carpeta + "\\" + "\\" + files_sub_sub,
                                         'r') as zip_ref_sub_sub:
                        zip_ref_sub_sub.extractall(rootDir + carpeta + "\\" + "\\" + carpeta_sub_sub)




# LISTAR Y DESCOMPRIMIR SEGUNDO ZIP
directories = os.listdir(rootDir)
for file in directories:
    if file.endswith("zip"):
        filename = os.path.basename(file)
        (carpeta, ext) = os.path.splitext(filename)
        nameZip = file
        print(carpeta)
        print(file)
        with zipfile.ZipFile(rootDir + "\\" + file, 'r') as zip_ref:
            zip_ref.extractall(rootDir + carpeta)
            # proceso_principal.principal(rootDir, nameZip, carpeta)
        # DENTRO DE CARPETA
        for files_sub in os.listdir(rootDir + carpeta):
            if os.path.isdir(os.path.join(rootDir + carpeta, files_sub)):
                print(files_sub)
                for files_sub_sub in os.listdir(rootDir + carpeta + "\\" + files_sub):
                    if files_sub_sub.endswith("zip"):
                        (carpeta_sub_sub, ext_sub_sub) = os.path.splitext(files_sub_sub)
                        with zipfile.ZipFile(rootDir + carpeta + "\\" + files_sub + "\\" + files_sub_sub,
                                             'r') as zip_ref_sub_sub:
                            zip_ref_sub_sub.extractall(rootDir + carpeta + "\\" + files_sub + "\\" + carpeta_sub_sub)

                        # DENTRO DE SUB CARPETA
                        for files_sub_sub_sub in os.listdir(
                                rootDir + carpeta + "\\" + files_sub + "\\" + carpeta_sub_sub):
                            if files_sub_sub_sub.endswith("zip"):
                                (carpeta_sub_sub_sub, ext_sub_sub_sub) = os.path.splitext(files_sub_sub_sub)
                                with zipfile.ZipFile(
                                        rootDir + carpeta + "\\" + files_sub + "\\" + carpeta_sub_sub + "\\" + files_sub_sub_sub,
                                        'r') as zip_ref_sub_sub_sub:
                                    zip_ref_sub_sub_sub.extractall(
                                        rootDir + carpeta + "\\" + files_sub + "\\" + carpeta_sub_sub + "\\" + carpeta_sub_sub_sub)
                    # SI SE TRATA DE UN RAR
                    if files_sub_sub.endswith("rar"):
                        print("Se encontró rar")
                        (carpeta_sub_sub, ext_sub_sub) = os.path.splitext(files_sub_sub)
                        r = rarfile.RarFile(rootDir + carpeta + "\\" + files_sub + "\\" + files_sub_sub)
                        r.extractall(rootDir + carpeta + "\\" + files_sub + "\\" + carpeta_sub_sub)
                        r.close()
                    # SI SE TRATA DE UN 7z
                    if files_sub_sub.endswith("7z"):
                        print("Se encontró rar")
    if file.endswith("rar"):
        print("Se encontró rar")
        filename = os.path.basename(file)
        (carpeta, ext) = os.path.splitext(filename)
        nameZip = file
        print(carpeta)
        print(file)
        r_l = rarfile.RarFile(rootDir + "\\" + file)
        r_l.extractall(rootDir + carpeta)
        r_l.close()
        # proceso_principal.principal(rootDir, nameZip, carpeta)
        # DENTRO DE CARPETA
        for files_sub in os.listdir(rootDir + carpeta):
            if os.path.isdir(os.path.join(rootDir + carpeta, files_sub)):
                print(files_sub)
                for files_sub_sub in os.listdir(rootDir + carpeta + "\\" + files_sub):
                    if files_sub_sub.endswith("zip"):
                        (carpeta_sub_sub, ext_sub_sub) = os.path.splitext(files_sub_sub)
                        with zipfile.ZipFile(rootDir + carpeta + "\\" + files_sub + "\\" + files_sub_sub,
                                             'r') as zip_ref_sub_sub:
                            zip_ref_sub_sub.extractall(rootDir + carpeta + "\\" + files_sub + "\\" + carpeta_sub_sub)

                        # DENTRO DE SUB CARPETA
                        for files_sub_sub_sub in os.listdir(
                                rootDir + carpeta + "\\" + files_sub + "\\" + carpeta_sub_sub):
                            if files_sub_sub_sub.endswith("zip"):
                                (carpeta_sub_sub_sub, ext_sub_sub_sub) = os.path.splitext(files_sub_sub_sub)
                                with zipfile.ZipFile(
                                        rootDir + carpeta + "\\" + files_sub + "\\" + carpeta_sub_sub + "\\" + files_sub_sub_sub,
                                        'r') as zip_ref_sub_sub_sub:
                                    zip_ref_sub_sub_sub.extractall(
                                        rootDir + carpeta + "\\" + files_sub + "\\" + carpeta_sub_sub + "\\" + carpeta_sub_sub_sub)
                    # SI SE TRATA DE UN RAR
                    if files_sub_sub.endswith("rar"):
                        print("Se encontró rar")
                        (carpeta_sub_sub, ext_sub_sub) = os.path.splitext(files_sub_sub)
                        r = rarfile.RarFile(rootDir + carpeta + "\\" + files_sub + "\\" + files_sub_sub)
                        r.extractall(rootDir + carpeta + "\\" + files_sub + "\\" + carpeta_sub_sub)
                        r.close()
                    # SI SE TRATA DE UN 7z
                    if files_sub_sub.endswith("7z"):
                        print("Se encontró rar")

'''
