import os
from Interfaz import Ventana_Principal
from principal import listas_comunes

def valida_tipo_solicitud(Array_Ventana):
    tipo = "MOD"
    tec = ""
    TImplantar = Array_Ventana[0]
    for tecnologia in TImplantar:
        if TImplantar[tecnologia]>0:
            tipo = "ALT"
            tec = tecnologia
            break
    for tecnologia in Array_Ventana[1]:
        if Array_Ventana[1][tecnologia]>0:
            tipo = "MOD"
            tec = tecnologia
            break
    return tipo, tec

def valida_emplazamiento_compartido(Array_Ventana):
    EmplazamientoSectores = Array_Ventana[2]
    return EmplazamientoSectores["Emplazamiento_Compartido"]


def antena_exterior(Array_Ventana, dsector):
    vexterior=""
    try:
        for sector in Array_Ventana[3]:
            if sector.upper() == dsector.upper():
                vexterior =Array_Ventana[3][sector]
    except Exception as err:
        pass
    return vexterior

def antena_interior(Array_Ventana, dsector):
    vinterior=""
    try:
        for sector in Array_Ventana[4]:
            if sector.upper() == dsector.upper():
                vinterior =Array_Ventana[4][sector]
    except Exception as err:
        pass
    return vinterior

def valida_tipo_sistema(Array_Ventana):
    tipo_sistema=""
    try:
        tipo_solicitud, tecnologia = valida_tipo_solicitud(Array_Ventana)
        tipo_sistema = listas_comunes.letra_tecnologias[tecnologia]
    except Exception as err:
        pass
    return tipo_sistema

def cantidad_sectores(Array_Ventana, i):
    cantidad = '0'
    #print(Array_Ventana[3])
    try:
        for sector in Array_Ventana[i]:
            if Array_Ventana[i][sector] == 1:
                cantidad = sector[len(sector)-1]
    except Exception as err:
        pass
    return cantidad

def modelo_antena_old(Array_Ventana):
    vmodelo=""
    try:
        for modelo in Array_Ventana[6]:
            if Array_Ventana[6][modelo] != "":
                vmodelo = Array_Ventana[6][modelo]
                break
    except Exception as err:
        pass
    return vmodelo

def altura_antena(Array_Ventana, dsector):
    valtura=""
    try:
        for sector in Array_Ventana[7]:
            if sector.upper() == dsector.upper():
                valtura =Array_Ventana[7][sector]
                # if Array_Ventana[7][sector] != "":
                #     valtura = Array_Ventana[7][sector]
                #     break
    except Exception as err:
        pass
    return valtura

def azimut_antena(Array_Ventana, dsector):
    vazimut=""
    try:
        for sector in Array_Ventana[5]:
            if sector.upper() == dsector.upper():
                vazimut =Array_Ventana[5][sector]
    except Exception as err:
        pass
    return vazimut

def modelo_antena(Array_Ventana, dsector):
    vmodelo=""
    try:
        for sector in Array_Ventana[6]:
            if sector.upper() == dsector.upper():
                vmodelo =Array_Ventana[6][sector]
    except Exception as err:
        pass
    return vmodelo

def tils_mayor_valor(Array_Ventana, dsector):
    valores = []
    try:
        for i in range(8,17):
            #print(i)
            for sector in Array_Ventana[i]:
                if sector.upper() == dsector.upper():
                    try:
                        if Array_Ventana[i][sector] == '':
                            datotil = 0
                        else:
                            datotil = Array_Ventana[i][sector]
                        valores.append(float(datotil))
                    except Exception as er0:
                        print("No es posible convertir a número el dato: " + Array_Ventana[i][sector])
        #print(valores)
    except Exception as err:
        pass
    return max(valores)

def tecnologia_implantar(Array_Ventana, dsector):
    vdato=""
    try:
        for sector in Array_Ventana[0]:
            if sector.upper() == dsector.upper():
                vdato =Array_Ventana[0][sector]
    except Exception as err:
        pass
    return vdato


#Bandera_Ventana, Array_Ventana = Ventana_Principal.ventana("")
#
# r = cantidad_sectores(Array_Ventana,3)
# print(r)
#
#rr = valida_tipo_solicitud(Array_Ventana)
#print(rr)
