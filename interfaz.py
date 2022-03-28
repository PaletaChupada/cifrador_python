'''
Autor: Daniel Espinoza (@paleta_chupada)
Version: 1.0
Descripcion: Cifrador de Cesar para alfabeto en ingles (mod 26)
'''

import ntpath
from tkinter import *
from tkinter import filedialog
import tkinter as tk
import functools
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
        ruta = labelExplorador.cget("text") # Obtenemos la direccion del archivo
        nombre = str(ntpath.basename(ruta)) # Obtenemos su nombre
        ruta_aux = str(ruta).replace(nombre,"") # Eliminamos el nombre de la ruta
        nombre = nombre.replace(".txt","") # Eliminamos su extension del nombre
        clave = numero.get() 
        clave = int(clave) # Obtenemos la clave en entero que se introduce en el Entry
        arreglo = np.loadtxt(ruta,dtype="str", delimiter="\n") # Eliminamos saltos de linea y cargamos el txt en un arreglo
        cadena = ""
        for n in range(len(arreglo)):
            cadena += arreglo[n] # Llenamos el string con los valores del arreglo
        mensaje = cadena.replace(" ","")
        
        cifrado = ""

        for simbolo in mensaje:
            if simbolo.isalpha(): # isalpha devuelve si la cadena es una minuscula o mayuscula entre A y Z, si no es alfabetico, entonces isalpha regresa false
                num = ord(simbolo)
                num += clave # Sumamos el corrimiento de la clave
                if simbolo.isupper(): # Preguntamos si es mayuscula
                    if num>ord('Z'): # Funcion ord devuelve el unicode de un caracter, si numero es mayor le restamos 26 (letras en el alfabeto) 
                                    #a numero para obtener el caracter con el corrimientod de la clave, este numero es ya que si es mayor a Z tenemos que meterlo en el rango de caracteres
                        num-=26
                    elif num<ord('A'): # Hacemos lo mismo para la A, en este caso se suma 26 para meterlo en el rango
                        num+=26
                elif simbolo.islower(): # Preguntamos si es minuscula y hacemos el mismo procedimiento de arriba
                    if num>ord('z'):
                        num-=26
                    elif num<ord('a'):
                        num+=26
                cifrado+=chr(num)

        cifrado = cifrado.upper() # Convertimos todo a mayusculas
        archivo_c = open(ruta_aux+nombre+"_C.txt","w") # Cremos el txt
        archivo_c.write(cifrado) # Escribimos el cifrado
        archivo_c.close() # Cerramos el archivo
        print("Mensaje Cifrado")

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

def tercera_v(master,  callback=None, args=(), kwargs={}):
    
    # Funcion para descifrar
    def decifrar():
        ruta = labelExplorador.cget("text") # Obtenemos la direccion del archivo
        nombre = str(ntpath.basename(ruta)) # Obtenemos su nombre
        ruta_aux = str(ruta).replace(nombre,"") # Eliminamos el nombre de la ruta
        nombre = nombre.replace(".txt","") # Eliminamos su extension del nombre
        clave = numero.get() 
        clave = int(clave) # Obtenemos la clave en entero que se introduce en el Entry
        cadena = str(np.loadtxt(ruta,dtype="str", delimiter="\n"))
        mensaje = cadena.lower()

        descifrado = ""
        clave = 26-clave
        for simbolo in mensaje:
            if simbolo.isalpha(): # isalpha devuelve si la cadena es una minuscula o mayuscula entre A y Z, si no es alfabetico, entonces isalpha regresa false
                num = ord(simbolo)
                num += clave # Sumamos el corrimiento de la clave
                if simbolo.isupper(): # Preguntamos si es mayuscula
                    if num>ord('Z'): # Funcion ord devuelve el unicode de un caracter, si numero es mayor le restamos 26 (letras en el alfabeto) 
                                    #a numero para obtener el caracter con el corrimientod de la clave, este numero es ya que si es mayor a Z tenemos que meterlo en el rango de caracteres
                        num-=26
                    elif num<ord('A'): # Hacemos lo mismo para la A, en este caso se suma 26 para meterlo en el rango
                        num+=26
                elif simbolo.islower(): # Preguntamos si es minuscula y hacemos el mismo procedimiento de arriba
                    if num>ord('z'):
                        num-=26
                    elif num<ord('a'):
                        num+=26
                descifrado+=chr(num)
        archivo_c = open(ruta_aux+nombre+"_D.txt","w") # Cremos el txt
        archivo_c.write(descifrado) # Escribimos el cifrado
        archivo_c.close() # Cerramos el archivo
        print("Mensaje Descifrado")

    # Creamos la tercera interfaz
    if callback is not None:
        callback = functools.partial(callback, *args, **kwargs)

    main_frame = tk.Frame(master)
    labelEspacio3 = Label(main_frame, text="")
    labelLlave = Label(main_frame, text="Ingresa la llave para decifrar (funcion de cifrado)", height=4)
    numero = Entry(main_frame)
    buttonCifrar = Button(main_frame, text="Decifrar", command=decifrar)
    buttonRegresar = Button(main_frame, text = "Regresar", command = callback)
    labelLlave.pack()
    numero.pack()
    labelEspacio3.pack()
    buttonCifrar.pack()
    buttonRegresar.pack()

    return main_frame
    
# Funcion para mostrar la ventana principal
def mostrar_prin():
    secundaria.pack_forget()
    tercera.pack_forget()
    principal.pack(side="top", fill="both", expand=True)

# Funcion para mostrar la ventana de cifrado
def mostrar_sec():
    principal.pack_forget()
    secundaria.pack(side="top", fill="both", expand=True)

def mostrar_ter():
    principal.pack_forget()
    tercera.pack(side="top", fill="both", expand=True)

# Creacion de la ventana y anexo de los botones y los labels                                                                                                       
root = tk.Tk() 
root.title('Practica 0 (Cifrador de Cesar)') 
root.geometry("400x250")
root.resizable(0,0)
principal = tk.Frame(root)
labelEspacio = Label(principal, text="")
labelEspacio2 = Label(principal, text="")
labelExplorador = Label(principal, text = "Selecciona un archivo txt", height=4)    
buttonBuscar = Button(principal, text = "Buscar", command = browseFiles)
buttonCifrar = Button(principal, text = "Cifrar", command=mostrar_sec)
buttonDescifrar = Button(principal, text = "Descifrar", command=mostrar_ter)  
buttonSalir = Button(principal, text = "Salir", command = exit)  
labelExplorador.pack()
buttonBuscar.pack()
labelEspacio.pack()
buttonCifrar.pack()
buttonDescifrar.pack()
labelEspacio2.pack()
buttonSalir.pack()
secundaria = secundaria_v(root, mostrar_prin)
tercera = tercera_v(root, mostrar_prin)
mostrar_prin()
root.mainloop() 