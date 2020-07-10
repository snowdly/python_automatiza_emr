import datetime

def principal():
    # Retorna resultado del proceso
    r = dict()
    r['Etapa_Validacion'] = 'Proceso de validación contra INE y Base de Datos'
    r['Resultado'] = 'Pendiente'
    r['Fecha'] = datetime.datetime.now()
    return r