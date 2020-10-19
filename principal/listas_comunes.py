etiqueta_xml = ['.//Datos_Certificacion/'
    , './/Datos_Certificacion/Datos_Visado/'
    , './/Datos_Certificacion/Tecnico_Competente/'
    , './/Estacion_Certificada/Datos_Emplazamiento/'
    , './/Estacion_Certificada/Datos_Emplazamiento/Calle/'
    , './/Estacion_Certificada/Datos_Estacion/'
    , './/Estacion_Certificada/Datos_Estacion/Sectores/Sector/'
    , './/Estacion_Certificada/Datos_Estacion/Sectores/Sector/Antena_Directiva/'
    , './/Estacion_Certificada/Datos_Estacion/Sectores/Sector/Volumen_Referencia/'
    , './/Informe_Medidas/Puntos_Medida/Punto_Medida/'
    , './/Informe_Medidas/Puntos_Medida/Punto_Medida/Punto_Sensible/'
    , './/Informe_Medidas/Informe_Medidas_Fase1/Datos_Medicion/'
    , './/Informe_Medidas/Informe_Medidas_Fase1/Equipos_Medida_Fase1/Equipo_Medida_Fase1/'
    , './/Informe_Medidas/Informe_Medidas_Fase1/Equipos_Medida_Fase1/Equipo_Medida_Fase1/Medidor/'
    , './/Informe_Medidas/Informe_Medidas_Fase1/Equipos_Medida_Fase1/Equipo_Medida_Fase1/Antena/'
    , './/Informe_Medidas/Informe_Medidas_Fase1/Medicion_Fase1/Medida_Fase1/'
    , './/Documentos/Informacion_Adicional/Documento/'
                ]

