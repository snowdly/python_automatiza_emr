import re
import datetime
from principal import procesos_comunes
from principal import listas_comunes
import os


def reglas_validacion_individual(etiqueta, regla, vdato, fichero, ficheros_respaldo, carpeta_trabajo, pdf_texto, fichero_texto_cap, fichero_tecnico, datos_pdf_tecnico):
    fichero_nombre, fichero_extension = os.path.splitext(os.path.basename(fichero))
    d = dict()
    V = []
    fichero_nombre_dividido = fichero_nombre.split('_')
    if regla == 'R_Datos_Certificacion_Tipo_Certificacion':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        if vdato != "A":
            d['OK_KO'] = "KO"
            V.append('Valor debe ser igual a A')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        d['Comparacion'] = "Se compara con el parámetro Tipo_Certificacion del documento XML"
        return d
    elif regla == 'R_Datos_Certificacion_Tipo_Solicitud':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        if not re.match("ALT|MOD", vdato):
            d['OK_KO'] = "KO"
            V.append('Valor debe ser igual a ALT ó MOD')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        d['Comparacion'] = "Se compara con el parámetro Tipo_Solicitud del documento XML"
        return d
    elif regla == 'R_Datos_Certificacion_Titular_Nombre_Razon_Social':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        if not re.match("AMENA|ORANGE", vdato):
            d['OK_KO'] = "KO"
            V.append('Valor debe ser igual a AMENA ó ORANGE')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        d['Comparacion'] = "Se compara con el parámetro Titular_Nombre_Razon_Social del documento XML"
        return d
    elif regla == 'R_Datos_Certificacion_Expediente_Concesional':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')

        try:
            # print(fichero_nombre_dividido[0][3])
            for letra in listas_comunes.expediente_concesional:
                if letra['LETRA'] == fichero_nombre_dividido[0][3]:
                    if vdato != letra['EXPEDIENTE']:
                        d['OK_KO'] = "KO"
                        V.append('Valor debe ser igual a valores de tabla entregada')
        except:
            d['OK_KO'] = "KO"
            V.append('Valor debe ser igual a valores de tabla entregada')

        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        d['Comparacion'] = "Se compara con el parámetro Expediente_Concesional del documento XML"
        return d
    elif regla == 'R_Datos_Certificacion_Datos_Visado_Numero_Visado':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        d['Comparacion'] = "Se compara con el parámetro Numero_Visado del documento XML"
        return d
    elif regla == 'R_Datos_Certificacion_Datos_Visado_Fecha_Visado':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        d['Comparacion'] = "Se compara con el parámetro Numero_Visado del documento XML"
        return d
    elif regla == 'R_Datos_Certificacion_Datos_Visado_Numero_Colegiado':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        d['Comparacion'] = "Se compara con el parámetro Numero_Colegiado del documento XML"
        return d
    elif regla == 'R_Datos_Certificacion_Datos_Visado_Colegio_Profesional':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        if not re.match("COITT|COIT", vdato):
            d['OK_KO'] = "KO"
            V.append('Valor debe ser igual a COITT ó COIT')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        d['Comparacion'] = "Se compara con el parámetro Colegio_Profesional del documento XML"
        return d
    elif regla == 'R_Datos_Certificacion_Tecnico_Competente_NIF_NIE':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        if not re.match("((([X-Z])|([LM])){1}([-]?)((\d){7})([-]?)([A-Z]{1}))|((\d{8})([-]?)([A-Z]))", vdato):
            d['OK_KO'] = "KO"
            V.append('DNI o NIE no tiene el formato correcto')
        #r_datos_pdf = procesos_comunes.compara_tecnico_competente_pdf(vdato,
        #                                                              '' if datos_pdf_tecnico['Texto'] is None else
        #                                                              datos_pdf_tecnico['Texto'],
        #                                                              '' if datos_pdf_tecnico['Fichero'] is None else
        #                                                              datos_pdf_tecnico['Fichero'])
        if datos_pdf_tecnico == '':
            d['OK_KO'] = "KO"
            V.append('No se ha encontrado fichero de Declaración de Responsable , o no ha sido posible leerlo. La revisión debe ser Visual')
        else:
            intll = procesos_comunes.busca_datos_pdf_texto(vdato, datos_pdf_tecnico)
            if not (len(intll['ListaEncontrados']) >= 1):
                d['OK_KO'] = "KO"
                V.append('DNI o NIE no coincide con el fichero de Declaración de Responsable')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        d['Comparacion'] = "Se compara con el documento PDF Declaración Responsable de Técnico competente"
        return d
    elif regla == 'R_Datos_Certificacion_Tecnico_Competente_Nombre':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        if not re.match(
                "^[a-zA-ZàáâäãåąčćęèéêëėįìíîïłńòóôöõøùúûüųūÿýżźñçčšžÀÁÂÄÃÅĄĆČĖĘÈÉÊËÌÍÎÏĮŁŃÒÓÔÖÕØÙÚÛÜŲŪŸÝŻŹÑßÇŒÆČŠŽ∂ð '-]+$",
                vdato):
            d['OK_KO'] = "KO"
            V.append('Nombre no tiene el formato correcto')
        '''
        r_datos_pdf = procesos_comunes.compara_tecnico_competente_pdf(vdato,
                                                                      '' if datos_pdf_tecnico['Texto'] is None else
                                                                      datos_pdf_tecnico['Texto'],
                                                                      '' if datos_pdf_tecnico['Fichero'] is None else
                                                                      datos_pdf_tecnico['Fichero'])
        if r_datos_pdf['OK_KO'] == 'KO':
            d['OK_KO'] = "KO"
        V.append(r_datos_pdf['Error'])
        '''
        if datos_pdf_tecnico == '':
            d['OK_KO'] = "KO"
            V.append('No se ha encontrado fichero de Declaración de Responsable , o no ha sido posible leerlo. La revisión debe ser Visual')
        else:
            intll = procesos_comunes.busca_datos_pdf_texto(vdato, datos_pdf_tecnico)
            if not (len(intll['ListaEncontrados']) >= 1):
                d['OK_KO'] = "KO"
                V.append('Nombre del técnico no coincide con el fichero de Declaración de Responsable')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        d['Comparacion'] = "Se compara con el documento PDF Declaración Responsable de Técnico competente"
        return d
    elif regla == 'R_Datos_Certificacion_Tecnico_Competente_Apellido1':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        if not re.match(
                "^[a-zA-ZàáâäãåąčćęèéêëėįìíîïłńòóôöõøùúûüųūÿýżźñçčšžÀÁÂÄÃÅĄĆČĖĘÈÉÊËÌÍÎÏĮŁŃÒÓÔÖÕØÙÚÛÜŲŪŸÝŻŹÑßÇŒÆČŠŽ∂ð '-]+$",
                vdato):
            d['OK_KO'] = "KO"
            V.append('Apellido no tiene el formato correcto')
        '''
        r_datos_pdf = procesos_comunes.compara_tecnico_competente_pdf(vdato,
                                                                      '' if datos_pdf_tecnico['Texto'] is None else
                                                                      datos_pdf_tecnico['Texto'],
                                                                      '' if datos_pdf_tecnico['Fichero'] is None else
                                                                      datos_pdf_tecnico['Fichero'])
        if r_datos_pdf['OK_KO'] == 'KO':
            d['OK_KO'] = "KO"
        V.append(r_datos_pdf['Error'])
        '''
        if datos_pdf_tecnico == '':
            d['OK_KO'] = "KO"
            V.append('No se ha encontrado fichero de Declaración de Responsable , o no ha sido posible leerlo. La revisión debe ser Visual')
        else:
            intll = procesos_comunes.busca_datos_pdf_texto(vdato, datos_pdf_tecnico)
            if not (len(intll['ListaEncontrados']) >= 1):
                d['OK_KO'] = "KO"
                V.append('Primer Apellido del técnico no coincide con el fichero de Declaración de Responsable')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        d['Comparacion'] = "Se compara con el documento PDF Declaración Responsable de Técnico competente"
        return d
    elif regla == 'R_Datos_Certificacion_Tecnico_Competente_Apellido2':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        if not re.match(
                "^[a-zA-ZàáâäãåąčćęèéêëėįìíîïłńòóôöõøùúûüųūÿýżźñçčšžÀÁÂÄÃÅĄĆČĖĘÈÉÊËÌÍÎÏĮŁŃÒÓÔÖÕØÙÚÛÜŲŪŸÝŻŹÑßÇŒÆČŠŽ∂ð '-]+$",
                vdato):
            d['OK_KO'] = "KO"
            V.append('Apellido no tiene el formato correcto')
        '''
        r_datos_pdf = procesos_comunes.compara_tecnico_competente_pdf(vdato,
                                                                      '' if datos_pdf_tecnico['Texto'] is None else
                                                                      datos_pdf_tecnico['Texto'],
                                                                      '' if datos_pdf_tecnico['Fichero'] is None else
                                                                      datos_pdf_tecnico['Fichero'])
        if r_datos_pdf['OK_KO'] == 'KO':
            d['OK_KO'] = "KO"
        V.append(r_datos_pdf['Error'])
        '''
        if datos_pdf_tecnico == '':
            d['OK_KO'] = "KO"
            V.append('No se ha encontrado fichero de Declaración de Responsable , o no ha sido posible leerlo. La revisión debe ser Visual')
        else:
            intll = procesos_comunes.busca_datos_pdf_texto(vdato, datos_pdf_tecnico)
            if not (len(intll['ListaEncontrados']) >= 1):
                d['OK_KO'] = "KO"
                V.append('Segundo Apellido del técnico no coincide con el fichero de Declaración de Responsable')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        d['Comparacion'] = "Se compara con el documento PDF Declaración Responsable de Técnico competente"
        return d
    elif regla == 'R_Estacion_Certificada_Datos_Emplazamiento_Codigo_Emplazamiento':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        if fichero_tecnico == '':
            d['OK_KO'] = 'KO'
            V.append('No existe fichero Técnico o no puede ser leido: ' + fichero_nombre + '.pdf' + '  La revisión debe ser VISUAL')
        else:
            intll = procesos_comunes.busca_datos_pdf_texto(vdato, fichero_tecnico)
            if len(intll['ListaEncontrados']) > 1:
                d['OK_KO'] = 'OK'
            else:
                d['OK_KO'] = 'KO/VISUAL'
                V.append('Valor no coincide con información del documento Técnico. Realizar validación VISUAL')

        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        d['Comparacion'] = "Se compara con Documento Técnico"
        return d
    elif regla == 'R_Estacion_Certificada_Datos_Emplazamiento_Emplazamiento_Compartido':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        if not re.match("SI|NO", vdato):
            d['OK_KO'] = "KO"
            V.append('Valor debe ser igual a SI ó NO')
        #VALIDACION IA
        datoreg=''
        valor_tipo_sistema = procesos_comunes.valor_elemento_xml(fichero,
                                                                 './/Estacion_Certificada/Datos_Estacion/Tipo_Sistema')
        for tecnologia in listas_comunes.tabla_tecnologias:
            if tecnologia['TECNOLOGIA'] == valor_tipo_sistema['Valor'].upper():
                datoreg = tecnologia['OTRAS']
                break
        if fichero_texto_cap== '':
            d['OK_KO'] = "KO"
            V.append('No se ha encontrado fichero CAP, o no ha sido posible leerlo')
        else:
            intll = procesos_comunes.busca_datos_pdf_texto(datoreg,  fichero_texto_cap)
            otras_tecnologias = 'SI' if len(intll['ListaEncontrados']) > 1 else 'NO'
            if vdato.upper() != otras_tecnologias.upper():
                d['OK_KO'] = 'KO/VISUAL'
                V.append('Valor no coincide con información del documento CAP. Realizar validación VISUAL')
        #V.append('Para la presente etapa, la validación debe ser visual')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        d['Comparacion'] = "Se compara con información del documento CAP"
        return d
    elif regla == 'R_Estacion_Certificada_Datos_Emplazamiento_Cod_INE_Termino_Municipal':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        cod_provincia = procesos_comunes.valor_elemento_xml(fichero,
                                                            './/Estacion_Certificada/Datos_Emplazamiento/Cod_INE_Provincia')
        Poblacion = \
            procesos_comunes.valor_elemento_xml(fichero, './/Estacion_Certificada/Datos_Emplazamiento/Calle/Poblacion')[
                'Valor']
        r = procesos_comunes.obtiene_datos_ine_p(fichero, vdato, cod_provincia['Valor'], Poblacion, ficheros_respaldo)
        if r['Cod_Municipio_Ine'] != vdato:
            d['OK_KO'] = 'KO'
            V.append('El valor no coincide con la tabla de datos del INE')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        d['Comparacion'] = "Se compara con el Término Municipal del documento Excel de Códigos INE"
        return d
    elif regla == 'R_Estacion_Certificada_Datos_Emplazamiento_Cod_INE_Provincia':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        cod_municipio = procesos_comunes.valor_elemento_xml(fichero,
                                                            './/Estacion_Certificada/Datos_Emplazamiento/Cod_INE_Termino_Municipal')
        Poblacion = \
            procesos_comunes.valor_elemento_xml(fichero, './/Estacion_Certificada/Datos_Emplazamiento/Calle/Poblacion')[
                'Valor']
        r = procesos_comunes.obtiene_datos_ine_p(fichero, cod_municipio['Valor'], vdato, Poblacion, ficheros_respaldo)
        if r['Cod_Provincia_INE'] != vdato:
            d['OK_KO'] = 'KO'
            V.append('El valor no coincide con la tabla de datos del INE')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        d['Comparacion'] = "Se compara con el Cod_INE_Provincia del documento Excel de Códigos INE"
        return d
    elif regla == 'R_Estacion_Certificada_Datos_Emplazamiento_Latitud':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')

        # VALIDACION IA
        datoreg = 'LATITUD(\W)*' + vdato
        if fichero_tecnico == '':
            d['OK_KO'] = 'KO'
            V.append('No existe fichero Técnico o no puede ser leido: ' + fichero_nombre + '.pdf' + '  La revisión debe ser VISUAL')
        else:
            intll = procesos_comunes.busca_datos_pdf_texto(datoreg, fichero_tecnico)
            if len(intll['ListaEncontrados']) >= 1:
                d['OK_KO'] = 'OK'
            else:
                d['OK_KO'] = 'KO/VISUAL'
                V.append('Valor no coincide con información del documento Técnico. Realizar validación VISUAL')

        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        d['Comparacion'] = "Se compara con información obtenida de la página web de Infoantenas"
        return d
    elif regla == 'R_Estacion_Certificada_Datos_Emplazamiento_Longitud':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')

        # VALIDACION IA
        datoreg = 'LONGITUD(\W)*' + vdato
        if fichero_tecnico == '':
            d['OK_KO'] = 'KO'
            V.append('No existe fichero Técnico o no puede ser leido: ' + fichero_nombre + '.pdf' + '  La revisión debe ser VISUAL')
        else:
            intll = procesos_comunes.busca_datos_pdf_texto(datoreg, fichero_tecnico)
            if len(intll['ListaEncontrados']) >= 1:
                d['OK_KO'] = 'OK'
            else:
                d['OK_KO'] = 'KO/VISUAL'
                V.append('Valor no coincide con información del documento Técnico. Realizar validación VISUAL')

        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        d['Comparacion'] = "Se compara con información obtenida de la página web de Infoantenas"
        return d
    elif regla == 'R_Estacion_Certificada_Datos_Emplazamiento_Datum':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        if not re.match("ETRS89|REGCAN95|WGS84", vdato):
            d['OK_KO'] = 'KO'
            V.append('Los valores permitidos en Datum: ETRS89 ó REGCAN95 ó WGS84')
        codigo_emplazamiento = procesos_comunes.valor_elemento_xml(fichero,
                                                                   './/Estacion_Certificada/Datos_Emplazamiento/Datum')['Valor']
        if len(codigo_emplazamiento) >= 3:
            inicial = codigo_emplazamiento[0:3]
        else:
            inicial = ''
        if inicial == 'CAN':
            if not re.match("REGCAN95|WGS84", vdato):
                d['OK_KO'] = 'KO'
                V.append('Canarias debe tener datum REGCAN95 ó WGS84')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        d['Comparacion'] = "Se compara con el parámetro Datum del documento XML"
        return d
    elif regla == 'R_Estacion_Certificada_Datos_Emplazamiento_Referencia_Catastral':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        '''
        if len(vdato.strip()) < 20:
            d['OK_KO'] = 'OK'
            V.append('Datos no coinciden, revisar visualmente en web')
        '''
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        d['Comparacion'] = "Se compara con el dato recogido de la página web de sede catastro"
        return d
    elif regla == 'R_Estacion_Certificada_Datos_Emplazamiento_Cota_Terreno_Sobre_Nivel_Mar':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'VISUAL'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        V.append('Para la presente etapa, la validación debe ser visual')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        d['Comparacion'] = "Se compara con el valor de la página web de iberpix"
        return d
    elif regla == 'R_Estacion_Certificada_Datos_Emplazamiento_Calle_Poblacion':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        RC = procesos_comunes.valor_elemento_xml(fichero,
                                                 './/Estacion_Certificada/Datos_Emplazamiento/Referencia_Catastral')[
            'Valor']
        r_api_catastro = procesos_comunes.consulta_api_catastro(RC)
        if r_api_catastro['OK_KO'] == 'OK':
            if str(r_api_catastro['nombre_municipio']).strip().upper() != str(vdato).strip().upper():
                d['OK_KO'] = 'KO/VISUAL'
                V.append('Datos no coinciden, revisar visualmente en web')
        else:
            d['OK_KO'] = 'KO/VISUAL'
            V.append(r_api_catastro['ERROR'])
        '''        
        cod_municipio = procesos_comunes.valor_elemento_xml(fichero,
                                                            './/Estacion_Certificada/Datos_Emplazamiento/Cod_INE_Termino_Municipal')
        cod_provincia = procesos_comunes.valor_elemento_xml(fichero, './/Estacion_Certificada/Datos_Emplazamiento/Cod_INE_Provincia')
        r = procesos_comunes.obtiene_datos_ine(fichero, cod_municipio['Valor'], cod_provincia['Valor'], ficheros_respaldo)
        if r['Nombre_Municipio_Catastro'].strip().upper() != str(vdato).strip().upper():
            d['OK_KO'] = 'KO'
            V.append('El valor no coincide con la tabla de datos del INE')
        '''
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        d['Comparacion'] = "Se compara con el dato recogido de la página web de sede catastro"
        return d
    elif regla == 'R_Estacion_Certificada_Datos_Emplazamiento_Calle_Tipo_Via':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        RC = procesos_comunes.valor_elemento_xml(fichero,
                                                 './/Estacion_Certificada/Datos_Emplazamiento/Referencia_Catastral')[
            'Valor']
        r_api_catastro = procesos_comunes.consulta_api_catastro(RC)
        if r_api_catastro['OK_KO'] == 'OK':
            if str(r_api_catastro['tipo_via']).strip().upper() != str(vdato).strip().upper():
                d['OK_KO'] = 'KO/VISUAL'
                V.append('Datos no coinciden, revisar visualmente en web')
        else:
            d['OK_KO'] = 'KO/VISUAL'
            V.append(r_api_catastro['ERROR'])
        '''
        if not re.match("AV|BU|CL|CM|CR|GL|PJ|PS|PZ|RB|RD|TR|VP", vdato):
            d['OK_KO'] = "KO"
            V.append('Valor debe ser igual a AV|BU|CL|CM|CR|GL|PJ|PS|PZ|RB|RD|TR|VP')
        '''
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        d['Comparacion'] = "Se compara con el dato recogido de la página web de sede catastro"
        return d
    elif regla == 'R_Estacion_Certificada_Datos_Emplazamiento_Calle_Nombre_Via':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        RC = procesos_comunes.valor_elemento_xml(fichero,
                                                 './/Estacion_Certificada/Datos_Emplazamiento/Referencia_Catastral')[
            'Valor']
        r_api_catastro = procesos_comunes.consulta_api_catastro(RC)
        if r_api_catastro['OK_KO'] == 'OK':
            if str(r_api_catastro['nombre_via']).strip().upper() != str(vdato).strip().upper():
                d['OK_KO'] = 'KO/VISUAL'
                V.append('Datos no coinciden, revisar visualmente en web')
        else:
            d['OK_KO'] = 'KO/VISUAL'
            V.append(r_api_catastro['ERROR'])
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        d['Comparacion'] = "Se compara con el dato recogido de la página web de sede catastro"
        return d
    elif regla == 'R_Estacion_Certificada_Datos_Emplazamiento_Calle_Numero_Portal':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        RC = procesos_comunes.valor_elemento_xml(fichero,
                                                 './/Estacion_Certificada/Datos_Emplazamiento/Referencia_Catastral')[
            'Valor']
        r_api_catastro = procesos_comunes.consulta_api_catastro(RC)
        if r_api_catastro['OK_KO'] == 'OK':
            if str(r_api_catastro['numero_portal']).strip().upper() != str(vdato).strip().upper():
                d['OK_KO'] = 'KO/VISUAL'
                V.append('Datos no coinciden, revisar visualmente en web')
        else:
            d['OK_KO'] = 'KO/VISUAL'
            V.append(r_api_catastro['ERROR'])
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        d['Comparacion'] = "Datos no coinciden, revisar visualmente en web"
        return d
    elif regla == 'R_Estacion_Certificada_Datos_Emplazamiento_Calle_Situacion':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        d['Comparacion'] = "Dato no obligatorio, se utiliza para especificar aún con mas detalle la ubicación de la BTS"
        return d
    elif regla == 'R_Estacion_Certificada_Datos_Estacion_Codigo_Estacion':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        codigo_emplazamiento = procesos_comunes.valor_elemento_xml(fichero, './/Estacion_Certificada/Datos_Estacion'
                                                                            '/Codigo_Estacion')['Valor']

        lr = procesos_comunes.obtine_letra_expediente_concesional(fichero)
        if lr['OK_KO'] == 'OK':
            codigo_cambiado = codigo_emplazamiento[0:3] + lr['Letra'] + codigo_emplazamiento[4:]
            if vdato != codigo_cambiado:
                d['OK_KO'] = 'KO'
                V.append(
                    'Debe tener el mismo código que el parámetro codigo emplazamiento salvo la letra que ocupa el 4 '
                    'lugar, en vez de una R debe ser la letra correspondiente a la tecnología del certificado '
                    'radioeléctrico.')
        else:
            d['OK_KO'] = 'KO'
            V.append(
                'No ha sido posible verificar la letra del expediente consecional, revise si el nombre del xml es correcto')

        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        d['Comparacion'] = "Se obtiene del título del documento xml"
        return d
    elif regla == 'R_Estacion_Certificada_Datos_Estacion_Tipo_Sistema':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        if not re.match("UMTS|GSM|DCS|RB|LTE|WIMAX|LMDS3.5", vdato):
            d['OK_KO'] = "KO"
            V.append('Valores UMTS|GSM|DCS|RB|LTE|WIMAX|LMDS3.5')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        d['Comparacion'] = "Se obtiene del valor Tipo_Sistema del documento xml "
        return d
    elif regla == 'R_Estacion_Certificada_Datos_Estacion_Tipo_Estacion':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK/VISUAL'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        if not re.match("ER1|ER2|ER3|ER4|ER5", vdato):
            d['OK_KO'] = "KO"
            V.append('Valor debe ser igual a ER1|ER2|ER3|ER4|ER5')
        V.append('Dato con coherencia, pendiente validarse visualmente')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        #d['Comparacion'] = "Se obtiene del valor Tipo_Sistema del documento xml "
        return d
    elif regla == 'R_Estacion_Certificada_Datos_Estacion_Entorno_Sensible':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        if not re.match("SI|NO", vdato):
            d['OK_KO'] = "KO"
            V.append('Valor debe ser igual a SI|NO')
        c = procesos_comunes.cantidad_elementos_xml(fichero,
                                                    './/Informe_Medidas/Puntos_Medida/Punto_Medida/Punto_Sensible/Situacion')[
            'Cantidad']
        if c == 0:
            if vdato != 'NO':
                d['OK_KO'] = "KO"
                V.append(
                    'El valor indica que NO existe entorno sensible, sin embargo SI existen datos para .//Informe_Medidas/Puntos_Medida/Punto_Medida/Punto_Sensible')
        else:
            if vdato != 'SI':
                d['OK_KO'] = "KO"
                V.append(
                    'El valor indica que SI existe entorno sensible, sin embargo NO existen datos para .//Informe_Medidas/Puntos_Medida/Punto_Medida/Punto_Sensible')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        d['Comparacion'] = "Se obtiene del valor Entorno Sensible del documento xml"
        return d

    elif regla == 'R_Estacion_Certificada_Datos_Estacion_Num_Sectores_Interiores':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK/VISUAL'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        sector_interior = procesos_comunes.valor_elemento_xml(fichero,
                                                              './/Estacion_Certificada/Datos_Estacion/Num_Sectores_Interiores')[
            'Valor']
        sector_exterior = procesos_comunes.valor_elemento_xml(fichero,
                                                              './/Estacion_Certificada/Datos_Estacion/Num_Sectores_Exteriores')[
            'Valor']
        sectores = procesos_comunes.cantidad_elementos_xml(fichero,
                                                           './/Estacion_Certificada/Datos_Estacion/Sectores/Sector/Tipo_Potencia_Radiada')[
            'Cantidad']

        if sectores != (int(sector_interior) + int(sector_exterior)):
            d['OK_KO'] = "KO"
            V.append(
                'El valor de Num_Sectores_Interiores más Num_Sectores_Exteriores, es diferente a la cantidad de Sectores')
        V.append('Dato con coherencia, pendiente validarse visualmente')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        return d
    elif regla == 'R_Estacion_Certificada_Datos_Estacion_Num_Sectores_Exteriores':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK/VISUAL'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        sector_interior = procesos_comunes.valor_elemento_xml(fichero,
                                                              './/Estacion_Certificada/Datos_Estacion/Num_Sectores_Interiores')[
            'Valor']
        sector_exterior = procesos_comunes.valor_elemento_xml(fichero,
                                                              './/Estacion_Certificada/Datos_Estacion/Num_Sectores_Exteriores')[
            'Valor']
        sectores = procesos_comunes.cantidad_elementos_xml(fichero,
                                                           './/Estacion_Certificada/Datos_Estacion/Sectores/Sector/Tipo_Potencia_Radiada')[
            'Cantidad']

        if sectores != (int(sector_interior) + int(sector_exterior)):
            d['OK_KO'] = "KO"
            V.append(
                'El valor de Num_Sectores_Interiores más Num_Sectores_Exteriores, es diferente a la cantidad de Sectores')
        V.append('Dato con coherencia, pendiente validarse visualmente')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        return d
    elif regla == 'R_Estacion_Certificada_Datos_Estacion_Sectores_Sector_Tipo_Potencia_Radiada':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        if not re.match("PIRE", vdato):
            d['OK_KO'] = "KO"
            V.append('Valor debe ser igual a PIRE')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        return d
    elif regla == 'R_Estacion_Certificada_Datos_Estacion_Sectores_Sector_Potencia_Maxima_Total':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        if not re.match("\d{1,}\.{0,1}\d{1,}", vdato):
            d['OK_KO'] = 'KO'
            V.append('Debe ser número')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        return d
    elif regla == 'R_Estacion_Certificada_Datos_Estacion_Sectores_Sector_Unidad_Potencia_Maxima_Total':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        if not re.match("W", vdato):
            d['OK_KO'] = "KO"
            V.append('Valor debe ser igual a W')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        return d
    elif regla == 'R_Estacion_Certificada_Datos_Estacion_Sectores_Sector_Localizacion_Antena':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'VISUAL'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        if not re.match("EXTERIOR|INTERIOR", vdato):
            d['OK_KO'] = "KO"
            V.append('Valor debe ser igual a EXTERIOR ó INTERIOR')
        V.append('Para la presente etapa, la validación debe ser visual')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        return d
    elif regla == 'R_Estacion_Certificada_Datos_Estacion_Sectores_Sector_Tipo_Antena':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'VISUAL'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        if not re.match("D|N", vdato):
            d['OK_KO'] = "KO"
            V.append('Valor debe ser igual a D ó N')
        V.append('Para la presente etapa, la validación debe ser visual')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        return d
    elif regla == 'R_Estacion_Certificada_Datos_Estacion_Sectores_Sector_Polarizacion':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        if not re.match("V|H|M|L|CR|CL", vdato):
            d['OK_KO'] = "KO"
            V.append('Valor debe ser igual a V|H|M|L|CR|CL')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        return d
    elif regla == 'R_Estacion_Certificada_Datos_Estacion_Sectores_Sector_Altura_Antena_Sobre_Terreno':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'VISUAL'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        V.append('Para la presente etapa, la validación debe ser visual')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        return d
    elif regla == 'R_Estacion_Certificada_Datos_Estacion_Sectores_Sector_Inclinacion_Haz_Sobre_Horizontal':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'VISUAL'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        V.append('Para la presente etapa, la validación debe ser visual')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        return d
    elif regla == 'R_Estacion_Certificada_Datos_Estacion_Sectores_Sector_Antena_Directiva_Tipo_Ganancia':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        if not re.match("ISO", vdato):
            d['OK_KO'] = "KO"
            V.append('Valor debe ser igual a ISO')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        return d
    elif regla == 'R_Estacion_Certificada_Datos_Estacion_Sectores_Sector_Antena_Directiva_Ganancia_Antena':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        return d
    elif regla == 'R_Estacion_Certificada_Datos_Estacion_Sectores_Sector_Antena_Directiva_Apertura_Horizontal_Haz':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'VISUAL'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        V.append('Para la presente etapa, la validación debe ser visual')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        return d
    elif regla == 'R_Estacion_Certificada_Datos_Estacion_Sectores_Sector_Antena_Directiva_Apertura_Vertical_Haz':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'VISUAL'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        V.append('Para la presente etapa, la validación debe ser visual')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        return d
    elif regla == 'R_Estacion_Certificada_Datos_Estacion_Sectores_Sector_Antena_Directiva_Acimut_Maxima_Radiacion':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'VISUAL'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        V.append('Para la presente etapa, la validación debe ser visual')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        return d
    elif regla == 'R_Estacion_Certificada_Datos_Estacion_Sectores_Sector_Antena_Directiva_Apertura_Horizontal_Haz':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        return d
    elif regla == 'R_Estacion_Certificada_Datos_Estacion_Sectores_Sector_Antena_Directiva_Nivel_Lobulos_Secundarios':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        return d
    elif regla == 'R_Estacion_Certificada_Datos_Estacion_Sectores_Sector_Volumen_Referencia_Forma_Volumen':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        if not re.match("ESFERA|CILINDRO|PARALELEPIPEDO|TOROIDE|OTRA", vdato):
            d['OK_KO'] = "KO"
            V.append('Valores ESFERA|CILINDRO|PARALELEPIPEDO|TOROIDE|OTRA')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        return d
    elif regla == 'R_Estacion_Certificada_Datos_Estacion_Sectores_Sector_Volumen_Referencia_Distancia_Referencia':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'VISUAL'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        V.append('Para la presente etapa, la validación debe ser visual')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        return d
    elif regla == 'R_Estacion_Certificada_Datos_Estacion_Sectores_Sector_Volumen_Referencia_Coeficiente_Reflexion':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'VISUAL'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        if not re.match('1|2.56|4', vdato):
            d['OK_KO'] = 'KO'
            V.append('Valor debe ser igual a 1 ó 2.56 ó 4')
        V.append('Para la presente etapa, la validación debe ser visual')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        return d
    elif regla == 'R_Informe_Medidas_Puntos_Medida_Punto_Medida_IdPunto':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        if float(vdato.replace(',', '.')) < 1:
            d['OK_KO'] = 'KO'
            V.append('Deben ser 5 o más puntos')
        c1 = procesos_comunes.cantidad_elementos_xml(fichero, './/Informe_Medidas/Puntos_Medida/Punto_Medida/IdPunto')
        if c1['Cantidad'] < 5:
            d['OK_KO'] = 'KO'
            V.append('Deben ser 5 o más puntos de medida')
        c2 = procesos_comunes.cantidad_elementos_xml(fichero, './/Informe_Medidas/Informe_Medidas_Fase1'
                                                              '/Medicion_Fase1/Medida_Fase1/IdPunto')
        if c1['Cantidad'] != c2['Cantidad']:
            d['OK_KO'] = 'KO'
            V.append('Cantidad de Puntos de Medida diferente a cantidad de Medidas')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()

        return d
    elif regla == 'R_Informe_Medidas_Puntos_Medida_Punto_Medida_Distancia':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK/VISUAL'
        d['Validacion'] = ''
        if not ((float(vdato.replace(',', '.')) >= 0) and (float(vdato.replace(',', '.')) <= 100)):
            d['OK_KO'] = 'KO'
            V.append('Puntos de Medida debe estar entre 0 y 100 metros')
        V.append('Dato con coherencia, pendiente validarse visualmente')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        return d
    elif regla == 'R_Informe_Medidas_Puntos_Medida_Punto_Medida_Acimut':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK/VISUAL'
        d['Validacion'] = ''
        if not ((float(vdato.replace(',', '.')) >= 0) and (float(vdato.replace(',', '.')) <= 359)):
            d['OK_KO'] = 'KO'
            V.append('Puntos de Medida debe estar entre 0 y 359 grados')
        V.append('Dato con coherencia, pendiente validarse visualmente')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        return d
    elif regla == 'R_Informe_Medidas_Puntos_Medida_Punto_Medida_Punto_Sensible_Situacion':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''

        # VALIDACION IA
        if fichero_tecnico == '':
            d['OK_KO'] = 'KO'
            V.append('No existe fichero Técnico o no puede ser leido: ' + fichero_nombre + '.pdf' + '  La revisión debe ser VISUAL')
        else:
            intll = procesos_comunes.busca_datos_pdf_texto(vdato.upper(), fichero_tecnico)
            if len(intll['ListaEncontrados']) >= 1:
                d['OK_KO'] = 'OK'
            else:
                d['OK_KO'] = 'KO/VISUAL'
                V.append('Valor no coincide con información del documento Técnico. Realizar validación VISUAL')

        #V.append('Para la presente etapa, la validación debe ser visual')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        return d
    elif regla == 'R_Informe_Medidas_Puntos_Medida_Punto_Medida_Punto_Sensible_Tipo_Espacio_Sensible':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        if not re.match('HS|ES|PP|RA', vdato):
            d['OK_KO'] = 'KO'
            V.append('Valores HS|ES|PP|RA')
        #VALIDACION IA
        nombrevia = procesos_comunes.valor_elemento_xml(fichero,
                                                            './/Informe_Medidas/Puntos_Medida/Punto_Medida/Punto_Sensible/Nombre_Via')

        if fichero_tecnico == '':
            d['OK_KO'] = 'KO'
            V.append('No existe fichero Técnico o no puede ser leido: ' + fichero_nombre + '.pdf' + '  La revisión debe ser VISUAL')
        else:
            intll = procesos_comunes.busca_datos_pdf_texto(nombrevia['Valor'].upper(), fichero_tecnico)
            if len(intll['ListaEncontrados']) >= 1:
                for encontrado in intll['ListaEncontrados']:
                    if encontrado.find(vdato.upper()) != -1:
                        d['OK_KO'] = "OK"
                        break
                    else:
                        d['OK_KO'] = "KO/VISUAL"
                        V.append('Valor no coincide con información del documento Técnico. Realizar validación VISUAL')
            else:
                d['OK_KO'] = 'KO/VISUAL'
                V.append('Valor no coincide con información del documento Técnico. Realizar validación VISUAL')

        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        return d
    elif regla == 'R_Informe_Medidas_Puntos_Medida_Punto_Medida_Punto_Sensible_Tipo_Via':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        if not re.match('AV|BU|CL|CM|CR|GL|PJ|PS|PZ|RB|RD|TR|VP', vdato):
            d['OK_KO'] = 'KO'
            V.append('Valores AV|BU|CL|CM|CR|GL|PJ|PS|PZ|RB|RD|TR|VP')

        # VALIDACION IA
        nombrevia = procesos_comunes.valor_elemento_xml(fichero,
                                                        './/Informe_Medidas/Puntos_Medida/Punto_Medida/Punto_Sensible/Nombre_Via')
        if fichero_tecnico == '':
            d['OK_KO'] = 'KO'
            V.append('No existe fichero Técnico o no puede ser leido: ' + fichero_nombre + '.pdf' + '  La revisión debe ser VISUAL')
        else:
            intll = procesos_comunes.busca_datos_pdf_texto(nombrevia['Valor'].upper(), fichero_tecnico)
            if len(intll['ListaEncontrados']) >= 1:
                for encontrado in intll['ListaEncontrados']:
                    if encontrado.find(vdato.upper()) != -1:
                        d['OK_KO'] = "OK"
                        break
                    else:
                        d['OK_KO'] = "KO/VISUAL"
                        V.append('Valor no coincide con información del documento Técnico. Realizar validación VISUAL')
            else:
                d['OK_KO'] = 'KO/VISUAL'
                V.append('Valor no coincide con información del documento Técnico. Realizar validación VISUAL')

        #V.append('Para la presente etapa, la validación debe ser visual')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        return d
    elif regla == 'R_Informe_Medidas_Puntos_Medida_Punto_Medida_Punto_Sensible_Nombre_Via':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        # VALIDACION IA
        if fichero_tecnico == '':
            d['OK_KO'] = 'KO'
            V.append('No existe fichero Técnico o no puede ser leido: ' + fichero_nombre + '.pdf' + '  La revisión debe ser VISUAL')
        else:
            intll = procesos_comunes.busca_datos_pdf_texto(vdato.upper(), fichero_tecnico)
            if len(intll['ListaEncontrados']) >= 1:
                d['OK_KO'] = 'OK'
            else:
                d['OK_KO'] = 'KO/VISUAL'
                V.append('Valor no coincide con información del documento Técnico. Realizar validación VISUAL')
        #V.append('Para la presente etapa, la validación debe ser visual')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        return d
    elif regla == 'R_Informe_Medidas_Puntos_Medida_Punto_Medida_Punto_Sensible_Numero_Portal':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        if not (vdato == 'S/N' or vdato.isdigit() or vdato == 'SN'):
            d['OK_KO'] = 'KO'
            V.append('Debe ser número o S/N')

        # VALIDACION IA
        nombrevia = procesos_comunes.valor_elemento_xml(fichero,
                                                        './/Informe_Medidas/Puntos_Medida/Punto_Medida/Punto_Sensible/Nombre_Via')
        if fichero_tecnico == '':
            d['OK_KO'] = 'KO'
            V.append('No existe fichero Técnico o no puede ser leido: ' + fichero_nombre + '.pdf' + '  La revisión debe ser VISUAL')
        else:
            intll = procesos_comunes.busca_datos_pdf_texto(nombrevia['Valor'].upper(), fichero_tecnico)
            if len(intll['ListaEncontrados']) >= 1:
                for encontrado in intll['ListaEncontrados']:
                    if encontrado.find(vdato.upper()) != -1:
                        d['OK_KO'] = "OK"
                        break
                    else:
                        d['OK_KO'] = "KO/VISUAL"
                        V.append('Valor no coincide con información del documento Técnico. Realizar validación VISUAL')
            else:
                d['OK_KO'] = 'KO/VISUAL'
                V.append('Valor no coincide con información del documento Técnico. Realizar validación VISUAL')
        #V.append('Para la presente etapa, la validación debe ser visual')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        return d
    elif regla == 'R_Informe_Medidas_Puntos_Medida_Punto_Medida_Punto_Sensible_Codigo_Postal':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'VISUAL'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        if not (vdato.isdigit() and len(vdato) == 5):
            d['OK_KO'] = 'KO'
            V.append('Debe tener formato de 5 números')
        V.append('Para la presente etapa, la validación debe ser visual')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        return d
    elif regla == 'R_Informe_Medidas_Puntos_Medida_Punto_Medida_Punto_Sensible_Poblacion':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        Poblacion = \
            procesos_comunes.valor_elemento_xml(fichero, './/Estacion_Certificada/Datos_Emplazamiento/Calle/Poblacion')[
                'Valor']
        if str(vdato).strip().upper() != str(Poblacion).strip().upper():
            d['OK_KO'] = 'KO'
            V.append('No es el mismo valor que la Población de los datos del Emplazamiento, revisar visualmente')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        return d
    elif regla == 'R_Informe_Medidas_Puntos_Medida_Punto_Medida_Punto_Sensible_Cod_INE_Termino_Municipal':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        cod_provincia = procesos_comunes.valor_elemento_xml(fichero,
                                                            './/Estacion_Certificada/Datos_Emplazamiento/Cod_INE_Provincia')
        r = procesos_comunes.obtiene_datos_ine(fichero, vdato, cod_provincia['Valor'], ficheros_respaldo)
        if r['Cod_Municipio_Ine'] != vdato:
            d['OK_KO'] = 'KO'
            V.append('El valor no coincide con la tabla de datos del INE')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        return d
    elif regla == 'R_Informe_Medidas_Puntos_Medida_Punto_Medida_Punto_Sensible_Cod_INE_Provincia':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        cod_municipio = procesos_comunes.valor_elemento_xml(fichero,
                                                            './/Estacion_Certificada/Datos_Emplazamiento/Cod_INE_Termino_Municipal')
        r = procesos_comunes.obtiene_datos_ine(fichero, cod_municipio['Valor'], vdato, ficheros_respaldo)
        if r['Cod_Provincia_INE'] != vdato:
            d['OK_KO'] = 'KO'
            V.append('El valor no coincide con la tabla de datos del INE')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        return d
    elif regla == 'R_Informe_Medidas_Informe_Medidas_Fase1_Datos_Medicion_Tecnico_Responsable':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        if not re.match(
                "((([X-Z])|([LM])){1}([-]?)((\d){7})([-]?)([A-Z]{1}))|((\d{8})([-]?)([A-Z]))\s[a-zA-ZàáâäãåąčćęèéêëėįìíîïłńòóôöõøùúûüųūÿýżźñçčšžÀÁÂÄÃÅĄĆČĖĘÈÉÊËÌÍÎÏĮŁŃÒÓÔÖÕØÙÚÛÜŲŪŸÝŻŹÑßÇŒÆČŠŽ∂ð '-]+$",
                vdato):
            d['OK_KO'] = "KO"
            V.append('Tecnico Responsable no tiene el formato correcto')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        return d
    elif regla == 'R_Informe_Medidas_Informe_Medidas_Fase1_Datos_Medicion_Fecha_Medicion':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        if procesos_comunes.add_months(datetime.datetime.strptime(vdato, '%Y-%m-%d').date(), 3) < datetime.date.today():
            d['OK_KO'] = 'KO'
            V.append('Fecha de medición caducada, es mayor a tres meses a fecha de hoy')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        return d
    elif regla == 'R_Informe_Medidas_Informe_Medidas_Fase1_Equipos_Medida_Fase1_Equipo_Medida_Fase1_IdEquipo':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        return d
    elif regla == 'R_Informe_Medidas_Informe_Medidas_Fase1_Equipos_Medida_Fase1_Equipo_Medida_Fase1_Fecha_Ultima_Calibracion':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'KO/VISUAL'
        d['Validacion'] = ''
        if procesos_comunes.add_months(datetime.datetime.strptime(vdato, '%Y-%m-%d').date(),
                                       24) < datetime.date.today():
            d['OK_KO'] = 'KO'
            V.append('La calibración tiene como máximo una duración de 2 años')
        #V.append('Para la presente etapa, la validación debe ser visual')
        fecha_vdato = datetime.datetime.strptime(vdato, '%Y-%m-%d')
        vdato = fecha_vdato.strftime('%d/%m/%Y')
        for encontrado in re.findall("CALIBRACION\s.+".strip(), pdf_texto):
            if encontrado.find(vdato.upper()) != -1:
                d['OK_KO'] = "OK"
                break
            else:
                d['OK_KO'] = "KO/VISUAL"
        if d['OK_KO'] == "KO/VISUAL":
            V.append(
                'Valor: ' + vdato + '  no coincide con dato extraído de PDF: ' + encontrado + '  . La revisión debe ser VISUAL')
        if fichero_tecnico == '':
            V.append('No existe fichero Técnico o no puede ser leido: ' + fichero_nombre + '.pdf' + '  La revisión debe ser VISUAL')
        # V.append('Para la presente etapa, la validación debe ser visual')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        return d
    elif regla == 'R_Informe_Medidas_Informe_Medidas_Fase1_Equipos_Medida_Fase1_Equipo_Medida_Fase1_Umbral_Deteccion_Vm':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        '''
        if float(vdato.replace(',', '.')) < 0.2:
            d['OK_KO'] = 'KO'
            V.append('Toda señal que se haya calculado por debajo de 0,2, no se pone el valor, se pone menor que umbral')
        '''
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        return d
    elif regla == 'R_Informe_Medidas_Informe_Medidas_Fase1_Equipos_Medida_Fase1_Equipo_Medida_Fase1_Longitud_Cable':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        return d
    elif regla == 'R_Informe_Medidas_Informe_Medidas_Fase1_Equipos_Medida_Fase1_Equipo_Medida_Fase1_Medidor_Marca_Medidor':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'KO/VISUAL'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor en el xml')
        #V.append('Fichero analizado: ' + pdf_texto['Fichero'])
        for encontrado in re.findall("MARCA\s.+".strip(), pdf_texto):
            if encontrado.find(vdato.upper()) != -1:
                d['OK_KO'] = "OK"
                break
            else:
                d['OK_KO'] = "KO/VISUAL"
        if d['OK_KO'] == "KO/VISUAL":
            V.append('Valor: '+ vdato + '  no coincide con dato extraído de PDF: ' + encontrado +'  . La revisión debe ser VISUAL')
        if fichero_tecnico == '':
            V.append('No existe fichero Técnico o no puede ser leido: ' + fichero_nombre + '.pdf' + '  La revisión debe ser VISUAL')
        #V.append('Para la presente etapa, la validación debe ser visual')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        return d
    elif regla == 'R_Informe_Medidas_Informe_Medidas_Fase1_Equipos_Medida_Fase1_Equipo_Medida_Fase1_Medidor_Modelo_Medidor':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'KO/VISUAL'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor en el xml')
        #V.append('Fichero analizado: ' + pdf_texto['Fichero'])
        for encontrado in re.findall("MODELO\s.+".strip(), pdf_texto):
            if encontrado.find(vdato.upper()) != -1:
                d['OK_KO'] = "OK"
                break
            else:
                d['OK_KO'] = "KO/VISUAL"
        if d['OK_KO'] == "KO/VISUAL":
            V.append('Valor: '+ vdato + '  no coincide con dato extraído de PDF: ' + encontrado +'  . La revisión debe ser VISUAL')
        if fichero_tecnico == '':
            V.append('No existe fichero Técnico o no puede ser leido: ' + fichero_nombre + '.pdf' + '  La revisión debe ser VISUAL')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        return d
    elif regla == 'R_Informe_Medidas_Informe_Medidas_Fase1_Equipos_Medida_Fase1_Equipo_Medida_Fase1_Medidor_Numero_Serie_Medidor':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'KO/VISUAL'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor en el xml')
        #V.append('Fichero analizado: ' + pdf_texto['Fichero'])
        for encontrado in re.findall("IDENTIFICACION\s.+".strip(), pdf_texto):
            if encontrado.find(vdato.upper()) != -1:
                d['OK_KO'] = "OK"
                break
            else:
                d['OK_KO'] = "KO/VISUAL"
        if d['OK_KO'] == "KO/VISUAL":
            V.append('Valor: '+ vdato + '  no coincide con dato extraído de PDF: ' + encontrado +'  . La revisión debe ser VISUAL')
        if fichero_tecnico == '':
            V.append('No existe fichero Técnico o no puede ser leido: ' + fichero_nombre + '.pdf' + '  La revisión debe ser VISUAL')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        return d
    elif regla == 'R_Informe_Medidas_Informe_Medidas_Fase1_Equipos_Medida_Fase1_Equipo_Medida_Fase1_Antena_Marca_Antena':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'KO/VISUAL'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor en el xml')
        #V.append('Fichero analizado: ' + pdf_texto['Fichero'])
        for encontrado in re.findall("MARCA\s.+".strip(), pdf_texto):
            if encontrado.find(vdato.upper()) != -1:
                d['OK_KO'] = "OK"
                break
            else:
                d['OK_KO'] = "KO/VISUAL"
        if d['OK_KO'] == "KO/VISUAL":
            V.append('Valor: '+ vdato + '  no coincide con dato extraído de PDF: ' + encontrado +'  . La revisión debe ser VISUAL')
        if fichero_tecnico == '':
            V.append('No existe fichero Técnico o no puede ser leido: ' + fichero_nombre + '.pdf' + '  La revisión debe ser VISUAL')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        return d
    elif regla == 'R_Informe_Medidas_Informe_Medidas_Fase1_Equipos_Medida_Fase1_Equipo_Medida_Fase1_Antena_Modelo_Antena':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'KO/VISUAL'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor en el xml')
        #V.append('Fichero analizado: ' + pdf_texto['Fichero'])
        for encontrado in re.findall("SONDA\:.+".strip(), pdf_texto):
            if encontrado.find(vdato.upper()) != -1:
                d['OK_KO'] = "OK"
                break
            else:
                d['OK_KO'] = "KO/VISUAL"
        if d['OK_KO'] == "KO/VISUAL":
            V.append('Valor: '+ vdato + '  no coincide con dato extraído de PDF: ' + encontrado +'  . La revisión debe ser VISUAL')
        if fichero_tecnico == '':
            V.append('No existe fichero Técnico o no puede ser leido: ' + fichero_nombre + '.pdf' + '  La revisión debe ser VISUAL')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        return d
    elif regla == 'R_Informe_Medidas_Informe_Medidas_Fase1_Equipos_Medida_Fase1_Equipo_Medida_Fase1_Antena_Numero_Serie_Antena':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'KO/VISUAL'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor en el xml')
        #V.append('Fichero analizado: ' + pdf_texto['Fichero'])
        for encontrado in re.findall("SONDA\:.+".strip(), pdf_texto):
            if encontrado.find(vdato.upper()) != -1:
                d['OK_KO'] = "OK"
                break
            else:
                d['OK_KO'] = "KO/VISUAL"
        if d['OK_KO'] == "KO/VISUAL":
            V.append('Valor: '+ vdato + '  no coincide con dato extraído de PDF: ' + encontrado +'  . La revisión debe ser VISUAL')
        if fichero_tecnico == '':
            V.append('No existe fichero Técnico o no puede ser leido: ' + fichero_nombre + '.pdf' + '  La revisión debe ser VISUAL')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        return d
    elif regla == 'R_Informe_Medidas_Informe_Medidas_Fase1_Medicion_Fase1_Medida_Fase1_IdPunto':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        c1 = procesos_comunes.cantidad_elementos_xml(fichero, './/Informe_Medidas/Puntos_Medida/Punto_Medida/IdPunto')
        c2 = procesos_comunes.cantidad_elementos_xml(fichero, './/Informe_Medidas/Informe_Medidas_Fase1'
                                                              '/Medicion_Fase1/Medida_Fase1/IdPunto')
        if c1['Cantidad'] != c2['Cantidad']:
            d['OK_KO'] = 'KO'
            V.append('Cantidad de Puntos de Medida diferente a cantidad de Medidas')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        return d
    elif regla == 'R_Informe_Medidas_Informe_Medidas_Fase1_Medicion_Fase1_Medida_Fase1_IdEquipo':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        return d
    elif regla == 'R_Informe_Medidas_Informe_Medidas_Fase1_Medicion_Fase1_Medida_Fase1_Hora_Inicio_Medicion':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        r = procesos_comunes.horas_medicion_diferencia(fichero, d['Etiqueta'])
        if r['OK_KO'] == 'KO':
            d['OK_KO'] = 'KO'
            V.append(r['Comentario'])
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        return d
    elif regla == 'R_Informe_Medidas_Informe_Medidas_Fase1_Medicion_Fase1_Medida_Fase1_Nivel_Referencia_Vm':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'VISUAL'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        V.append('Para la presente etapa, la validación debe ser visual')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        return d
    elif regla == 'R_Informe_Medidas_Informe_Medidas_Fase1_Medicion_Fase1_Medida_Fase1_Nivel_Decision_Vm':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        dr = procesos_comunes.validaciones_real_medida_fase_etiqueta(fichero, d['Etiqueta'])
        if dr['OK_KO'] == 'KO':
            d['OK_KO'] = 'KO'
            V.append(dr['Error'])
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        return d
    elif regla == 'R_Informe_Medidas_Informe_Medidas_Fase1_Medicion_Fase1_Medida_Fase1_Valor_Medido_Promediado_Vm':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        dr = procesos_comunes.validaciones_real_medida_fase_etiqueta(fichero, d['Etiqueta'])
        if dr['OK_KO'] == 'KO':
            d['OK_KO'] = 'KO'
            V.append(dr['Error'])
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        return d
    elif regla == 'R_Informe_Medidas_Informe_Medidas_Fase1_Medicion_Fase1_Medida_Fase1_Valor_Calculado_Vm':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        dr = procesos_comunes.validaciones_real_medida_fase_etiqueta(fichero, d['Etiqueta'])
        if dr['OK_KO'] == 'KO':
            d['OK_KO'] = 'KO'
            V.append(dr['Error'])
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        return d
    elif regla == 'R_Informe_Medidas_Informe_Medidas_Fase1_Medicion_Fase1_Medida_Fase1_Diferencia_Vm':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        dr = procesos_comunes.validaciones_real_medida_fase_etiqueta(fichero, d['Etiqueta'])
        if dr['OK_KO'] == 'KO':
            d['OK_KO'] = 'KO'
            V.append(dr['Error'])
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        return d
    elif regla == 'R_Documentos_Informacion_Adicional_Documento_Nombre':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''
        if vdato is None:
            d['OK_KO'] = 'KO'
            V.append('No existe valor')
        if vdato.strip() != fichero_nombre.strip():
            d['OK_KO'] = 'KO'
            V.append('El dato no coincide con el nombre del documento')
        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        return d
    elif regla == 'R_Documentos_Informacion_Adicional_Documento_Extension':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''

        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        return d
    elif regla == 'R_Documentos_Informacion_Adicional_Documento_Codificacion':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''

        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        return d
    elif regla == 'R_Documentos_Informacion_Adicional_Documento_Contenido':
        d['Etiqueta'] = etiqueta
        d['Valor'] = vdato
        d['OK_KO'] = 'OK'
        d['Validacion'] = ''

        d['Validacion'] = V
        d['Fecha_Hora'] = datetime.datetime.now()
        return d
