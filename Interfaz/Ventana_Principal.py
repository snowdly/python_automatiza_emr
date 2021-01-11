import tkinter as tk
import tkinter.font as tkFont
from tkinter.ttk import Combobox
from tkinter import messagebox
from principal import base_datos

# variables matrices
DatosVentana = []
DTImplantar =	{
                          "DTI_G900": 0,
                          "DTI_G1800": 0,
                          "DTI_U900": 0,
                          "DTI_U2100": 0,
                          "DTI_L800": 0,
                          "DTI_L1800": 0,
                        "DTI_L2100": 0,
                        "DTI_L2600": 0,
                        "DTI_5G": 0
                        }
DTPosterior = {
            "DTP_G900": 0,
            "DTP_G1800": 0,
            "DTP_U900": 0,
            "DTP_U2100": 0,
            "DTP_L800": 0,
            "DTP_L1800": 0,
            "DTP_L2100": 0,
            "DTP_L2600": 0,
            "DTP_5G": 0
        }
DEmplazamientoSectores ={
    "Emplazamiento_Compartido" : "",
    "Numero_Sectores" : ""
}
DAntenaExterior = {
            "Sector1": 0,
            "Sector2": 0,
            "Sector3": 0,
            "sector4": 0
}
DAntenaInterior = {
            "Sector1": 0,
            "Sector2": 0,
            "Sector3": 0,
            "sector4": 0
}
DAzimut = {
            "Sector1": "",
            "Sector2": "",
            "Sector3": "",
            "sector4": ""
}
DModeloAntena = {
            "Sector1": "",
            "Sector2": "",
            "Sector3": "",
            "sector4": ""
}
DAlturaAntena = {
            "Sector1": "",
            "Sector2": "",
            "Sector3": "",
            "sector4": ""
}
DTiltsG900 = {
            "Sector1": "",
            "Sector2": "",
            "Sector3": "",
            "sector4": ""
}
DTiltsG1800 = {
            "Sector1": "",
            "Sector2": "",
            "Sector3": "",
            "sector4": ""
}
DTiltsU900 = {
            "Sector1": "",
            "Sector2": "",
            "Sector3": "",
            "sector4": ""
}
DTiltsU2100 = {
            "Sector1": "",
            "Sector2": "",
            "Sector3": "",
            "sector4": ""
}
DTiltsL800 = {
            "Sector1": "",
            "Sector2": "",
            "Sector3": "",
            "sector4": ""
}
DTiltsL1800 = {
            "Sector1": "",
            "Sector2": "",
            "Sector3": "",
            "sector4": ""
}
DTiltsL2100 = {
            "Sector1": "",
            "Sector2": "",
            "Sector3": "",
            "sector4": ""
}
DTiltsL2600 = {
            "Sector1": "",
            "Sector2": "",
            "Sector3": "",
            "sector4": ""
}
DTiltsG5 = {
            "Sector1": "",
            "Sector2": "",
            "Sector3": "",
            "sector4": ""
}
Bandera_Principal = "OK"
Continuar_Proceso = False

