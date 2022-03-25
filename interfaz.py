from tkinter import *
from tkinter import filedialog
import numpy as np

# Inicializamos variable para guardar la ruta del archivo
archivo = ""

# Funcion para abrir el explorador y guardar la ruta
def browseFiles(): 
    ruta = filedialog.askopenfilename(initialdir = "D:/Documentos/ESCOM/7moSemestre/Crypto/Practica 0/", title = "Select a File", filetypes = (("Text files", "*.txt*"), ("all files", "*.*"))) 
    labelExplorador.configure(text=ruta)

# Funcion de decifrado
def cifrar():
    ruta = labelExplorador.cget("text")
    archivo = np.loadtxt(ruta,dtype="str", delimiter="\n")
    print(archivo)

# Creacion de la ventana y anexo de los botones y los labels                                                                                                       
window = Tk() 
window.title('File Explorer') 
window.geometry("600x200")
window.resizable(0,0)
labelEspacio = Label(window, text="")
labelExplorador = Label(window, text = "Selecciona un archivo txt", height=4)    
buttonBuscar = Button(window, text = "Buscar", command = browseFiles)
buttonCifrar = Button(window, text = "Cifrar", command=cifrar)
buttonDescifrar = Button(window, text = "Descifrar")  
buttonSalir = Button(window, text = "Salir", command = exit)  
labelExplorador.pack()
buttonBuscar.pack()
buttonCifrar.pack()
buttonDescifrar.pack()
buttonSalir.pack()

window.mainloop() 