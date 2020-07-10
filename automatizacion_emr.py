import logging
import os
import pandas as pd
from principal import procesos_comunes
from principal import audita_comprimidos
from principal import lee_directorio
from principal import compara_xml
from principal import valida_xml_individual
from principal import valida_xml_entre
from principal import valida_ine_bd
from principal import valida_fuentes_web
from principal import valida_fuentes_pdf
from principal import proceso_xml_individual

rootDir = 'D:/EMR_Auditorias_Python/'
rootDirAuditoria = os.path.join(rootDir, 'Auditorias/')
rootDirResultados = 'D:/EMR_Auditorias_Python/Auditorias/Resultado/Reporte_Estado_Auditoria/'
rootLog = os.path.join(rootDir, 'Logs/')
fichero_log = os.path.join(rootLog, 'EMR_log.log')
print("Fichero log en ", fichero_log)


# Configura log
logging.basicConfig(level=logging.DEBUG
                    , filename=fichero_log, filemode='w', format='%(asctime)s - %(levelname)s - %(message)s')
resumen = pd.DataFrame(columns=('Etapa_Validacion', 'Resultado', 'Fecha'))


logging.debug('Comienza el programa')
fichero_auditable = procesos_comunes.obtiene_fichero_auditable(rootDirAuditoria)
nameFile = os.path.splitext(fichero_auditable)[0]
rutas_trabajo = procesos_comunes.prepara_carpetas_trabajo(rootDirAuditoria)



logging.debug('Inicia: Audita estructura de ficheros')
r = audita_comprimidos.audita_principal()
resumen = resumen.append(r, ignore_index=True)
logging.debug('Finaliza: Finaliza estructura de ficheros')


logging.debug('Inicia: Descomprimir ficheros')
r = lee_directorio.descomprime_todos_ficheros(rutas_trabajo['ruta_auditoria_carpeta_trabajo'])
resumen = resumen.append(r, ignore_index=True)
logging.debug('Finaliza: Descomprimir ficheros')


logging.debug('Inicia: Compara XMLs')
r = compara_xml.compara_xml_principal(rutas_trabajo['ruta_auditoria_carpeta_trabajo'], rutas_trabajo['ruta_auditoria_carpeta_reporte'], nameFile)
resumen = resumen.append(r, ignore_index=True)
logging.debug('Finaliza: Compara XMLs')


logging.debug('Inicia: Validación de cada XML')
#r = valida_xml_individual.principal(rutas_trabajo['ruta_auditoria_carpeta_trabajo'], rutas_trabajo['ruta_auditoria_carpeta_reporte'], nameZip=nameFile )
r = proceso_xml_individual.principal(rutas_trabajo['ruta_auditoria_carpeta_trabajo'], rutas_trabajo['ruta_auditoria_carpeta_reporte'], nameFile)
resumen = resumen.append(r, ignore_index=True)
logging.debug('Finaliza: Validación de cada XML')

logging.debug('Inicia: Proceso de revisión de valores entre etiquetas XML')
r = valida_xml_entre.principal()
resumen = resumen.append(r, ignore_index=True)
logging.debug('Finaliza: Proceso de revisión de valores entre etiquetas XML')

logging.debug('Inicia: Proceso de validación INE y Base de Datos')
r = valida_ine_bd.principal()
resumen = resumen.append(r, ignore_index=True)
logging.debug('Finaliza: Proceso de validación INE y Base de Datos')

logging.debug('Inicia: Proceso de validación con fuentes web')
r = valida_fuentes_web.principal()
resumen = resumen.append(r, ignore_index=True)
logging.debug('Finaliza: Proceso de validación con fuentes web')

logging.debug('Inicia: Proceso de validación con fuentes PDF')
r = valida_fuentes_pdf.principal()
resumen = resumen.append(r, ignore_index=True)
logging.debug('Finaliza: Proceso de validación con fuentes PDF')


# Genera resumen
writer = pd.ExcelWriter(os.path.join(rutas_trabajo['ruta_auditoria_carpeta_reporte'],  nameFile+'_Resumen.xlsx'))
resumen.to_excel(writer, 'sheet1')
writer.save()


