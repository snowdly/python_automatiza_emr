import datetime
import os
from principal import procesos_comunes
from validacion_web import infoantenas
from validacion_web import Accesos_Web


def principal(rootDir, ficheros_respaldo):
    # Obtener los xml
    for fichero in procesos_comunes.lista_xml(rootDir):
        fichero_nombre, fichero_extension = os.path.splitext(os.path.basename(fichero))

    # Retorna ventanas de infoantenas
    print(fichero)
    print(fichero_nombre)
    print(fichero_extension)
    latitud = procesos_comunes.valor_elemento_xml(fichero, './/Estacion_Certificada/Datos_Emplazamiento/Latitud')['Valor']
    longitud = procesos_comunes.valor_elemento_xml(fichero, './/Estacion_Certificada/Datos_Emplazamiento/Longitud')['Valor']
    print(latitud, longitud)
    #infoantenas.obtiene_datos(longitud, latitud, ficheros_respaldo)

    # Llama a función para levantar todos las webs
    Accesos_Web.consulta_webs(fichero, ficheros_respaldo)

    # Retorna resultado del proceso
    r = dict()
    r['Etapa_Validacion'] = 'Proceso de validación contra fuentes web'
    r['Resultado'] = 'Finalizado'
    r['Fecha'] = datetime.datetime.now()
    return r


#principal('D:/EMR_Auditorias_Python/Auditorias/PO6100/Carpeta_de_Trabajo/',
#          'D:/EMR_Auditorias_Python/Auditorias/PO6100/Reporte_Estado_Auditoria/', 'GALB6100E_GALR6100E_ER1_M_ARCA_112601_1')

#principal('D:/EMR_Auditorias_Python/Auditorias/PO6100/Carpeta_de_Trabajo/', '', '')