import datetime

def principal():
    # Retorna resultado del proceso
    r = dict()
    r['Etapa_Validacion'] = 'Proceso de validación de XML grupal'
    r['Resultado'] = 'Pendiente'
    r['Fecha'] = datetime.datetime.now()
    return r