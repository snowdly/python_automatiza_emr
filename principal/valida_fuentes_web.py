import datetime
import os
from principal import procesos_comunes
from validacion_web import infoantenas
from validacion_web import Accesos_Web
import logging

def principal_a():
    # Retorna resultado del proceso
    r = dict()
    r['Etapa_Validacion'] = 'Proceso de validación contra fuentes PDF'
    r['Resultado'] = 'Pendiente'
    r['Fecha'] = datetime.datetime.now()
    return r

def principal(rootDir, ficheros_respaldo):
    logging.debug('INICIA Proceso de validación contra fuentes web')
    # Obtener los xml
    rf = procesos_comunes.obtiene_primer_xml(rootDir)
    #print(rf)
    r = dict()
    if rf['OK_KO'] == 'OK':
        # Retorna ventanas de infoantenas
        latitud = procesos_comunes.valor_elemento_xml(rf['Fichero'], './/Estacion_Certificada/Datos_Emplazamiento/Latitud')['Valor']
        longitud = procesos_comunes.valor_elemento_xml(rf['Fichero'], './/Estacion_Certificada/Datos_Emplazamiento/Longitud')['Valor']
        #print(latitud, longitud)
        try:
            municipio, provincia=infoantenas.obtiene_datos(longitud, latitud, ficheros_respaldo)
        except Exception as e:
            logging.debug('Se ha producido un error API de infoantenas')
            logging.debug(e)
        try:
            # Llama a función para levantar todos las webs
            Accesos_Web.consulta_webs(rf['Fichero'], ficheros_respaldo, municipio, provincia)
        except Exception as e:
            logging.debug('Se ha producido un error Proceso de validación contra fuentes web')
            logging.debug(e)

        # Retorna resultado del proceso
        r['Resultado'] = 'Finalizado'
    else:
        r['Resultado'] = 'Finalizado reparo - No se pudieron consultas las fuentes web.'
    r['Etapa_Validacion'] = 'Proceso de validación contra fuentes web'
    r['Fecha'] = datetime.datetime.now()
    return r