lista_completa_old = [
    {'Etiqueta': './/Datos_Certificacion/Tipo_Certificacion', 'Regla': 'R_Datos_Certificacion_Tipo_Certificacion'}
    , {'Etiqueta': './/Datos_Certificacion/Tipo_Solicitud', 'Regla': 'R_Datos_Certificacion_Tipo_Solicitud'}
    , {'Etiqueta': './/Datos_Certificacion/Titular_Nombre_Razon_Social',
       'Regla': 'R_Datos_Certificacion_Titular_Nombre_Razon_Social'}
    , {'Etiqueta': './/Datos_Certificacion/Expediente_Concesional',
       'Regla': 'R_Datos_Certificacion_Expediente_Concesional'}
    , {'Etiqueta': './/Datos_Certificacion/Datos_Visado/Numero_Visado',
       'Regla': 'R_Datos_Certificacion_Datos_Visado_Numero_Visado'}
    , {'Etiqueta': './/Datos_Certificacion/Datos_Visado/Fecha_Visado',
       'Regla': 'R_Datos_Certificacion_Datos_Visado_Fecha_Visado'}
    , {'Etiqueta': './/Datos_Certificacion/Datos_Visado/Numero_Colegiado',
       'Regla': 'R_Datos_Certificacion_Datos_Visado_Numero_Colegiado'}
    , {'Etiqueta': './/Datos_Certificacion/Datos_Visado/Colegio_Profesional',
       'Regla': 'R_Datos_Certificacion_Datos_Visado_Colegio_Profesional'}
    , {'Etiqueta': './/Datos_Certificacion/Tecnico_Competente/NIF_NIE',
       'Regla': 'R_Datos_Certificacion_Tecnico_Competente_NIF_NIE'}
    , {'Etiqueta': './/Datos_Certificacion/Tecnico_Competente/Nombre',
       'Regla': 'R_Datos_Certificacion_Tecnico_Competente_Nombre'}
    , {'Etiqueta': './/Datos_Certificacion/Tecnico_Competente/Apellido1',
       'Regla': 'R_Datos_Certificacion_Tecnico_Competente_Apellido1'}
    , {'Etiqueta': './/Datos_Certificacion/Tecnico_Competente/Apellido2',
       'Regla': 'R_Datos_Certificacion_Tecnico_Competente_Apellido2'}
    , {'Etiqueta': './/Estacion_Certificada/Datos_Emplazamiento/Codigo_Emplazamiento',
       'Regla': 'R_Estacion_Certificada_Datos_Emplazamiento_Codigo_Emplazamiento'}
    , {'Etiqueta': './/Estacion_Certificada/Datos_Emplazamiento/Emplazamiento_Compartido',
       'Regla': 'R_Estacion_Certificada_Datos_Emplazamiento_Emplazamiento_Compartido'}
    , {'Etiqueta': './/Estacion_Certificada/Datos_Emplazamiento/Cod_INE_Termino_Municipal',
       'Regla': 'R_Estacion_Certificada_Datos_Emplazamiento_Cod_INE_Termino_Municipal'}
    , {'Etiqueta': './/Estacion_Certificada/Datos_Emplazamiento/Cod_INE_Provincia',
       'Regla': 'R_Estacion_Certificada_Datos_Emplazamiento_Cod_INE_Provincia'}
    , {'Etiqueta': './/Estacion_Certificada/Datos_Emplazamiento/Latitud',
       'Regla': 'R_Estacion_Certificada_Datos_Emplazamiento_Latitud'}
    , {'Etiqueta': './/Estacion_Certificada/Datos_Emplazamiento/Longitud',
       'Regla': 'R_Estacion_Certificada_Datos_Emplazamiento_Longitud'}
    , {'Etiqueta': './/Estacion_Certificada/Datos_Emplazamiento/Datum',
       'Regla': 'R_Estacion_Certificada_Datos_Emplazamiento_Datum'}
    , {'Etiqueta': './/Estacion_Certificada/Datos_Emplazamiento/Referencia_Catastral',
       'Regla': 'R_Estacion_Certificada_Datos_Emplazamiento_Referencia_Catastral'}
    , {'Etiqueta': './/Estacion_Certificada/Datos_Emplazamiento/Cota_Terreno_Sobre_Nivel_Mar',
       'Regla': 'R_Estacion_Certificada_Datos_Emplazamiento_Cota_Terreno_Sobre_Nivel_Mar'}
    , {'Etiqueta': './/Estacion_Certificada/Datos_Emplazamiento/Calle/Poblacion',
       'Regla': 'R_Estacion_Certificada_Datos_Emplazamiento_Calle_Poblacion'}
    , {'Etiqueta': './/Estacion_Certificada/Datos_Emplazamiento/Calle/Tipo_Via',
       'Regla': 'R_Estacion_Certificada_Datos_Emplazamiento_Calle_Tipo_Via'}
    , {'Etiqueta': './/Estacion_Certificada/Datos_Emplazamiento/Calle/Nombre_Via',
       'Regla': 'R_Estacion_Certificada_Datos_Emplazamiento_Calle_Nombre_Via'}
    , {'Etiqueta': './/Estacion_Certificada/Datos_Emplazamiento/Calle/Numero_Portal',
       'Regla': 'R_Estacion_Certificada_Datos_Emplazamiento_Calle_Numero_Portal'}
    , {'Etiqueta': './/Estacion_Certificada/Datos_Emplazamiento/Calle/Situacion',
       'Regla': 'R_Estacion_Certificada_Datos_Emplazamiento_Calle_Situacion'}
    , {'Etiqueta': './/Estacion_Certificada/Datos_Estacion/Codigo_Expediente',
       'Regla': 'R_Estacion_Certificada_Datos_Estacion_Codigo_Expediente'}
    , {'Etiqueta': './/Estacion_Certificada/Datos_Estacion/Codigo_Estacion',
       'Regla': 'R_Estacion_Certificada_Datos_Estacion_Codigo_Estacion'}
    , {'Etiqueta': './/Estacion_Certificada/Datos_Estacion/Tipo_Sistema',
       'Regla': 'R_Estacion_Certificada_Datos_Estacion_Tipo_Sistema'}
    , {'Etiqueta': './/Estacion_Certificada/Datos_Estacion/Tipo_Estacion',
       'Regla': 'R_Estacion_Certificada_Datos_Estacion_Tipo_Estacion'}
    , {'Etiqueta': './/Estacion_Certificada/Datos_Estacion/Entorno_Sensible',
       'Regla': 'R_Estacion_Certificada_Datos_Estacion_Entorno_Sensible'}
    , {'Etiqueta': './/Estacion_Certificada/Datos_Estacion/Num_Sectores_Interiores',
       'Regla': 'R_Estacion_Certificada_Datos_Estacion_Num_Sectores_Interiores'}
    , {'Etiqueta': './/Estacion_Certificada/Datos_Estacion/Num_Sectores_Exteriores',
       'Regla': 'R_Estacion_Certificada_Datos_Estacion_Num_Sectores_Exteriores'}
    , {'Etiqueta': './/Estacion_Certificada/Datos_Estacion/Sectores/Sector/Tipo_Potencia_Radiada',
       'Regla': 'R_Estacion_Certificada_Datos_Estacion_Sectores_Sector_Tipo_Potencia_Radiada'}
    , {'Etiqueta': './/Estacion_Certificada/Datos_Estacion/Sectores/Sector/Potencia_Maxima_Total',
       'Regla': 'R_Estacion_Certificada_Datos_Estacion_Sectores_Sector_Potencia_Maxima_Total'}
    , {'Etiqueta': './/Estacion_Certificada/Datos_Estacion/Sectores/Sector/Unidad_Potencia_Maxima_Total',
       'Regla': 'R_Estacion_Certificada_Datos_Estacion_Sectores_Sector_Unidad_Potencia_Maxima_Total'}
    , {'Etiqueta': './/Estacion_Certificada/Datos_Estacion/Sectores/Sector/Localizacion_Antena',
       'Regla': 'R_Estacion_Certificada_Datos_Estacion_Sectores_Sector_Localizacion_Antena'}
    , {'Etiqueta': './/Estacion_Certificada/Datos_Estacion/Sectores/Sector/Tipo_Antena',
       'Regla': 'R_Estacion_Certificada_Datos_Estacion_Sectores_Sector_Tipo_Antena'}
    , {'Etiqueta': './/Estacion_Certificada/Datos_Estacion/Sectores/Sector/Polarizacion',
       'Regla': 'R_Estacion_Certificada_Datos_Estacion_Sectores_Sector_Polarizacion'}
    , {'Etiqueta': './/Estacion_Certificada/Datos_Estacion/Sectores/Sector/Altura_Antena_Sobre_Terreno',
       'Regla': 'R_Estacion_Certificada_Datos_Estacion_Sectores_Sector_Altura_Antena_Sobre_Terreno'}
    , {'Etiqueta': './/Estacion_Certificada/Datos_Estacion/Sectores/Sector/Inclinacion_Haz_Sobre_Horizontal',
       'Regla': 'R_Estacion_Certificada_Datos_Estacion_Sectores_Sector_Inclinacion_Haz_Sobre_Horizontal'}
    , {'Etiqueta': './/Estacion_Certificada/Datos_Estacion/Sectores/Sector/Antena_Directiva/Tipo_Ganancia',
       'Regla': 'R_Estacion_Certificada_Datos_Estacion_Sectores_Sector_Antena_Directiva_Tipo_Ganancia'}
    , {'Etiqueta': './/Estacion_Certificada/Datos_Estacion/Sectores/Sector/Antena_Directiva/Ganancia_Antena',
       'Regla': 'R_Estacion_Certificada_Datos_Estacion_Sectores_Sector_Antena_Directiva_Ganancia_Antena'}
    , {'Etiqueta': './/Estacion_Certificada/Datos_Estacion/Sectores/Sector/Antena_Directiva/Apertura_Horizontal_Haz',
       'Regla': 'R_Estacion_Certificada_Datos_Estacion_Sectores_Sector_Antena_Directiva_Apertura_Horizontal_Haz'}
    , {'Etiqueta': './/Estacion_Certificada/Datos_Estacion/Sectores/Sector/Antena_Directiva/Apertura_Vertical_Haz',
       'Regla': 'R_Estacion_Certificada_Datos_Estacion_Sectores_Sector_Antena_Directiva_Apertura_Vertical_Haz'}
    , {'Etiqueta': './/Estacion_Certificada/Datos_Estacion/Sectores/Sector/Antena_Directiva/Acimut_Maxima_Radiacion',
       'Regla': 'R_Estacion_Certificada_Datos_Estacion_Sectores_Sector_Antena_Directiva_Acimut_Maxima_Radiacion'}
    , {'Etiqueta': './/Estacion_Certificada/Datos_Estacion/Sectores/Sector/Antena_Directiva/Nivel_Lobulos_Secundarios',
       'Regla': 'R_Estacion_Certificada_Datos_Estacion_Sectores_Sector_Antena_Directiva_Nivel_Lobulos_Secundarios'}
    , {'Etiqueta': './/Estacion_Certificada/Datos_Estacion/Sectores/Sector/Volumen_Referencia/Forma_Volumen',
       'Regla': 'R_Estacion_Certificada_Datos_Estacion_Sectores_Sector_Volumen_Referencia_Forma_Volumen'}
    , {'Etiqueta': './/Estacion_Certificada/Datos_Estacion/Sectores/Sector/Volumen_Referencia/Distancia_Referencia',
       'Regla': 'R_Estacion_Certificada_Datos_Estacion_Sectores_Sector_Volumen_Referencia_Distancia_Referencia'}
    , {'Etiqueta': './/Estacion_Certificada/Datos_Estacion/Sectores/Sector/Volumen_Referencia/Coeficiente_Reflexion',
       'Regla': 'R_Estacion_Certificada_Datos_Estacion_Sectores_Sector_Volumen_Referencia_Coeficiente_Reflexion'}
    , {'Etiqueta': './/Informe_Medidas/Puntos_Medida/Punto_Medida/IdPunto',
       'Regla': 'R_Informe_Medidas_Puntos_Medida_Punto_Medida_IdPunto'}
    , {'Etiqueta': './/Informe_Medidas/Puntos_Medida/Punto_Medida/Distancia',
       'Regla': 'R_Informe_Medidas_Puntos_Medida_Punto_Medida_Distancia'}
    , {'Etiqueta': './/Informe_Medidas/Puntos_Medida/Punto_Medida/Acimut',
       'Regla': 'R_Informe_Medidas_Puntos_Medida_Punto_Medida_Acimut'}
    , {'Etiqueta': './/Informe_Medidas/Puntos_Medida/Punto_Medida/Punto_Sensible/Situacion',
       'Regla': 'R_Informe_Medidas_Puntos_Medida_Punto_Medida_Punto_Sensible_Situacion'}
    , {'Etiqueta': './/Informe_Medidas/Puntos_Medida/Punto_Medida/Punto_Sensible/Tipo_Espacio_Sensible',
       'Regla': 'R_Informe_Medidas_Puntos_Medida_Punto_Medida_Punto_Sensible_Tipo_Espacio_Sensible'}
    , {'Etiqueta': './/Informe_Medidas/Puntos_Medida/Punto_Medida/Punto_Sensible/Tipo_Via',
       'Regla': 'R_Informe_Medidas_Puntos_Medida_Punto_Medida_Punto_Sensible_Tipo_Via'}
    , {'Etiqueta': './/Informe_Medidas/Puntos_Medida/Punto_Medida/Punto_Sensible/Nombre_Via',
       'Regla': 'R_Informe_Medidas_Puntos_Medida_Punto_Medida_Punto_Sensible_Nombre_Via'}
    , {'Etiqueta': './/Informe_Medidas/Puntos_Medida/Punto_Medida/Punto_Sensible/Numero_Portal',
       'Regla': 'R_Informe_Medidas_Puntos_Medida_Punto_Medida_Punto_Sensible_Numero_Portal'}
    , {'Etiqueta': './/Informe_Medidas/Puntos_Medida/Punto_Medida/Punto_Sensible/Codigo_Postal',
       'Regla': 'R_Informe_Medidas_Puntos_Medida_Punto_Medida_Punto_Sensible_Codigo_Postal'}
    , {'Etiqueta': './/Informe_Medidas/Puntos_Medida/Punto_Medida/Punto_Sensible/Poblacion',
       'Regla': 'R_Informe_Medidas_Puntos_Medida_Punto_Medida_Punto_Sensible_Poblacion'}
    , {'Etiqueta': './/Informe_Medidas/Puntos_Medida/Punto_Medida/Punto_Sensible/Cod_INE_Termino_Municipal',
       'Regla': 'R_Informe_Medidas_Puntos_Medida_Punto_Medida_Punto_Sensible_Cod_INE_Termino_Municipal'}
    , {'Etiqueta': './/Informe_Medidas/Puntos_Medida/Punto_Medida/Punto_Sensible/Cod_INE_Provincia',
       'Regla': 'R_Informe_Medidas_Puntos_Medida_Punto_Medida_Punto_Sensible_Cod_INE_Provincia'}
    , {'Etiqueta': './/Informe_Medidas/Informe_Medidas_Fase1/Datos_Medicion/Tecnico_Responsable',
       'Regla': 'R_Informe_Medidas_Informe_Medidas_Fase1_Datos_Medicion_Tecnico_Responsable'}
    , {'Etiqueta': './/Informe_Medidas/Informe_Medidas_Fase1/Datos_Medicion/Fecha_Medicion',
       'Regla': 'R_Informe_Medidas_Informe_Medidas_Fase1_Datos_Medicion_Fecha_Medicion'}
    , {'Etiqueta': './/Informe_Medidas/Informe_Medidas_Fase1/Equipos_Medida_Fase1/Equipo_Medida_Fase1/IdEquipo',
       'Regla': 'R_Informe_Medidas_Informe_Medidas_Fase1_Equipos_Medida_Fase1_Equipo_Medida_Fase1_IdEquipo'}
    , {
        'Etiqueta': './/Informe_Medidas/Informe_Medidas_Fase1/Equipos_Medida_Fase1/Equipo_Medida_Fase1/Fecha_Ultima_Calibracion',
        'Regla': 'R_Informe_Medidas_Informe_Medidas_Fase1_Equipos_Medida_Fase1_Equipo_Medida_Fase1_Fecha_Ultima_Calibracion'}
    , {
        'Etiqueta': './/Informe_Medidas/Informe_Medidas_Fase1/Equipos_Medida_Fase1/Equipo_Medida_Fase1/Umbral_Deteccion_Vm',
        'Regla': 'R_Informe_Medidas_Informe_Medidas_Fase1_Equipos_Medida_Fase1_Equipo_Medida_Fase1_Umbral_Deteccion_Vm'}
    , {'Etiqueta': './/Informe_Medidas/Informe_Medidas_Fase1/Equipos_Medida_Fase1/Equipo_Medida_Fase1/Longitud_Cable',
       'Regla': 'R_Informe_Medidas_Informe_Medidas_Fase1_Equipos_Medida_Fase1_Equipo_Medida_Fase1_Longitud_Cable'}
    , {
        'Etiqueta': './/Informe_Medidas/Informe_Medidas_Fase1/Equipos_Medida_Fase1/Equipo_Medida_Fase1/Medidor/Marca_Medidor',
        'Regla': 'R_Informe_Medidas_Informe_Medidas_Fase1_Equipos_Medida_Fase1_Equipo_Medida_Fase1_Medidor_Marca_Medidor'}
    , {
        'Etiqueta': './/Informe_Medidas/Informe_Medidas_Fase1/Equipos_Medida_Fase1/Equipo_Medida_Fase1/Medidor/Modelo_Medidor',
        'Regla': 'R_Informe_Medidas_Informe_Medidas_Fase1_Equipos_Medida_Fase1_Equipo_Medida_Fase1_Medidor_Modelo_Medidor'}
    , {
        'Etiqueta': './/Informe_Medidas/Informe_Medidas_Fase1/Equipos_Medida_Fase1/Equipo_Medida_Fase1/Medidor/Numero_Serie_Medidor',
        'Regla': 'R_Informe_Medidas_Informe_Medidas_Fase1_Equipos_Medida_Fase1_Equipo_Medida_Fase1_Medidor_Numero_Serie_Medidor'}
    , {
        'Etiqueta': './/Informe_Medidas/Informe_Medidas_Fase1/Equipos_Medida_Fase1/Equipo_Medida_Fase1/Antena/Marca_Antena',
        'Regla': 'R_Informe_Medidas_Informe_Medidas_Fase1_Equipos_Medida_Fase1_Equipo_Medida_Fase1_Antena_Marca_Antena'}
    , {
        'Etiqueta': './/Informe_Medidas/Informe_Medidas_Fase1/Equipos_Medida_Fase1/Equipo_Medida_Fase1/Antena/Modelo_Antena',
        'Regla': 'R_Informe_Medidas_Informe_Medidas_Fase1_Equipos_Medida_Fase1_Equipo_Medida_Fase1_Antena_Modelo_Antena'}
    , {
        'Etiqueta': './/Informe_Medidas/Informe_Medidas_Fase1/Equipos_Medida_Fase1/Equipo_Medida_Fase1/Antena/Numero_Serie_Antena',
        'Regla': 'R_Informe_Medidas_Informe_Medidas_Fase1_Equipos_Medida_Fase1_Equipo_Medida_Fase1_Antena_Numero_Serie_Antena'}
    , {'Etiqueta': './/Informe_Medidas/Informe_Medidas_Fase1/Medicion_Fase1/Medida_Fase1/IdPunto',
       'Regla': 'R_Informe_Medidas_Informe_Medidas_Fase1_Medicion_Fase1_Medida_Fase1_IdPunto'}
    , {'Etiqueta': './/Informe_Medidas/Informe_Medidas_Fase1/Medicion_Fase1/Medida_Fase1/IdEquipo',
       'Regla': 'R_Informe_Medidas_Informe_Medidas_Fase1_Medicion_Fase1_Medida_Fase1_IdEquipo'}
    , {'Etiqueta': './/Informe_Medidas/Informe_Medidas_Fase1/Medicion_Fase1/Medida_Fase1/Hora_Inicio_Medicion',
       'Regla': 'R_Informe_Medidas_Informe_Medidas_Fase1_Medicion_Fase1_Medida_Fase1_Hora_Inicio_Medicion'}
    , {'Etiqueta': './/Informe_Medidas/Informe_Medidas_Fase1/Medicion_Fase1/Medida_Fase1/Nivel_Referencia_Vm',
       'Regla': 'R_Informe_Medidas_Informe_Medidas_Fase1_Medicion_Fase1_Medida_Fase1_Nivel_Referencia_Vm'}
    , {'Etiqueta': './/Informe_Medidas/Informe_Medidas_Fase1/Medicion_Fase1/Medida_Fase1/Nivel_Decision_Vm',
       'Regla': 'R_Informe_Medidas_Informe_Medidas_Fase1_Medicion_Fase1_Medida_Fase1_Nivel_Decision_Vm'}
    , {'Etiqueta': './/Informe_Medidas/Informe_Medidas_Fase1/Medicion_Fase1/Medida_Fase1/Valor_Medido_Promediado_Vm',
       'Regla': 'R_Informe_Medidas_Informe_Medidas_Fase1_Medicion_Fase1_Medida_Fase1_Valor_Medido_Promediado_Vm'}
    , {'Etiqueta': './/Informe_Medidas/Informe_Medidas_Fase1/Medicion_Fase1/Medida_Fase1/Valor_Calculado_Vm',
       'Regla': 'R_Informe_Medidas_Informe_Medidas_Fase1_Medicion_Fase1_Medida_Fase1_Valor_Calculado_Vm'}
    , {'Etiqueta': './/Informe_Medidas/Informe_Medidas_Fase1/Medicion_Fase1/Medida_Fase1/Diferencia_Vm',
       'Regla': 'R_Informe_Medidas_Informe_Medidas_Fase1_Medicion_Fase1_Medida_Fase1_Diferencia_Vm'}
    , {'Etiqueta': './/Documentos/Informacion_Adicional/Documento/Nombre',
       'Regla': 'R_Documentos_Informacion_Adicional_Documento_Nombre'}
    , {'Etiqueta': './/Documentos/Informacion_Adicional/Documento/Extension',
       'Regla': 'R_Documentos_Informacion_Adicional_Documento_Extension'}
    , {'Etiqueta': './/Documentos/Informacion_Adicional/Documento/Codificacion',
       'Regla': 'R_Documentos_Informacion_Adicional_Documento_Codificacion'}
    , {'Etiqueta': './/Documentos/Informacion_Adicional/Documento/Contenido',
       'Regla': 'R_Documentos_Informacion_Adicional_Documento_Contenido'}

]

