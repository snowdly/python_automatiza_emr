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

def modelo_antena(Array_Ventana):
    vmodelo=""
    try:
        for modelo in Array_Ventana[6]:
            if Array_Ventana[6][modelo] != "":
                vmodelo = Array_Ventana[6][modelo]
                break
    except Exception as err:
        pass
    return vmodelo


# Bandera_Ventana, Array_Ventana = Ventana_Principal.ventana()
#
# r = cantidad_sectores(Array_Ventana,3)
# print(r)
#
# rr = cantidad_sectores(Array_Ventana,4)
# print(rr)