def ventana(Fichero_Auditoria):
    # Validaciones iniciales
    prueba_bd = base_datos.prueba_conectividad()
    if prueba_bd["Conectividad"] == "KO":
        print("Conectividad con Base de Datos: " + prueba_bd["Error"])
    else:
        # Creacion de ventana principal
        Continuar_Proceso = True
        root = tk.Tk()
        root.title("Automatización Auditorias EMR - Fichero: " + Fichero_Auditoria)
        width=870
        height=840
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        # LabelFrame general
        ftl = tkFont.Font(family='Times', size=13)
        labelframe = tk.LabelFrame(root, text='Ingresar datos... ' +  Fichero_Auditoria, font=ftl)
        labelframe.pack(expand='yes', fill='both')
        ft = tkFont.Font(family='Times', size=12)


        # Label frame Tecnologias a Implantar
        labelframeTI = tk.LabelFrame(labelframe, text='Tecnologías a Implantar', width=850, height=70, font=ftl)
        labelframeTI.grid(padx=3, pady=25)


        #TECNOLOGIAS A IMPLANTAR
        check_G900I = tk.IntVar()
        def GCheckBox_G900I_command():
            if check_G900I.get():
                print('Checkbox 1 selected')
                DTImplantar["DTI_G900"] = 1
                print(DTImplantar)
            else:
                DTImplantar["DTI_G900"] = 0
        GCheckBox_G900I = tk.Checkbutton(labelframeTI)
        GCheckBox_G900I["variable"] = check_G900I
        GCheckBox_G900I["font"] = ft
        GCheckBox_G900I["fg"] = "#333333"
        GCheckBox_G900I["justify"] = "center"
        GCheckBox_G900I["text"] = "G900"
        GCheckBox_G900I.place(x=10, y=10, width=70, height=25)
        GCheckBox_G900I["offvalue"] = "0"
        GCheckBox_G900I["onvalue"] = "1"
        GCheckBox_G900I["command"] = GCheckBox_G900I_command

        check_G1800I = tk.IntVar()
        def GCheckBox_G1800I_command():
            if check_G1800I.get():
                DTImplantar["DTI_G1800"] = 1
            else:
                DTImplantar["DTI_G1800"] = 0
        GCheckBox_G1800I = tk.Checkbutton(labelframeTI)
        GCheckBox_G1800I["variable"] = check_G1800I
        GCheckBox_G1800I["font"] = ft
        GCheckBox_G1800I["fg"] = "#333333"
        GCheckBox_G1800I["justify"] = "center"
        GCheckBox_G1800I["text"] = "G1800"
        GCheckBox_G1800I.place(x=90, y=10, width=70, height=25)
        GCheckBox_G1800I["offvalue"] = "0"
        GCheckBox_G1800I["onvalue"] = "1"
        GCheckBox_G1800I["command"] = GCheckBox_G1800I_command

        check_U900I = tk.IntVar()
        def GCheckBox_U900I_command():
            if check_U900I.get():
                DTImplantar["DTI_U900"] = 1
            else:
                DTImplantar["DTI_U900"] = 0
        GCheckBox_U900I = tk.Checkbutton(labelframeTI)
        GCheckBox_U900I["variable"] = check_U900I
        GCheckBox_U900I["font"] = ft
        GCheckBox_U900I["fg"] = "#333333"
        GCheckBox_U900I["justify"] = "center"
        GCheckBox_U900I["text"] = "U900"
        GCheckBox_U900I.place(x=160, y=10, width=70, height=25)
        GCheckBox_U900I["offvalue"] = "0"
        GCheckBox_U900I["onvalue"] = "1"
        GCheckBox_U900I["command"] = GCheckBox_U900I_command

        check_U2100I = tk.IntVar()
        def GCheckBox_U2100I_command():
            if check_U2100I.get():
                DTImplantar["DTI_U2100"] = 1
            else:
                DTImplantar["DTI_U2100"] = 0
        GCheckBox_U2100I = tk.Checkbutton(labelframeTI)
        GCheckBox_U2100I["variable"] = check_U2100I
        GCheckBox_U2100I["font"] = ft
        GCheckBox_U2100I["fg"] = "#333333"
        GCheckBox_U2100I["justify"] = "center"
        GCheckBox_U2100I["text"] = "U2100"
        GCheckBox_U2100I.place(x=240, y=10, width=70, height=25)
        GCheckBox_U2100I["offvalue"] = "0"
        GCheckBox_U2100I["onvalue"] = "1"
        GCheckBox_U2100I["command"] = GCheckBox_U2100I_command

        check_L800I = tk.IntVar()
        def GCheckBox_L800I_command():
            if check_L800I.get():
                DTImplantar["DTI_L800"] = 1
            else:
                DTImplantar["DTI_L800"] = 0
        GCheckBox_L800I = tk.Checkbutton(labelframeTI)
        GCheckBox_L800I["variable"] = check_L800I
        GCheckBox_L800I["font"] = ft
        GCheckBox_L800I["fg"] = "#333333"
        GCheckBox_L800I["justify"] = "center"
        GCheckBox_L800I["text"] = "L800"
        GCheckBox_L800I.place(x=320, y=10, width=70, height=25)
        GCheckBox_L800I["offvalue"] = "0"
        GCheckBox_L800I["onvalue"] = "1"
        GCheckBox_L800I["command"] = GCheckBox_L800I_command

        check_L1800I = tk.IntVar()
        def GCheckBox_L1800I_command():
            if check_L1800I.get():
                DTImplantar["DTI_L1800"] = 1
            else:
                DTImplantar["DTI_L1800"] = 0
        GCheckBox_L1800I = tk.Checkbutton(labelframeTI)
        GCheckBox_L1800I["variable"] = check_L1800I
        GCheckBox_L1800I["font"] = ft
        GCheckBox_L1800I["fg"] = "#333333"
        GCheckBox_L1800I["justify"] = "center"
        GCheckBox_L1800I["text"] = "L1800"
        GCheckBox_L1800I.place(x=400, y=10, width=70, height=25)
        GCheckBox_L1800I["offvalue"] = "0"
        GCheckBox_L1800I["onvalue"] = "1"
        GCheckBox_L1800I["command"] = GCheckBox_L1800I_command

        check_L2100I = tk.IntVar()
        def GCheckBox_L2100I_command():
            if check_L2100I.get():
                DTImplantar["DTI_L2100"] = 1
                print(DTImplantar)
            else:
                DTImplantar["DTI_L2100"] = 0
        GCheckBox_L2100I = tk.Checkbutton(labelframeTI)
        GCheckBox_L2100I["variable"] = check_L2100I
        GCheckBox_L2100I["font"] = ft
        GCheckBox_L2100I["fg"] = "#333333"
        GCheckBox_L2100I["justify"] = "center"
        GCheckBox_L2100I["text"] = "L2100"
        GCheckBox_L2100I.place(x=480, y=10, width=70, height=25)
        GCheckBox_L2100I["offvalue"] = "0"
        GCheckBox_L2100I["onvalue"] = "1"
        GCheckBox_L2100I["command"] = GCheckBox_L2100I_command

        check_L2600I = tk.IntVar()
        def GCheckBox_L2600I_command():
            if check_L2600I.get():
                DTImplantar["DTI_L2600"] = 1
            else:
                DTImplantar["DTI_L2600"] = 0
        GCheckBox_L2600I = tk.Checkbutton(labelframeTI)
        GCheckBox_L2600I["variable"] = check_L2600I
        GCheckBox_L2600I["font"] = ft
        GCheckBox_L2600I["fg"] = "#333333"
        GCheckBox_L2600I["justify"] = "center"
        GCheckBox_L2600I["text"] = "L2600"
        GCheckBox_L2600I.place(x=560, y=10, width=70, height=25)
        GCheckBox_L2600I["offvalue"] = "0"
        GCheckBox_L2600I["onvalue"] = "1"
        GCheckBox_L2600I["command"] = GCheckBox_L2600I_command

        check_5GI = tk.IntVar()
        def GCheckBox_5GI_command():
            if check_5GI.get():
                DTImplantar["DTI_5G"] = 1
            else:
                DTImplantar["DTI_5G"] = 0
        GCheckBox_5GI = tk.Checkbutton(labelframeTI)
        GCheckBox_5GI["variable"] = check_5GI
        GCheckBox_5GI["font"] = ft
        GCheckBox_5GI["fg"] = "#333333"
        GCheckBox_5GI["justify"] = "center"
        GCheckBox_5GI["text"] = "5G"
        GCheckBox_5GI.place(x=640, y=10, width=70, height=25)
        GCheckBox_5GI["offvalue"] = "0"
        GCheckBox_5GI["onvalue"] = "1"
        GCheckBox_5GI["command"] = GCheckBox_5GI_command


        # TECNOLOGIAS POSTERIORES
        labelframeTP = tk.LabelFrame(labelframe, text='Tecnologías Posteriores', width=850, height=70, font=ftl)
        labelframeTP.grid(padx=10, pady=3)

        check_G900P = tk.IntVar()
        def GCheckBox_G900P_command():
            if check_G900P.get():
                DTPosterior["DTP_G900"] = 1
            else:
                DTPosterior["DTP_G900"] = 0
        GCheckBox_G900P = tk.Checkbutton(labelframeTP)
        GCheckBox_G900P["variable"] = check_G900P
        GCheckBox_G900P["font"] = ft
        GCheckBox_G900P["fg"] = "#333333"
        GCheckBox_G900P["justify"] = "center"
        GCheckBox_G900P["text"] = "G900"
        GCheckBox_G900P.place(x=10, y=10, width=70, height=25)
        GCheckBox_G900P["offvalue"] = "0"
        GCheckBox_G900P["onvalue"] = "1"
        GCheckBox_G900P["command"] = GCheckBox_G900P_command

        check_G1800P = tk.IntVar()
        def GCheckBox_G1800P_command():
            if check_G1800P.get():
                DTPosterior["DTP_G1800"] = 1
            else:
                DTPosterior["DTP_G1800"] = 0
        GCheckBox_G1800P = tk.Checkbutton(labelframeTP)
        GCheckBox_G1800P["variable"] = check_G1800P
        GCheckBox_G1800P["font"] = ft
        GCheckBox_G1800P["fg"] = "#333333"
        GCheckBox_G1800P["justify"] = "center"
        GCheckBox_G1800P["text"] = "G1800"
        GCheckBox_G1800P.place(x=90, y=10, width=70, height=25)
        GCheckBox_G1800P["offvalue"] = "0"
        GCheckBox_G1800P["onvalue"] = "1"
        GCheckBox_G1800P["variable"] = "1"
        GCheckBox_G1800P["command"] = GCheckBox_G1800P_command

        check_U900P = tk.IntVar()
        def GCheckBox_U900P_command():
            if check_U900P.get():
                DTPosterior["DTP_U900"] = 1
            else:
                DTPosterior["DTP_U900"] = 0
        GCheckBox_U900P = tk.Checkbutton(labelframeTP)
        GCheckBox_U900P["variable"] = check_U900P
        GCheckBox_U900P["font"] = ft
        GCheckBox_U900P["fg"] = "#333333"
        GCheckBox_U900P["justify"] = "center"
        GCheckBox_U900P["text"] = "U900"
        GCheckBox_U900P.place(x=160, y=10, width=70, height=25)
        GCheckBox_U900P["offvalue"] = "0"
        GCheckBox_U900P["onvalue"] = "1"
        GCheckBox_U900P["command"] = GCheckBox_U900P_command

        check_U2100P = tk.IntVar()
        def GCheckBox_U2100P_command():
            if check_U2100P.get():
                DTPosterior["DTP_U2100"] = 1
            else:
                DTPosterior["DTP_U2100"] = 0
        GCheckBox_U2100P = tk.Checkbutton(labelframeTP)
        GCheckBox_U2100P["variable"] = check_U2100P
        GCheckBox_U2100P["font"] = ft
        GCheckBox_U2100P["fg"] = "#333333"
        GCheckBox_U2100P["justify"] = "center"
        GCheckBox_U2100P["text"] = "U2100"
        GCheckBox_U2100P.place(x=240, y=10, width=70, height=25)
        GCheckBox_U2100P["offvalue"] = "0"
        GCheckBox_U2100P["onvalue"] = "1"
        GCheckBox_U2100P["command"] = GCheckBox_U2100P_command

        check_L800P = tk.IntVar()
        def GCheckBox_L800P_command():
            if check_L800P.get():
                DTPosterior["DTP_L800"] = 1
            else:
                DTPosterior["DTP_L800"] = 0
        GCheckBox_L800P = tk.Checkbutton(labelframeTP)
        GCheckBox_L800P["variable"] = check_L800P
        GCheckBox_L800P["font"] = ft
        GCheckBox_L800P["fg"] = "#333333"
        GCheckBox_L800P["justify"] = "center"
        GCheckBox_L800P["text"] = "L800"
        GCheckBox_L800P.place(x=320, y=10, width=70, height=25)
        GCheckBox_L800P["offvalue"] = "0"
        GCheckBox_L800P["onvalue"] = "1"
        GCheckBox_L800P["command"] = GCheckBox_L800P_command

        check_L1800P = tk.IntVar()
        def GCheckBox_L1800P_command():
            if check_L1800P.get():
                DTPosterior["DTP_L1800"] = 1
            else:
                DTPosterior["DTP_L1800"] = 0
        GCheckBox_L1800P = tk.Checkbutton(labelframeTP)
        GCheckBox_L1800P["variable"] = check_L1800P
        GCheckBox_L1800P["font"] = ft
        GCheckBox_L1800P["fg"] = "#333333"
        GCheckBox_L1800P["justify"] = "center"
        GCheckBox_L1800P["text"] = "L1800"
        GCheckBox_L1800P.place(x=400, y=10, width=70, height=25)
        GCheckBox_L1800P["offvalue"] = "0"
        GCheckBox_L1800P["onvalue"] = "1"
        GCheckBox_L1800P["command"] = GCheckBox_L1800P_command

        check_L2100P = tk.IntVar()
        def GCheckBox_L2100P_command():
            if check_L2100P.get():
                DTPosterior["DTP_L2100"] = 1
            else:
                DTPosterior["DTP_L2100"] = 0
        GCheckBox_L2100P = tk.Checkbutton(labelframeTP)
        GCheckBox_L2100P["variable"] = check_L2100P
        GCheckBox_L2100P["font"] = ft
        GCheckBox_L2100P["fg"] = "#333333"
        GCheckBox_L2100P["justify"] = "center"
        GCheckBox_L2100P["text"] = "L2100"
        GCheckBox_L2100P.place(x=480, y=10, width=70, height=25)
        GCheckBox_L2100P["offvalue"] = "0"
        GCheckBox_L2100P["onvalue"] = "1"
        GCheckBox_L2100P["command"] = GCheckBox_L2100P_command

        check_L2600P = tk.IntVar()
        def GCheckBox_L2600P_command():
            if check_L2600P.get():
                DTPosterior["DTP_L2600"] = 1
            else:
                DTPosterior["DTP_L2600"] = 0
        GCheckBox_L2600P = tk.Checkbutton(labelframeTP)
        GCheckBox_L2600P["variable"] = check_L2600P
        GCheckBox_L2600P["font"] = ft
        GCheckBox_L2600P["fg"] = "#333333"
        GCheckBox_L2600P["justify"] = "center"
        GCheckBox_L2600P["text"] = "L2600"
        GCheckBox_L2600P.place(x=560, y=10, width=70, height=25)
        GCheckBox_L2600P["offvalue"] = "0"
        GCheckBox_L2600P["onvalue"] = "1"
        GCheckBox_L2600P["command"] = GCheckBox_L2600P_command

        check_5GP = tk.IntVar()
        def GCheckBox_5GP_command():
            if check_5GP.get():
                DTPosterior["DTP_5G"] = 1
                print(DTPosterior)
            else:
                DTPosterior["DTP_5G"] = 0
        GCheckBox_5GP = tk.Checkbutton(labelframeTP)
        GCheckBox_5GP["variable"] = check_5GP
        GCheckBox_5GP["font"] = ft
        GCheckBox_5GP["fg"] = "#333333"
        GCheckBox_5GP["justify"] = "center"
        GCheckBox_5GP["text"] = "5G"
        GCheckBox_5GP.place(x=640, y=10, width=70, height=25)
        GCheckBox_5GP["offvalue"] = "0"
        GCheckBox_5GP["onvalue"] = "1"
        GCheckBox_5GP["command"] = GCheckBox_5GP_command

        # EMPLAZAMIENTOS Y NUMERO DE SECTORES
        labelEmSe = tk.LabelFrame(labelframe, text='Emplazamiento Compartido   -   Número de sectores', width=850, height=70, font=ftl)
        labelEmSe.grid(padx=10, pady=3)
        GLabel_418=tk.Label(labelEmSe)
        GLabel_418["font"] = ft
        GLabel_418["fg"] = "#333333"
        GLabel_418["justify"] = "center"
        GLabel_418["text"] = "Emplazamiento Compartido:"
        GLabel_418.place(x=10,y=10,width=187,height=30)

        cmbEmplazamiento = Combobox(labelEmSe, width="10", values=("SI", "NO"), font = ft)
        cmbEmplazamiento.place(x=200, y=10, width=70, height=25)
        cmbEmplazamiento.current(0)

        GLabel_420=tk.Label(labelEmSe)
        GLabel_420["font"] = ft
        GLabel_420["fg"] = "#333333"
        GLabel_420["justify"] = "center"
        GLabel_420["text"] = "Número de Sectores:"
        GLabel_420.place(x=300,y=10,width=187,height=30)
        cmbSectores = Combobox(labelEmSe, width="10", values=("1", "2", "3", "4"), font = ft)
        cmbSectores.place(x=470, y=10, width=70, height=25)
        cmbSectores.current(0)

        # ANTENAS
        labelAntenas = tk.LabelFrame(labelframe, text='Antenas', width=850, height=170, font=ftl)
        labelAntenas.grid(padx=10, pady=3)
        GLabel_Antenas=tk.Label(labelAntenas, font = ftl, text="Antenas", justify = "center", bg="#FAF0E6")
        GLabel_Antenas.place(x=25,y=3,width=100,height=30)
        GLabel_Exteriores=tk.Label(labelAntenas, font = ftl, text="Exteriores", justify = "center")
        GLabel_Exteriores.place(x=25,y=23,width=150,height=30)
        GLabel_Interiores=tk.Label(labelAntenas, font = ftl, text="Interiores", justify = "center")
        GLabel_Interiores.place(x=25,y=43,width=150,height=30)
        GLabel_Azimut=tk.Label(labelAntenas, font = ftl, text="Azimut", justify = "center")
        GLabel_Azimut.place(x=25,y=63,width=150,height=30)
        GLabel_Modelo=tk.Label(labelAntenas, font = ftl, text="Modelo antena", justify = "center")
        GLabel_Modelo.place(x=25,y=63+25,width=150,height=30)
        GLabel_Altura=tk.Label(labelAntenas, font = ftl, text="Altura de antena", justify = "center")
        GLabel_Altura.place(x=25,y=63+25*2,width=150,height=30)
        GLabel_Sector1 = tk.Label(labelAntenas, font=ftl, text="Sector1", justify="center", bg="#FAF0E6")
        GLabel_Sector1.place(x=150, y=3, width=100, height=30)
        GLabel_Sector2 = tk.Label(labelAntenas, font=ftl, text="Sector2", justify="center", bg="#FAF0E6")
        GLabel_Sector2.place(x=150+130, y=3, width=100, height=30)
        GLabel_Sector3 = tk.Label(labelAntenas, font=ftl, text="Sector3", justify="center", bg="#FAF0E6")
        GLabel_Sector3.place(x=150+130*2, y=3, width=100, height=30)
        GLabel_Sector4 = tk.Label(labelAntenas, font=ftl, text="Sector4", justify="center", bg="#FAF0E6")
        GLabel_Sector4.place(x=150+130*3, y=3, width=100, height=30)

        ANEXS1 = tk.IntVar()
        def ANEXS1_command():
            DAntenaExterior["Sector1"] = 1 if ANEXS1.get() else 0
        GCheckBox_ANEXS1 = tk.Checkbutton(labelAntenas, variable=ANEXS1, font=ftl, offvalue="0", onvalue="1")
        GCheckBox_ANEXS1.place(x=160, y=23, width=70, height=25)
        GCheckBox_ANEXS1["command"] = ANEXS1_command
        ANEXS2 = tk.IntVar()
        def ANEXS2_command():
            DAntenaExterior["Sector2"] = 1 if ANEXS2.get() else 0
        GCheckBox_ANEXS2 = tk.Checkbutton(labelAntenas, variable=ANEXS2, font=ftl, offvalue="0", onvalue="1")
        GCheckBox_ANEXS2.place(x=160+130, y=23, width=70, height=25)
        GCheckBox_ANEXS2["command"] = ANEXS2_command
        ANEXS3 = tk.IntVar()
        def ANEXS3_command():
            DAntenaExterior["Sector3"] = 1 if ANEXS3.get() else 0
        GCheckBox_ANEXS3 = tk.Checkbutton(labelAntenas, variable=ANEXS3, font=ftl, offvalue="0", onvalue="1")
        GCheckBox_ANEXS3.place(x=160+130*2, y=23, width=70, height=25)
        GCheckBox_ANEXS3["command"] = ANEXS3_command
        ANEXS4 = tk.IntVar()
        def ANEXS4_command():
            DAntenaExterior["Sector4"] = 1 if ANEXS4.get() else 0
        GCheckBox_ANEXS4 = tk.Checkbutton(labelAntenas, variable=ANEXS4, font=ftl, offvalue="0", onvalue="1")
        GCheckBox_ANEXS4.place(x=160+130*3, y=23, width=70, height=25)
        GCheckBox_ANEXS4["command"] = ANEXS4_command

        ANINS1 = tk.IntVar()
        def ANINS1_command():
            DAntenaInterior["Sector1"] = 1 if ANINS1.get() else 0
        GCheckBox_ANINS1 = tk.Checkbutton(labelAntenas, variable=ANINS1, font=ftl, offvalue="0", onvalue="1")
        GCheckBox_ANINS1.place(x=160, y=43, width=70, height=25)
        GCheckBox_ANINS1["command"] = ANINS1_command
        ANINS2 = tk.IntVar()
        def ANINS2_command():
            DAntenaInterior["Sector2"] = 1 if ANINS2.get() else 0
        GCheckBox_ANINS2 = tk.Checkbutton(labelAntenas, variable=ANINS2, font=ftl, offvalue="0", onvalue="1")
        GCheckBox_ANINS2.place(x=160+130, y=43, width=70, height=25)
        GCheckBox_ANINS2["command"] = ANINS2_command
        ANINS3 = tk.IntVar()
        def ANINS3_command():
            DAntenaInterior["Sector3"] = 1 if ANINS3.get() else 0
        GCheckBox_ANINS3 = tk.Checkbutton(labelAntenas, variable=ANINS3, font=ftl, offvalue="0", onvalue="1")
        GCheckBox_ANINS3.place(x=160+130*2, y=43, width=70, height=25)
        GCheckBox_ANINS3["command"] = ANINS3_command
        ANINS4 = tk.IntVar()
        def ANINS4_command():
            DAntenaInterior["Sector4"] = 1 if ANINS4.get() else 0
        GCheckBox_ANINS4 = tk.Checkbutton(labelAntenas, variable=ANINS4, font=ftl, offvalue="0", onvalue="1")
        GCheckBox_ANINS4.place(x=160+130*3, y=43, width=70, height=25)
        GCheckBox_ANINS4["command"] = ANINS4_command

        TxtAzimutS1 = tk.Entry(labelAntenas, text="", font=ftl)
        TxtAzimutS1.place(x=170, y=63, width=100, height=25)
        TxtAzimutS2 = tk.Entry(labelAntenas, text="", font=ftl)
        TxtAzimutS2.place(x=170+130, y=63, width=100, height=25)
        TxtAzimutS3 = tk.Entry(labelAntenas, text="", font=ftl)
        TxtAzimutS3.place(x=170+130*2, y=63, width=100, height=25)
        TxtAzimutS4 = tk.Entry(labelAntenas, text="", font=ftl)
        TxtAzimutS4.place(x=170+130*3, y=63, width=100, height=25)

        obtiene_antenas = base_datos.obtiene_antenas()
        if obtiene_antenas["Error"] == "":
            results_for_modeloantena = obtiene_antenas["Modelos_Antenas"]
            Continuar_Proceso = True
        else:
            results_for_modeloantena = [""]
            messagebox.showerror("Error", obtiene_antenas["Error"])
            #Continuar_Proceso = False

        fts = tkFont.Font(family='Times', size=10)
        cmbANS1 = Combobox(labelAntenas, width="10", values=results_for_modeloantena, font=fts)
        cmbANS1.place(x=170, y=63+25, width=100, height=25)
        cmbANS1.current(0)
        cmbANS2 = Combobox(labelAntenas, width="10", values=results_for_modeloantena, font=fts)
        cmbANS2.place(x=170+130, y=63 + 25, width=100, height=25)
        cmbANS2.current(0)
        cmbANS3 = Combobox(labelAntenas, width="10", values=results_for_modeloantena, font=fts)
        cmbANS3.place(x=170+130*2, y=63 + 25, width=100, height=25)
        cmbANS3.current(0)
        cmbANS4 = Combobox(labelAntenas, width="10", values=results_for_modeloantena, font=fts)
        cmbANS4.place(x=170 + 130 * 3, y=63 + 25, width=100, height=25)
        cmbANS4.current(0)

        TxtAlturaS1 = tk.Entry(labelAntenas, text="", font=ftl)
        TxtAlturaS1.place(x=170, y=63+25*2, width=100, height=25)
        TxtAlturaS2 = tk.Entry(labelAntenas, text="", font=ftl)
        TxtAlturaS2.place(x=170+130, y=63 + 25 * 2, width=100, height=25)
        TxtAlturaS3 = tk.Entry(labelAntenas, text="", font=ftl)
        TxtAlturaS3.place(x=170 + 130*2, y=63 + 25 * 2, width=100, height=25)
        TxtAlturaS4 = tk.Entry(labelAntenas, text="", font=ftl)
        TxtAlturaS4.place(x=170 + 130*3, y=63 + 25 * 2, width=100, height=25)

        # TILTS
        labelTilts = tk.LabelFrame(labelframe, text='Tilts', width=850, height=300, font=ft)
        labelTilts.grid(padx=10, pady=3)
        GLabel_Tilts = tk.Label(labelTilts, font=ft, text="Tilts", justify="center", bg="#FAF0E6")
        GLabel_Tilts.place(x=25, y=3, width=100, height=30)
        TLabel_Sector1 = tk.Label(labelTilts, font=ftl, text="Sector1", justify="center", bg="#FAF0E6")
        TLabel_Sector1.place(x=150, y=3, width=100, height=30)
        TLabel_Sector2 = tk.Label(labelTilts, font=ftl, text="Sector2", justify="center", bg="#FAF0E6")
        TLabel_Sector2.place(x=150 + 130, y=3, width=100, height=30)
        TLabel_Sector3 = tk.Label(labelTilts, font=ftl, text="Sector3", justify="center", bg="#FAF0E6")
        TLabel_Sector3.place(x=150 + 130 * 2, y=3, width=100, height=30)
        TLabel_Sector4 = tk.Label(labelTilts, font=ftl, text="Sector4", justify="center", bg="#FAF0E6")
        TLabel_Sector4.place(x=150 + 130 * 3, y=3, width=100, height=30)
        GLabel_G900 = tk.Label(labelTilts, font=ft, text="G900", justify="center")
        GLabel_G900.place(x=25, y=3+25, width=150, height=30)
        GLabel_G1800 = tk.Label(labelTilts, font=ft, text="G1800", justify="center", bg="#FAF0E6")
        GLabel_G1800.place(x=25, y=3 + 25*2, width=150, height=30)
        GLabel_U900 = tk.Label(labelTilts, font=ft, text="U900", justify="center")
        GLabel_U900.place(x=25, y=3 + 25 * 3, width=150, height=30)
        GLabel_U2100 = tk.Label(labelTilts, font=ft, text="U2100", justify="center", bg="#FAF0E6")
        GLabel_U2100.place(x=25, y=3 + 25*4, width=150, height=30)
        GLabel_L800 = tk.Label(labelTilts, font=ft, text="L800", justify="center")
        GLabel_L800.place(x=25, y=3 + 25*5, width=150, height=30)
        GLabel_L1800 = tk.Label(labelTilts, font=ft, text="L1800", justify="center", bg="#FAF0E6")
        GLabel_L1800.place(x=25, y=3 + 25*6, width=150, height=30)
        GLabel_L2100 = tk.Label(labelTilts, font=ft, text="L2100", justify="center")
        GLabel_L2100.place(x=25, y=3 + 25*7, width=150, height=30)
        GLabel_L2600 = tk.Label(labelTilts, font=ft, text="L2600", justify="center", bg="#FAF0E6")
        GLabel_L2600.place(x=25, y=3 + 25*8, width=150, height=30)
        GLabel_5G = tk.Label(labelTilts, font=ft, text="5G", justify="center")
        GLabel_5G.place(x=25, y=3 + 25 * 9, width=150, height=30)

        TxtTG900S1 = tk.Entry(labelTilts, text="", font=ftl)
        TxtTG900S1.place(x=170, y=3+25, width=100, height=25)
        TxtTG900S2 = tk.Entry(labelTilts, text="", font=ftl)
        TxtTG900S2.place(x=170 + 130, y=3+25, width=100, height=25)
        TxtTG900S3 = tk.Entry(labelTilts, text="", font=ftl)
        TxtTG900S3.place(x=170 + 130 * 2, y=3+25, width=100, height=25)
        TxtTG900S4 = tk.Entry(labelTilts, text="", font=ftl)
        TxtTG900S4.place(x=170 + 130 * 3, y=3+25, width=100, height=25)
        TxtTG1800S1 = tk.Entry(labelTilts, text="", font=ftl)
        TxtTG1800S1.place(x=170, y=3 + 25*2, width=100, height=25)
        TxtTG1800S2 = tk.Entry(labelTilts, text="", font=ftl)
        TxtTG1800S2.place(x=170 + 130, y=3 + 25*2, width=100, height=25)
        TxtTG1800S3 = tk.Entry(labelTilts, text="", font=ftl)
        TxtTG1800S3.place(x=170 + 130 * 2, y=3 + 25*2, width=100, height=25)
        TxtTG1800S4 = tk.Entry(labelTilts, text="", font=ftl)
        TxtTG1800S4.place(x=170 + 130 * 3, y=3 + 25*2, width=100, height=25)
        TxtTU900S1 = tk.Entry(labelTilts, text="", font=ftl)
        TxtTU900S1.place(x=170, y=3 + 25 * 3, width=100, height=25)
        TxtTU900S2 = tk.Entry(labelTilts, text="", font=ftl)
        TxtTU900S2.place(x=170 + 130, y=3 + 25 * 3, width=100, height=25)
        TxtTU900S3 = tk.Entry(labelTilts, text="", font=ftl)
        TxtTU900S3.place(x=170 + 130 * 2, y=3 + 25 * 3, width=100, height=25)
        TxtTU900S4 = tk.Entry(labelTilts, text="", font=ftl)
        TxtTU900S4.place(x=170 + 130 * 3, y=3 + 25 * 3, width=100, height=25)
        TxtTU21001S1 = tk.Entry(labelTilts, text="", font=ftl)
        TxtTU21001S1.place(x=170, y=3 + 25 * 4, width=100, height=25)
        TxtTU21001S2 = tk.Entry(labelTilts, text="", font=ftl)
        TxtTU21001S2.place(x=170 + 130, y=3 + 25 * 4, width=100, height=25)
        TxtTU21001S3 = tk.Entry(labelTilts, text="", font=ftl)
        TxtTU21001S3.place(x=170 + 130 * 2, y=3 + 25 * 4, width=100, height=25)
        TxtTU21001S4 = tk.Entry(labelTilts, text="", font=ftl)
        TxtTU21001S4.place(x=170 + 130 * 3, y=3 + 25 * 4, width=100, height=25)
        TxtTL800S1 = tk.Entry(labelTilts, text="", font=ftl)
        TxtTL800S1.place(x=170, y=3 + 25 * 5, width=100, height=25)
        TxtTL800S2 = tk.Entry(labelTilts, text="", font=ftl)
        TxtTL800S2.place(x=170 + 130, y=3 + 25 * 5, width=100, height=25)
        TxtTL800S3 = tk.Entry(labelTilts, text="", font=ftl)
        TxtTL800S3.place(x=170 + 130 * 2, y=3 + 25 * 5, width=100, height=25)
        TxtTL800S4 = tk.Entry(labelTilts, text="", font=ftl)
        TxtTL800S4.place(x=170 + 130 * 3, y=3 + 25 * 5, width=100, height=25)
        TxtTL1800S1 = tk.Entry(labelTilts, text="", font=ftl)
        TxtTL1800S1.place(x=170, y=3 + 25 * 6, width=100, height=25)
        TxtTL1800S2 = tk.Entry(labelTilts, text="", font=ftl)
        TxtTL1800S2.place(x=170 + 130, y=3 + 25 * 6, width=100, height=25)
        TxtTL1800S3 = tk.Entry(labelTilts, text="", font=ftl)
        TxtTL1800S3.place(x=170 + 130 * 2, y=3 + 25 * 6, width=100, height=25)
        TxtTL1800S4 = tk.Entry(labelTilts, text="", font=ftl)
        TxtTL1800S4.place(x=170 + 130 * 3, y=3 + 25 * 6, width=100, height=25)
        TxtTL2100S1 = tk.Entry(labelTilts, text="", font=ftl)
        TxtTL2100S1.place(x=170, y=3 + 25 * 7, width=100, height=25)
        TxtTL2100S2 = tk.Entry(labelTilts, text="", font=ftl)
        TxtTL2100S2.place(x=170 + 130, y=3 + 25 * 7, width=100, height=25)
        TxtTL2100S3 = tk.Entry(labelTilts, text="", font=ftl)
        TxtTL2100S3.place(x=170 + 130 * 2, y=3 + 25 * 7, width=100, height=25)
        TxtTL2100S4 = tk.Entry(labelTilts, text="", font=ftl)
        TxtTL2100S4.place(x=170 + 130 * 3, y=3 + 25 * 7, width=100, height=25)
        TxtTL2600S1 = tk.Entry(labelTilts, text="", font=ftl)
        TxtTL2600S1.place(x=170, y=3 + 25 * 8, width=100, height=25)
        TxtTL2600S2 = tk.Entry(labelTilts, text="", font=ftl)
        TxtTL2600S2.place(x=170 + 130, y=3 + 25 * 8, width=100, height=25)
        TxtTL2600S3 = tk.Entry(labelTilts, text="", font=ftl)
        TxtTL2600S3.place(x=170 + 130 * 2, y=3 + 25 * 8, width=100, height=25)
        TxtTL2600S4 = tk.Entry(labelTilts, text="", font=ftl)
        TxtTL2600S4.place(x=170 + 130 * 3, y=3 + 25 * 8, width=100, height=25)
        TxtT5GS1 = tk.Entry(labelTilts, text="", font=ftl)
        TxtT5GS1.place(x=170, y=3 + 25 * 9, width=100, height=25)
        TxtT5GS2 = tk.Entry(labelTilts, text="", font=ftl)
        TxtT5GS2.place(x=170 + 130, y=3 + 25 * 9, width=100, height=25)
        TxtT5GS3 = tk.Entry(labelTilts, text="", font=ftl)
        TxtT5GS3.place(x=170 + 130 * 2, y=3 + 25 * 9, width=100, height=25)
        TxtT5GS4 = tk.Entry(labelTilts, text="", font=ftl)
        TxtT5GS4.place(x=170 + 130 * 3, y=3 + 25 * 9, width=100, height=25)

        #BOTONES
        def asignar_valores():
            DEmplazamientoSectores["Emplazamiento_Compartido"] = cmbEmplazamiento.get()
            DEmplazamientoSectores["Numero_Sectores"] = cmbSectores.get()
            DModeloAntena["Sector1"] = cmbANS1.get()
            DModeloAntena["Sector2"] = cmbANS2.get()
            DModeloAntena["Sector3"] = cmbANS3.get()
            DModeloAntena["Sector4"] = cmbANS4.get()
            DAzimut["Sector1"] = TxtAzimutS1.get()
            DAzimut["Sector2"] = TxtAzimutS2.get()
            DAzimut["Sector2"] = TxtAzimutS2.get()
            DAzimut["Sector2"] = TxtAzimutS2.get()
            DAlturaAntena["Sector1"] = TxtAlturaS1.get()
            DAlturaAntena["Sector2"] = TxtAlturaS2.get()
            DAlturaAntena["Sector3"] = TxtAlturaS3.get()
            DAlturaAntena["Sector4"] = TxtAlturaS4.get()
            DTiltsG900["Sector1"] = TxtTG900S1.get()
            DTiltsG900["Sector2"] = TxtTG900S2.get()
            DTiltsG900["Sector3"] = TxtTG900S3.get()
            DTiltsG900["Sector4"] = TxtTG900S4.get()
            DTiltsG1800["Sector1"] = TxtTG1800S1.get()
            DTiltsG1800["Sector2"] = TxtTG1800S2.get()
            DTiltsG1800["Sector3"] = TxtTG1800S3.get()
            DTiltsG1800["Sector4"] = TxtTG1800S4.get()
            DTiltsU900["Sector1"] = TxtTU900S1.get()
            DTiltsU900["Sector1"] = TxtTU900S2.get()
            DTiltsU900["Sector3"] = TxtTU900S3.get()
            DTiltsU900["Sector4"] = TxtTU900S4.get()
            DTiltsU2100["Sector1"] = TxtTU21001S1.get()
            DTiltsU2100["Sector2"] = TxtTU21001S2.get()
            DTiltsU2100["Sector3"] = TxtTU21001S3.get()
            DTiltsU2100["Sector4"] = TxtTU21001S4.get()
            DTiltsL800["Sector1"] = TxtTL800S1.get()
            DTiltsL800["Sector2"] = TxtTL800S2.get()
            DTiltsL800["Sector3"] = TxtTL800S3.get()
            DTiltsL800["Sector4"] = TxtTL800S4.get()
            DTiltsL1800["Sector1"] = TxtTL1800S1.get()
            DTiltsL1800["Sector2"] = TxtTL1800S2.get()
            DTiltsL1800["Sector3"] = TxtTL1800S3.get()
            DTiltsL1800["Sector4"] = TxtTL1800S4.get()
            DTiltsL2100["Sector1"] = TxtTL2100S1.get()
            DTiltsL2100["Sector2"] = TxtTL2100S2.get()
            DTiltsL2100["Sector3"] = TxtTL2100S3.get()
            DTiltsL2100["Sector4"] = TxtTL2100S4.get()
            DTiltsL2600["Sector1"] = TxtTL2600S1.get()
            DTiltsL2600["Sector2"] = TxtTL2600S2.get()
            DTiltsL2600["Sector3"] = TxtTL2600S3.get()
            DTiltsL2600["Sector4"] = TxtTL2600S4.get()
            DTiltsG5["Sector1"] = TxtT5GS1.get()
            DTiltsG5["Sector2"] = TxtT5GS1.get()
            DTiltsG5["Sector3"] = TxtT5GS1.get()
            DTiltsG5["Sector4"] = TxtT5GS1.get()


        def btnAceptar_command():
            nonlocal Continuar_Proceso
            Continuar_Proceso = True
            asignar_valores()
            DatosVentana.append(DTImplantar)
            DatosVentana.append(DTPosterior)
            DatosVentana.append(DEmplazamientoSectores)
            DatosVentana.append(DAntenaExterior)
            DatosVentana.append(DAntenaInterior)
            DatosVentana.append(DAzimut)
            DatosVentana.append(DModeloAntena)
            DatosVentana.append(DAlturaAntena)
            DatosVentana.append(DTiltsG900)
            DatosVentana.append(DTiltsG1800)
            DatosVentana.append(DTiltsU900)
            DatosVentana.append(DTiltsU2100)
            DatosVentana.append(DTiltsL800)
            DatosVentana.append(DTiltsL1800)
            DatosVentana.append(DTiltsL2100)
            DatosVentana.append(DTiltsL2600)
            DatosVentana.append(DTiltsL2600)

            root.destroy()

        def btnCancelar_command():
            nonlocal Continuar_Proceso
            Continuar_Proceso = False
            root.destroy()

        btnAceptar = tk.Button(root, text="Aceptar", font=ftl, command=btnAceptar_command)
        btnAceptar.place(relx="0.3", rely="0.94")
        btnCancelar = tk.Button(root, text="Cancelar", font=ftl, command = btnCancelar_command)
        btnCancelar.place(relx="0.5", rely="0.94")

        # PROCESO PRINCIPAL
        root.mainloop()

    return Continuar_Proceso, DatosVentana


#Bandera_Ventana, Array_Ventana = ventana()