lista_completa = [
 {'Etiqueta': './/Datos_Certificacion/Tipo_Certificacion', 'Regla': 'R_Datos_Certificacion_Tipo_Certificacion', 'Comparacion': 'Se chequea dentro de XML, igual a A'}
,{'Etiqueta': './/Datos_Certificacion/Tipo_Solicitud', 'Regla': 'R_Datos_Certificacion_Tipo_Solicitud', 'Comparacion': 'Se chequea dentro de XML, valor: Alt o MOD'}
,{'Etiqueta': './/Datos_Certificacion/Titular_Nombre_Razon_Social', 'Regla': 'R_Datos_Certificacion_Titular_Nombre_Razon_Social', 'Comparacion': 'Se compara con el parámetro Titular_Nombre_Razon_Social del documento XML'}
,{'Etiqueta': './/Datos_Certificacion/Expediente_Concesional', 'Regla': 'R_Datos_Certificacion_Expediente_Concesional', 'Comparacion': 'Se compara con el parámetro Expediente_Concesional del documento XML'}
,{'Etiqueta': './/Datos_Certificacion/Datos_Visado/Numero_Visado', 'Regla': 'R_Datos_Certificacion_Datos_Visado_Numero_Visado', 'Comparacion': 'Se compara con el parámetro Numero_Visado del documento XML'}
,{'Etiqueta': './/Datos_Certificacion/Datos_Visado/Fecha_Visado', 'Regla': 'R_Datos_Certificacion_Datos_Visado_Fecha_Visado', 'Comparacion': 'Se compara con el parámetro Numero_Visado del documento XML'}
,{'Etiqueta': './/Datos_Certificacion/Datos_Visado/Numero_Colegiado', 'Regla': 'R_Datos_Certificacion_Datos_Visado_Numero_Colegiado', 'Comparacion': 'Se compara con el parámetro Numero_Colegiado del documento XML'}
,{'Etiqueta': './/Datos_Certificacion/Datos_Visado/Colegio_Profesional', 'Regla': 'R_Datos_Certificacion_Datos_Visado_Colegio_Profesional', 'Comparacion': 'Se compara con el parámetro Colegio_Profesional del documento XML'}
,{'Etiqueta': './/Datos_Certificacion/Tecnico_Competente/NIF_NIE', 'Regla': 'R_Datos_Certificacion_Tecnico_Competente_NIF_NIE', 'Comparacion': 'Se compara con el documento PDF Declaración Responsable de Técnico competente'}
,{'Etiqueta': './/Datos_Certificacion/Tecnico_Competente/Nombre', 'Regla': 'R_Datos_Certificacion_Tecnico_Competente_Nombre', 'Comparacion': 'Se compara con el documento PDF Declaración Responsable de Técnico competente'}
,{'Etiqueta': './/Datos_Certificacion/Tecnico_Competente/Apellido1', 'Regla': 'R_Datos_Certificacion_Tecnico_Competente_Apellido1', 'Comparacion': 'Se compara con el documento PDF Declaración Responsable de Técnico competente'}
,{'Etiqueta': './/Datos_Certificacion/Tecnico_Competente/Apellido2', 'Regla': 'R_Datos_Certificacion_Tecnico_Competente_Apellido2', 'Comparacion': 'Se compara con el documento PDF Declaración Responsable de Técnico competente'}
,{'Etiqueta': './/Estacion_Certificada/Datos_Emplazamiento/Codigo_Emplazamiento', 'Regla': 'R_Estacion_Certificada_Datos_Emplazamiento_Codigo_Emplazamiento', 'Comparacion': 'Se compara con Excel de Códigos INE'}
,{'Etiqueta': './/Estacion_Certificada/Datos_Emplazamiento/Emplazamiento_Compartido', 'Regla': 'R_Estacion_Certificada_Datos_Emplazamiento_Emplazamiento_Compartido', 'Comparacion': 'Se compara con Excel de Códigos INE'}
,{'Etiqueta': './/Estacion_Certificada/Datos_Emplazamiento/Cod_INE_Termino_Municipal', 'Regla': 'R_Estacion_Certificada_Datos_Emplazamiento_Cod_INE_Termino_Municipal', 'Comparacion': 'Se compara con el Término Municipal del documento Excel de Códigos INE'}
,{'Etiqueta': './/Estacion_Certificada/Datos_Emplazamiento/Cod_INE_Provincia', 'Regla': 'R_Estacion_Certificada_Datos_Emplazamiento_Cod_INE_Provincia', 'Comparacion': 'Se compara con el Cod_INE_Provincia del documento Excel de Códigos INE'}
,{'Etiqueta': './/Estacion_Certificada/Datos_Emplazamiento/Latitud', 'Regla': 'R_Estacion_Certificada_Datos_Emplazamiento_Latitud', 'Comparacion': 'Se compara con información obtenida de la página web de Infoantenas'}
,{'Etiqueta': './/Estacion_Certificada/Datos_Emplazamiento/Longitud', 'Regla': 'R_Estacion_Certificada_Datos_Emplazamiento_Longitud', 'Comparacion': 'Se compara con información obtenida de la página web de Infoantenas'}
,{'Etiqueta': './/Estacion_Certificada/Datos_Emplazamiento/Datum', 'Regla': 'R_Estacion_Certificada_Datos_Emplazamiento_Datum', 'Comparacion': 'Se compara con el parámetro Datum del documento XML'}
,{'Etiqueta': './/Estacion_Certificada/Datos_Emplazamiento/Referencia_Catastral', 'Regla': 'R_Estacion_Certificada_Datos_Emplazamiento_Referencia_Catastral', 'Comparacion': 'Se compara con el dato recogido de la página web de sede catastro'}
,{'Etiqueta': './/Estacion_Certificada/Datos_Emplazamiento/Cota_Terreno_Sobre_Nivel_Mar', 'Regla': 'R_Estacion_Certificada_Datos_Emplazamiento_Cota_Terreno_Sobre_Nivel_Mar', 'Comparacion': 'Se compara con el valor de la página web de iberpix'}
,{'Etiqueta': './/Estacion_Certificada/Datos_Emplazamiento/Calle/Poblacion', 'Regla': 'R_Estacion_Certificada_Datos_Emplazamiento_Calle_Poblacion', 'Comparacion': 'Se compara con el dato recogido de la página web de sede catastro'}
,{'Etiqueta': './/Estacion_Certificada/Datos_Emplazamiento/Calle/Tipo_Via', 'Regla': 'R_Estacion_Certificada_Datos_Emplazamiento_Calle_Tipo_Via', 'Comparacion': 'Se compara con el dato recogido de la página web de sede catastro'}
,{'Etiqueta': './/Estacion_Certificada/Datos_Emplazamiento/Calle/Nombre_Via', 'Regla': 'R_Estacion_Certificada_Datos_Emplazamiento_Calle_Nombre_Via', 'Comparacion': 'Se compara con el dato recogido de la página web de sede catastro'}
,{'Etiqueta': './/Estacion_Certificada/Datos_Emplazamiento/Calle/Numero_Portal', 'Regla': 'R_Estacion_Certificada_Datos_Emplazamiento_Calle_Numero_Portal', 'Comparacion': 'Se compara con el dato recogido de la página web de sede catastro'}
,{'Etiqueta': './/Estacion_Certificada/Datos_Emplazamiento/Calle/Situacion', 'Regla': 'R_Estacion_Certificada_Datos_Emplazamiento_Calle_Situacion', 'Comparacion': 'Dato no obligatorio, se utiliza para especificar aún con mas detalle la ubicación de la BTS'}
,{'Etiqueta': './/Estacion_Certificada/Datos_Estacion/Codigo_Estacion', 'Regla': 'R_Estacion_Certificada_Datos_Estacion_Codigo_Estacion', 'Comparacion': 'Se compara con el titulo del XML'}
,{'Etiqueta': './/Estacion_Certificada/Datos_Estacion/Tipo_Sistema', 'Regla': 'R_Estacion_Certificada_Datos_Estacion_Tipo_Sistema', 'Comparacion': 'Se comprueba si es una tecnologia valida contra el fichero de referencia pdf'}
,{'Etiqueta': './/Estacion_Certificada/Datos_Estacion/Tipo_Estacion', 'Regla': 'R_Estacion_Certificada_Datos_Estacion_Tipo_Estacion', 'Comparacion': 'Se comprueba el dato contra la web "Sistema de Informacion Urbana"'}
,{'Etiqueta': './/Estacion_Certificada/Datos_Estacion/Entorno_Sensible', 'Regla': 'R_Estacion_Certificada_Datos_Estacion_Entorno_Sensible', 'Comparacion': 'Se comprueba dentro del XML, SI o NO'}
,{'Etiqueta': './/Estacion_Certificada/Datos_Estacion/Num_Sectores_Interiores', 'Regla': 'R_Estacion_Certificada_Datos_Estacion_Num_Sectores_Interiores', 'Comparacion': 'Se comparara con el fichero CAB y debe haber tantos sectores como número indicado'}
,{'Etiqueta': './/Estacion_Certificada/Datos_Estacion/Num_Sectores_Exteriores', 'Regla': 'R_Estacion_Certificada_Datos_Estacion_Num_Sectores_Exteriores', 'Comparacion': 'Se comparara con el fichero CAB y debe haber tantos sectores como número indicado'}
,{'Etiqueta': './/Estacion_Certificada/Datos_Estacion/Sectores/Sector/Tipo_Potencia_Radiada', 'Regla': 'R_Estacion_Certificada_Datos_Estacion_Sectores_Sector_Tipo_Potencia_Radiada', 'Comparacion': 'Se comprueba dentro del XML, PIRE'}
,{'Etiqueta': './/Estacion_Certificada/Datos_Estacion/Sectores/Sector/Potencia_Maxima_Total', 'Regla': 'R_Estacion_Certificada_Datos_Estacion_Sectores_Sector_Potencia_Maxima_Total', 'Comparacion': 'Comprobacion dentro del XML, debe de estar llenado y se revisa que sea numero'}
,{'Etiqueta': './/Estacion_Certificada/Datos_Estacion/Sectores/Sector/Unidad_Potencia_Maxima_Total', 'Regla': 'R_Estacion_Certificada_Datos_Estacion_Sectores_Sector_Unidad_Potencia_Maxima_Total', 'Comparacion': 'Comprobacion dentro del XML, debe estar llenado y valor en W'}
,{'Etiqueta': './/Estacion_Certificada/Datos_Estacion/Sectores/Sector/Localizacion_Antena', 'Regla': 'R_Estacion_Certificada_Datos_Estacion_Sectores_Sector_Localizacion_Antena', 'Comparacion': 'Se comprueba con el diseño  CAP/FSC'}
,{'Etiqueta': './/Estacion_Certificada/Datos_Estacion/Sectores/Sector/Tipo_Antena', 'Regla': 'R_Estacion_Certificada_Datos_Estacion_Sectores_Sector_Tipo_Antena', 'Comparacion': 'Se comprueba con el diseño  CAP/FSC'}
,{'Etiqueta': './/Estacion_Certificada/Datos_Estacion/Sectores/Sector/Polarizacion', 'Regla': 'R_Estacion_Certificada_Datos_Estacion_Sectores_Sector_Polarizacion', 'Comparacion': 'Se comprueba con el DATASHEET de la antena'}
,{'Etiqueta': './/Estacion_Certificada/Datos_Estacion/Sectores/Sector/Altura_Antena_Sobre_Terreno', 'Regla': 'R_Estacion_Certificada_Datos_Estacion_Sectores_Sector_Altura_Antena_Sobre_Terreno', 'Comparacion': 'Se compara con dato del CAB'}
,{'Etiqueta': './/Estacion_Certificada/Datos_Estacion/Sectores/Sector/Inclinacion_Haz_Sobre_Horizontal', 'Regla': 'R_Estacion_Certificada_Datos_Estacion_Sectores_Sector_Inclinacion_Haz_Sobre_Horizontal', 'Comparacion': 'Se compara con dato del CAB'}
,{'Etiqueta': './/Estacion_Certificada/Datos_Estacion/Sectores/Sector/Antena_Directiva/Tipo_Ganancia', 'Regla': 'R_Estacion_Certificada_Datos_Estacion_Sectores_Sector_Antena_Directiva_Tipo_Ganancia', 'Comparacion': 'Se comprueba dentro del XML, ISO'}
,{'Etiqueta': './/Estacion_Certificada/Datos_Estacion/Sectores/Sector/Antena_Directiva/Ganancia_Antena', 'Regla': 'R_Estacion_Certificada_Datos_Estacion_Sectores_Sector_Antena_Directiva_Ganancia_Antena', 'Comparacion': 'Se comprueba con el DATASHEET de la antena'}
,{'Etiqueta': './/Estacion_Certificada/Datos_Estacion/Sectores/Sector/Antena_Directiva/Apertura_Horizontal_Haz', 'Regla': 'R_Estacion_Certificada_Datos_Estacion_Sectores_Sector_Antena_Directiva_Apertura_Horizontal_Haz', 'Comparacion': 'Se comprueba con el DATASHEET de la antena'}
,{'Etiqueta': './/Estacion_Certificada/Datos_Estacion/Sectores/Sector/Antena_Directiva/Apertura_Vertical_Haz', 'Regla': 'R_Estacion_Certificada_Datos_Estacion_Sectores_Sector_Antena_Directiva_Apertura_Vertical_Haz', 'Comparacion': 'Se comprueba con el DATASHEET de la antena'}
,{'Etiqueta': './/Estacion_Certificada/Datos_Estacion/Sectores/Sector/Antena_Directiva/Acimut_Maxima_Radiacion', 'Regla': 'R_Estacion_Certificada_Datos_Estacion_Sectores_Sector_Antena_Directiva_Acimut_Maxima_Radiacion', 'Comparacion': 'Se comprueba con el diseño CAP/FSC'}
,{'Etiqueta': './/Estacion_Certificada/Datos_Estacion/Sectores/Sector/Antena_Directiva/Nivel_Lobulos_Secundarios', 'Regla': 'R_Estacion_Certificada_Datos_Estacion_Sectores_Sector_Antena_Directiva_Nivel_Lobulos_Secundarios', 'Comparacion': 'Se comprueba con el DATASHEET de la antena'}
,{'Etiqueta': './/Estacion_Certificada/Datos_Estacion/Sectores/Sector/Volumen_Referencia/Forma_Volumen', 'Regla': 'R_Estacion_Certificada_Datos_Estacion_Sectores_Sector_Volumen_Referencia_Forma_Volumen', 'Comparacion': 'Se comprueba dentro del XML,se comprueba si es una forma de volumen correcta'}
,{'Etiqueta': './/Estacion_Certificada/Datos_Estacion/Sectores/Sector/Volumen_Referencia/Distancia_Referencia', 'Regla': 'R_Estacion_Certificada_Datos_Estacion_Sectores_Sector_Volumen_Referencia_Distancia_Referencia', 'Comparacion': 'Se buscar y compara con LM1 de la tabla de volumenes compuestos del PDF del certificado radioelectrico'}
,{'Etiqueta': './/Estacion_Certificada/Datos_Estacion/Sectores/Sector/Volumen_Referencia/Coeficiente_Reflexion', 'Regla': 'R_Estacion_Certificada_Datos_Estacion_Sectores_Sector_Volumen_Referencia_Coeficiente_Reflexion', 'Comparacion': 'Se busca y compara el dato con el coeficiente presente en el PDF'}
,{'Etiqueta': './/Informe_Medidas/Puntos_Medida/Punto_Medida/IdPunto', 'Regla': 'R_Informe_Medidas_Puntos_Medida_Punto_Medida_IdPunto', 'Comparacion': 'Se comprueba dentro del XML, numero entero no repetido y consecutivo'}
,{'Etiqueta': './/Informe_Medidas/Puntos_Medida/Punto_Medida/Distancia', 'Regla': 'R_Informe_Medidas_Puntos_Medida_Punto_Medida_Distancia', 'Comparacion': 'Se comprueba dentro del XML,debe estar llenado y entre 0 y 100 metros'}
,{'Etiqueta': './/Informe_Medidas/Puntos_Medida/Punto_Medida/Acimut', 'Regla': 'R_Informe_Medidas_Puntos_Medida_Punto_Medida_Acimut', 'Comparacion': 'Se comprueba dentro del XML, debe estar llenado y entre 0 y 359 grados'}
,{'Etiqueta': './/Informe_Medidas/Puntos_Medida/Punto_Medida/Punto_Sensible/Situacion', 'Regla': 'R_Informe_Medidas_Puntos_Medida_Punto_Medida_Punto_Sensible_Situacion', 'Comparacion': 'Debe coincidir con datos del PDF del certificado'}
,{'Etiqueta': './/Informe_Medidas/Puntos_Medida/Punto_Medida/Punto_Sensible/Tipo_Espacio_Sensible', 'Regla': 'R_Informe_Medidas_Puntos_Medida_Punto_Medida_Punto_Sensible_Tipo_Espacio_Sensible', 'Comparacion': 'Debe coincidir con datos del PDF del certificado'}
,{'Etiqueta': './/Informe_Medidas/Puntos_Medida/Punto_Medida/Punto_Sensible/Tipo_Via', 'Regla': 'R_Informe_Medidas_Puntos_Medida_Punto_Medida_Punto_Sensible_Tipo_Via', 'Comparacion': 'Debe coincidir con datos del PDF del certificado'}
,{'Etiqueta': './/Informe_Medidas/Puntos_Medida/Punto_Medida/Punto_Sensible/Nombre_Via', 'Regla': 'R_Informe_Medidas_Puntos_Medida_Punto_Medida_Punto_Sensible_Nombre_Via', 'Comparacion': 'Debe coincidir con datos del PDF del certificado'}
,{'Etiqueta': './/Informe_Medidas/Puntos_Medida/Punto_Medida/Punto_Sensible/Numero_Portal', 'Regla': 'R_Informe_Medidas_Puntos_Medida_Punto_Medida_Punto_Sensible_Numero_Portal', 'Comparacion': 'Debe coincidir con datos del PDF del certificado'}
,{'Etiqueta': './/Informe_Medidas/Puntos_Medida/Punto_Medida/Punto_Sensible/Codigo_Postal', 'Regla': 'R_Informe_Medidas_Puntos_Medida_Punto_Medida_Punto_Sensible_Codigo_Postal', 'Comparacion': 'Debe coincidir con datos del PDF del certificado'}
,{'Etiqueta': './/Informe_Medidas/Puntos_Medida/Punto_Medida/Punto_Sensible/Poblacion', 'Regla': 'R_Informe_Medidas_Puntos_Medida_Punto_Medida_Punto_Sensible_Poblacion', 'Comparacion': 'Debe coincidir con datos del PDF del certificado'}
,{'Etiqueta': './/Informe_Medidas/Puntos_Medida/Punto_Medida/Punto_Sensible/Cod_INE_Termino_Municipal', 'Regla': 'R_Informe_Medidas_Puntos_Medida_Punto_Medida_Punto_Sensible_Cod_INE_Termino_Municipal', 'Comparacion': 'Debe coincidir con datos del PDF del certificado'}
,{'Etiqueta': './/Informe_Medidas/Puntos_Medida/Punto_Medida/Punto_Sensible/Cod_INE_Provincia', 'Regla': 'R_Informe_Medidas_Puntos_Medida_Punto_Medida_Punto_Sensible_Cod_INE_Provincia', 'Comparacion': 'Debe coincidir con datos del PDF del certificado'}
,{'Etiqueta': './/Informe_Medidas/Informe_Medidas_Fase1/Datos_Medicion/Tecnico_Responsable', 'Regla': 'R_Informe_Medidas_Informe_Medidas_Fase1_Datos_Medicion_Tecnico_Responsable', 'Comparacion': 'Se comprueba dentro del XML,debe ser el DNI concatenado con el nombre completo del técnico.'}
,{'Etiqueta': './/Informe_Medidas/Informe_Medidas_Fase1/Datos_Medicion/Fecha_Medicion', 'Regla': 'R_Informe_Medidas_Informe_Medidas_Fase1_Datos_Medicion_Fecha_Medicion', 'Comparacion': 'Se comprueba dentro del xml, la fecha de medición caduca cada tres meses.'}
,{'Etiqueta': './/Informe_Medidas/Informe_Medidas_Fase1/Equipos_Medida_Fase1/Equipo_Medida_Fase1/IdEquipo', 'Regla': 'R_Informe_Medidas_Informe_Medidas_Fase1_Equipos_Medida_Fase1_Equipo_Medida_Fase1_IdEquipo', 'Comparacion': 'Se comprueba dentro del xml, normalmente cero'}
,{'Etiqueta': './/Informe_Medidas/Informe_Medidas_Fase1/Equipos_Medida_Fase1/Equipo_Medida_Fase1/Fecha_Ultima_Calibracion', 'Regla': 'R_Informe_Medidas_Informe_Medidas_Fase1_Equipos_Medida_Fase1_Equipo_Medida_Fase1_Fecha_Ultima_Calibracion', 'Comparacion': 'Se compara el dato con el Certificado de Calibracion en PDF'}
,{'Etiqueta': './/Informe_Medidas/Informe_Medidas_Fase1/Equipos_Medida_Fase1/Equipo_Medida_Fase1/Umbral_Deteccion_Vm', 'Regla': 'R_Informe_Medidas_Informe_Medidas_Fase1_Equipos_Medida_Fase1_Equipo_Medida_Fase1_Umbral_Deteccion_Vm', 'Comparacion': 'Se compara con PDF adjunto con mismo nombre que xml'}
,{'Etiqueta': './/Informe_Medidas/Informe_Medidas_Fase1/Equipos_Medida_Fase1/Equipo_Medida_Fase1/Longitud_Cable', 'Regla': 'R_Informe_Medidas_Informe_Medidas_Fase1_Equipos_Medida_Fase1_Equipo_Medida_Fase1_Longitud_Cable', 'Comparacion': 'Se comprueba dentro del xml, es un valor numero'}
,{'Etiqueta': './/Informe_Medidas/Informe_Medidas_Fase1/Equipos_Medida_Fase1/Equipo_Medida_Fase1/Medidor/Marca_Medidor', 'Regla': 'R_Informe_Medidas_Informe_Medidas_Fase1_Equipos_Medida_Fase1_Equipo_Medida_Fase1_Medidor_Marca_Medidor', 'Comparacion': 'Se compara el dato con el Certificado de Calibracion en PDF'}
,{'Etiqueta': './/Informe_Medidas/Informe_Medidas_Fase1/Equipos_Medida_Fase1/Equipo_Medida_Fase1/Medidor/Modelo_Medidor', 'Regla': 'R_Informe_Medidas_Informe_Medidas_Fase1_Equipos_Medida_Fase1_Equipo_Medida_Fase1_Medidor_Modelo_Medidor', 'Comparacion': 'Se compara el dato con el Certificado de Calibracion en PDF'}
,{'Etiqueta': './/Informe_Medidas/Informe_Medidas_Fase1/Equipos_Medida_Fase1/Equipo_Medida_Fase1/Medidor/Numero_Serie_Medidor', 'Regla': 'R_Informe_Medidas_Informe_Medidas_Fase1_Equipos_Medida_Fase1_Equipo_Medida_Fase1_Medidor_Numero_Serie_Medidor', 'Comparacion': 'Se compara el dato con el Certificado de Calibracion en PDF'}
,{'Etiqueta': './/Informe_Medidas/Informe_Medidas_Fase1/Equipos_Medida_Fase1/Equipo_Medida_Fase1/Antena/Marca_Antena', 'Regla': 'R_Informe_Medidas_Informe_Medidas_Fase1_Equipos_Medida_Fase1_Equipo_Medida_Fase1_Antena_Marca_Antena', 'Comparacion': 'Se compara el dato con el Certificado de Calibracion en PDF'}
,{'Etiqueta': './/Informe_Medidas/Informe_Medidas_Fase1/Equipos_Medida_Fase1/Equipo_Medida_Fase1/Antena/Modelo_Antena', 'Regla': 'R_Informe_Medidas_Informe_Medidas_Fase1_Equipos_Medida_Fase1_Equipo_Medida_Fase1_Antena_Modelo_Antena', 'Comparacion': 'Se compara el dato con el Certificado de Calibracion en PDF'}
,{'Etiqueta': './/Informe_Medidas/Informe_Medidas_Fase1/Equipos_Medida_Fase1/Equipo_Medida_Fase1/Antena/Numero_Serie_Antena', 'Regla': 'R_Informe_Medidas_Informe_Medidas_Fase1_Equipos_Medida_Fase1_Equipo_Medida_Fase1_Antena_Numero_Serie_Antena', 'Comparacion': 'Se compara el dato con el Certificado de Calibracion en PDF'}
,{'Etiqueta': './/Informe_Medidas/Informe_Medidas_Fase1/Medicion_Fase1/Medida_Fase1/IdPunto', 'Regla': 'R_Informe_Medidas_Informe_Medidas_Fase1_Medicion_Fase1_Medida_Fase1_IdPunto', 'Comparacion': 'Se comprueba dentro del xml, se nmera el punto de medida'}
,{'Etiqueta': './/Informe_Medidas/Informe_Medidas_Fase1/Medicion_Fase1/Medida_Fase1/IdEquipo', 'Regla': 'R_Informe_Medidas_Informe_Medidas_Fase1_Medicion_Fase1_Medida_Fase1_IdEquipo', 'Comparacion': 'Se comprueba dentro del xml, coincide con la del equipo usando'}
,{'Etiqueta': './/Informe_Medidas/Informe_Medidas_Fase1/Medicion_Fase1/Medida_Fase1/Hora_Inicio_Medicion', 'Regla': 'R_Informe_Medidas_Informe_Medidas_Fase1_Medicion_Fase1_Medida_Fase1_Hora_Inicio_Medicion', 'Comparacion': 'Se comprueba dentro del xml, minimo 7 minutos de diferencia de una medida a otra'}
,{'Etiqueta': './/Informe_Medidas/Informe_Medidas_Fase1/Medicion_Fase1/Medida_Fase1/Nivel_Referencia_Vm', 'Regla': 'R_Informe_Medidas_Informe_Medidas_Fase1_Medicion_Fase1_Medida_Fase1_Nivel_Referencia_Vm', 'Comparacion': 'Se comprueba el fichero de referencia pdf y se usa la frecuencia mas baja del emplazamiento'}
,{'Etiqueta': './/Informe_Medidas/Informe_Medidas_Fase1/Medicion_Fase1/Medida_Fase1/Nivel_Decision_Vm', 'Regla': 'R_Informe_Medidas_Informe_Medidas_Fase1_Medicion_Fase1_Medida_Fase1_Nivel_Decision_Vm', 'Comparacion': 'Se comprueba dentro del xml, mitad del nivel de referencia'}
,{'Etiqueta': './/Informe_Medidas/Informe_Medidas_Fase1/Medicion_Fase1/Medida_Fase1/Valor_Medido_Promediado_Vm', 'Regla': 'R_Informe_Medidas_Informe_Medidas_Fase1_Medicion_Fase1_Medida_Fase1_Valor_Medido_Promediado_Vm', 'Comparacion': 'Se comprueba dentro del xml, numero menor que humbral'}
,{'Etiqueta': './/Informe_Medidas/Informe_Medidas_Fase1/Medicion_Fase1/Medida_Fase1/Valor_Calculado_Vm', 'Regla': 'R_Informe_Medidas_Informe_Medidas_Fase1_Medicion_Fase1_Medida_Fase1_Valor_Calculado_Vm', 'Comparacion': 'Se comprueba dentro del xml, mayor que valor promedio'}
,{'Etiqueta': './/Informe_Medidas/Informe_Medidas_Fase1/Medicion_Fase1/Medida_Fase1/Diferencia_Vm', 'Regla': 'R_Informe_Medidas_Informe_Medidas_Fase1_Medicion_Fase1_Medida_Fase1_Diferencia_Vm', 'Comparacion': 'Se comprueba dentro del xml'}
,{'Etiqueta': './/Documentos/Informacion_Adicional/Documento/Nombre', 'Regla': 'R_Documentos_Informacion_Adicional_Documento_Nombre', 'Comparacion': ''}
,{'Etiqueta': './/Documentos/Informacion_Adicional/Documento/Extension', 'Regla': 'R_Documentos_Informacion_Adicional_Documento_Extension', 'Comparacion': ''}
,{'Etiqueta': './/Documentos/Informacion_Adicional/Documento/Codificacion', 'Regla': 'R_Documentos_Informacion_Adicional_Documento_Codificacion', 'Comparacion': ''}
,{'Etiqueta': './/Documentos/Informacion_Adicional/Documento/Contenido', 'Regla': 'R_Documentos_Informacion_Adicional_Documento_Contenido', 'Comparacion': ''}


]

