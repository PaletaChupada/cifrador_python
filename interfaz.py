from tkinter import *
from tkinter import filedialog
import tkinter as tk
import functools
from matplotlib.pyplot import text
import numpy as np

# Funcion para abrir el explorador y guardar la ruta
def browseFiles(): 
    ruta = filedialog.askopenfilename(initialdir = "D:/Documentos/ESCOM/7moSemestre/Crypto/Practica 0/", title = "Select a File", filetypes = (("Text files", "*.txt*"), ("all files", "*.*")))
    labelInfo = Label(principal, text="Ruta del archivo: ")
    labelInfo.place(x=150,y=0) 
    labelExplorador.configure(text=ruta)

# Funcion de decifrado
def secundaria_v(master,  callback=None, args=(), kwargs={}):

    # Funcion para cifrar
    def cifrar():
        ruta = labelExplorador.cget("text")
        clave = numero.get()
        clave = int(clave)
        arreglo = np.loadtxt(ruta,dtype="str", delimiter="\n")
        cadena = ""
        print(len(arreglo))
        for n in range(len(arreglo)):
            print(arreglo[n])
        # mensaje = cadena.replace(" ","")
        # mensaje.upper()
        print(clave)

    # Creamos interfaz para que el usario ingrese la clave
    if callback is not None:
        callback = functools.partial(callback, *args, **kwargs)

    main_frame = tk.Frame(master)
    labelEspacio3 = Label(main_frame, text="")
    labelClave = Label(main_frame, text="Ingresa la clave y presiona enter", height=4)
    numero = Entry(main_frame)
    buttonCifrar = Button(main_frame, text="Cifrar", command = cifrar)
    buttonRegresar = Button(main_frame, text = "Regresar", command = callback)
    labelClave.pack()
    numero.pack()
    labelEspacio3.pack()
    buttonCifrar.pack()
    buttonRegresar.pack()

    return main_frame
    

     
# Funcion para mostrar la ventana principal
def mostrar_prin():
    secundaria.pack_forget()
    principal.pack(side="top", fill="both", expand=True)

# Funcion para mostrar la ventana de cifrado
def mostrar_sec():
    buttonBuscar.pack_forget()
    principal.pack_forget()
    secundaria.pack(side="top", fill="both", expand=True)

# Creacion de la ventana y anexo de los botones y los labels                                                                                                       
root = tk.Tk() 
root.title('Practica 0 (Cifrador de Ceasar)') 
root.geometry("400x250")
root.resizable(0,0)
principal = tk.Frame(root)
labelEspacio = Label(principal, text="")
labelEspacio2 = Label(principal, text="")
labelExplorador = Label(principal, text = "Selecciona un archivo txt", height=4)    
buttonBuscar = Button(principal, text = "Buscar", command = browseFiles)
buttonCifrar = Button(principal, text = "Cifrar", command=mostrar_sec)
buttonDescifrar = Button(principal, text = "Descifrar")  
buttonSalir = Button(principal, text = "Salir", command = exit)  
labelExplorador.pack()
buttonBuscar.pack()
labelEspacio.pack()
buttonCifrar.pack()
buttonDescifrar.pack()
labelEspacio2.pack()
buttonSalir.pack()
secundaria = secundaria_v(root, mostrar_prin)
mostrar_prin()
root.mainloop() 