import fitz


def pdf_fitz(fichero_pdf):
    print(fichero_pdf)
    try:
        b = open(fichero_pdf, "rb").read()
        #doc = fitz.open(fichero_pdf)
        print(b)
    except Exception as e:
        print(e)


fichero_pdf = 'D:\EMR_Auditorias_Python\Auditorias\ZX0353\Carpeta_de_Trabajo\ZX0353\ARAE0353A_ARAR0353A_ER1_M_ZTE_126468_3\ARAE0353A_ARAR0353A_ER1_M_ZTE_126468_3.pdf'
#fichero_pdf = r'D:/EMR_Auditorias_Python\Auditorias\ZX0353\Carpeta_de_Trabajo\ZX0353\ARAE0353A_ARAR0353A_ER1_M_ZTE_126468_3\ARAE0353A_ARAR0353A_ER1_M_ZTE_126428_3.pdf'
#fichero_pdf_a = 'D:\\EMR_Auditorias_Python\\Auditorias\\ZX0353\\Carpeta_de_Trabajo\\ZX0353\\ARAE0353A_ARAR0353A_ER1_M_ZTE_126468_3\\ARAE0353A_ARAR0353A_ER1_M_ZTE_126428_3.pdf'
#fichero_pdf = 'D:/EMR_Auditorias_Python/Auditorias/ZX0353/Carpeta_de_Trabajo/ZX0353/ARAE0353A_ARAR0353A_ER1_M_ZTE_126468_3/ARAE0353A_ARAR0353A_ER1_M_ZTE_126428_3.pdf'

r = pdf_fitz(fichero_pdf)