expediente_concesional = [
    {'G': '2G', 'TECNOLOGIA': 'GSM 900', 'LETRA': 'E', 'EXPEDIENTE': 'DGZZ-1200436'}
    , {'G': '2G', 'TECNOLOGIA': 'DCS (GSM1800)', 'LETRA': 'R', 'EXPEDIENTE': ''}
    , {'G': '3G', 'TECNOLOGIA': 'UMTS 900', 'LETRA': 'F', 'EXPEDIENTE': 'DGZZ-1104544'}
    , {'G': '3G', 'TECNOLOGIA': 'UMTS 2100', 'LETRA': 'B', 'EXPEDIENTE': 'M ZZ-0020004'}
    , {'G': '4G', 'TECNOLOGIA': 'LTE 800', 'LETRA': 'M', 'EXPEDIENTE': 'DGZZ-1400353'}
    , {'G': '4G', 'TECNOLOGIA': 'LTE 1800', 'LETRA': 'N', 'EXPEDIENTE': 'DGZZ-1300380'}
    , {'G': '4G', 'TECNOLOGIA': 'LTE 2100', 'LETRA': 'T', 'EXPEDIENTE': 'DGZZ-1601470'}
    , {'G': '4G', 'TECNOLOGIA': 'LTE 2600', 'LETRA': 'L', 'EXPEDIENTE': 'DGZZ-1105021'}
]

tabla_tecnologias = [
    {'TECNOLOGIA': 'UMTS', 'OTRAS': 'LTE|GSM'}
    , {'TECNOLOGIA': 'LTE', 'OTRAS': 'UMTS|GSM'}
    , {'TECNOLOGIA':'GSM', 'OTRAS': 'LTE|UMTS'}
]
