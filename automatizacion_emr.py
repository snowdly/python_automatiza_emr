import logging
import os
import pandas as pd
from principal import procesos_comunes
from principal import audita_comprimidos
from principal import lee_directorio
from principal import compara_xml
from principal import valida_xml_entre
from validacion_ine_bbdd import valida_ine_bd
from principal import valida_fuentes_web
from principal import valida_fuentes_pdf
from principal import proceso_xml_individual

# Asignación de variables
print (os.path.dirname(os.path.abspath(__file__)))
rutas_base = procesos_comunes.genera_rutas_trabajo()
rootDir = rutas_base['ruta_base']
rootDirAuditoria = rutas_base['ruta_auditoria']
rootLog = rutas_base['ruta_logs']
fichero_log = os.path.join(rootLog, 'EMR_log.log')
print("Fichero log en ", fichero_log)

# Configura log
logging.basicConfig(level=logging.DEBUG
                    , filename=fichero_log, filemode='w', format='%(asctime)s - %(levelname)s - %(message)s')
resumen = pd.DataFrame(columns=('Etapa_Validacion', 'Resultado', 'Fecha'))

try:
    logging.debug('Comienza el programa')
    fichero_auditable = procesos_comunes.obtiene_fichero_auditable(rootDirAuditoria)
    nameFile = os.path.splitext(fichero_auditable)[0]
    rutas_trabajo = procesos_comunes.prepara_carpetas_trabajo(rootDirAuditoria)
except Exception as e:
    logging.debug('Se ha producido un error obteniendo el entorno de ejecución')
    logging.debug(e)
    exit()

try:
    logging.debug('Inicia: Descomprimir ficheros')
    r = lee_directorio.descomprime_todos_ficheros(rutas_trabajo['ruta_auditoria_carpeta_trabajo'], rutas_base['ruta_ficheros_respaldo'])
    resumen = resumen.append(r, ignore_index=True)
    logging.debug('Finaliza: Descomprimir ficheros')
except Exception as e:
    logging.debug('Se ha producido un error descomprimiento los ficheros')
    logging.debug(e)
    exit()

try:
    logging.debug('Inicia: Audita estructura de ficheros')
    r = audita_comprimidos.audita_principal()
    resumen = resumen.append(r, ignore_index=True)
    logging.debug('Finaliza: Finaliza estructura de ficheros')
except Exception as e:
    r = procesos_comunes.estructura_respuesta_error('Proceso de revisión de estructura de ficheros')
    resumen = resumen.append(r, ignore_index=True)
    logging.debug('Se ha producido un error Proceso de revisión de estructura de ficheros')
    logging.debug(e)

try:
    logging.debug('Inicia: Compara XMLs')
    r = compara_xml.compara_xml_principal(rutas_trabajo['ruta_auditoria_carpeta_trabajo'], rutas_trabajo['ruta_auditoria_carpeta_reporte'], nameFile)
    resumen = resumen.append(r, ignore_index=True)
    logging.debug('Finaliza: Compara XMLs')
except Exception as e:
    r = procesos_comunes.estructura_respuesta_error('Proceso de comparación entre XML')
    resumen = resumen.append(r, ignore_index=True)
    logging.debug('Se ha producido un error Proceso de comparación entre XML')
    logging.debug(e)

try:
    logging.debug('Inicia: Validación de cada XML')
    r = proceso_xml_individual.principal(rutas_trabajo['ruta_auditoria_carpeta_trabajo'], rutas_trabajo['ruta_auditoria_carpeta_reporte'], nameFile, rutas_base['ruta_ficheros_respaldo'])
    resumen = resumen.append(r, ignore_index=True)
    logging.debug('Finaliza: Validación de cada XML')
except Exception as e:
    r = procesos_comunes.estructura_respuesta_error('Proceso de validación de XML individual')
    resumen = resumen.append(r, ignore_index=True)
    logging.debug('Se ha producido un error Proceso de validación de XML individual')
    logging.debug(e)
    print(e)

try:
    logging.debug('Inicia: Proceso de revisión de valores entre etiquetas XML')
    r = valida_xml_entre.principal()
    resumen = resumen.append(r, ignore_index=True)
    logging.debug('Finaliza: Proceso de revisión de valores entre etiquetas XML')
except Exception as e:
    r = procesos_comunes.estructura_respuesta_error('Proceso de validación de XML grupal')
    resumen = resumen.append(r, ignore_index=True)
    logging.debug('Se ha producido un error Proceso de validación de XML grupal')
    logging.debug(e)

try:
    logging.debug('Inicia: Proceso de validación INE y Base de Datos')
    r = valida_ine_bd.principal()
    resumen = resumen.append(r, ignore_index=True)
    logging.debug('Finaliza: Proceso de validación INE y Base de Datos')
except Exception as e:
    r = procesos_comunes.estructura_respuesta_error('Proceso de validación contra INE y Base de Datos')
    resumen = resumen.append(r, ignore_index=True)
    logging.debug('Se ha producido un error Proceso de validación contra INE y Base de Datos')
    logging.debug(e)

try:
    logging.debug('Inicia: Proceso de validación con fuentes web')
    r = valida_fuentes_web.principal(rutas_trabajo['ruta_auditoria_carpeta_trabajo'], rutas_base['ruta_ficheros_respaldo'])
    resumen = resumen.append(r, ignore_index=True)
    logging.debug('Finaliza: Proceso de validación con fuentes web')
except Exception as e:
    r = procesos_comunes.estructura_respuesta_error('Proceso de validación contra fuentes web')
    resumen = resumen.append(r, ignore_index=True)
    logging.debug('Se ha producido un error Proceso de validación contra fuentes web')
    logging.debug(e)

try:
    logging.debug('Inicia: Proceso de validación con fuentes PDF')
    r = valida_fuentes_pdf.principal()
    resumen = resumen.append(r, ignore_index=True)
    logging.debug('Finaliza: Proceso de validación con fuentes PDF')
except Exception as e:
    r = procesos_comunes.estructura_respuesta_error('Proceso de validación contra fuentes PDF')
    resumen = resumen.append(r, ignore_index=True)
    logging.debug('Se ha producido un error Proceso de validación contra fuentes PDF')
    logging.debug(e)

# Genera resumen
writer = pd.ExcelWriter(os.path.join(rutas_trabajo['ruta_auditoria_carpeta_reporte'],  nameFile+'_Resumen.xlsx'))
resumen.to_excel(writer, 'sheet1')
writer.save()


