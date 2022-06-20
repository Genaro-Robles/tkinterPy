import tkinter as tk
from tkinter import messagebox as tkmes



class Aplicacion():
    def __init__(self):
        self.ventana1 = tk.Tk()
        self.ventana1.title("Registro de Entrada")
        self.ventana1.geometry("450x320")
        self.nom=tk.StringVar()
        self.label1=tk.Label(self.ventana1, text="Nombre: ")
        self.label1.grid(column=0,row=0)
        self.entry1=tk.Entry(self.ventana1,width=25,textvariable=self.nom)
        self.entry1.grid(column=1,row=0)
        self.ape=tk.StringVar()
        self.label2=tk.Label(self.ventana1, text="Apellido: ")
        self.label2.grid(column=0,row=1)
        self.entry2=tk.Entry(self.ventana1,width=25,textvariable=self.ape)
        self.entry2.grid(column=1,row=1)
        self.seleccion=tk.IntVar()
        self.seleccion.set(2)
        self.label3=tk.Label(self.ventana1, text="Sexo: ")
        self.label3.grid(column=0,row=2)
        self.radio1=tk.Radiobutton(self.ventana1,text="Masculino",variable=self.seleccion,value=1)
        self.radio1.grid(column=1,row=2)
        self.radio2=tk.Radiobutton(self.ventana1,text="Femenino",variable=self.seleccion,value=2)
        self.radio2.grid(column=1,row=3)
        self.label3=tk.Label(self.ventana1, text="Lenguajes: ")
        self.label3.grid(column=0,row=5)
        self.seleccion1=tk.IntVar()
        self.check1=tk.Checkbutton(self.ventana1,text="Espa�ol",variable=self.seleccion1)
        self.check1.grid(column=0,row=6)
        self.seleccion2=tk.IntVar()
        self.check2=tk.Checkbutton(self.ventana1,text="Ingles",variable=self.seleccion2)
        self.check2.grid(column=1,row=6)
        self.seleccion3=tk.IntVar()
        self.check2=tk.Checkbutton(self.ventana1,text="Japones",variable=self.seleccion3)
        self.check2.grid(column=0,row=7)
        self.tel=tk.StringVar()
        self.label4=tk.Label(self.ventana1, text="Telefono: ")
        self.label4.grid(column=0,row=8)
        self.entry3=tk.Entry(self.ventana1,width=30,textvariable=self.tel)
        self.entry3.grid(column=1,row=8)
        self.dir=tk.StringVar()
        self.label5=tk.Label(self.ventana1, text="Direccion: ",pady=6)
        self.label5.grid(column=0,row=9)
        self.entry4=tk.Entry(self.ventana1,width=30,textvariable=self.dir)
        self.entry4.grid(column=1,row=9)
        self.boton1=tk.Button(self.ventana1,text="Enviar",command=self.mostrar)
        self.boton1.grid(column=0,row=10)
        self.ventana1.mainloop()
    
    def mostrar(self):
        tkmes.showinfo("AVISO", "REGISTRO INGRESADO CORRECTAMENTE")
        nombre = self.nom.get()
        apellido = self.ape.get()
        telefono = self.tel.get()
        direccion = self.dir.get()
        sexo = ""
        lenguaje = ""
        if self.seleccion.get()==1:
            sexo = "Masculino"
        elif self.seleccion.get()==2:
            sexo = "Femenino"

        if self.seleccion1.get()==1:
            lenguaje += " Espa�ol "
        if self.seleccion2.get()==1:
            lenguaje +=" Ingles "
        if self.seleccion3.get()==1:
            lenguaje +=" Japones "

        self.ventana2 = tk.Tk()
        self.ventana2.title("Registro de Salida")
        self.ventana2.geometry("400x200")
        self.label1=tk.Label(self.ventana2, text="Nombre: "+nombre, font = "MVBoli 16 bold")
        self.label1.grid(column=0,row=0)
        self.label2=tk.Label(self.ventana2, text="Apellido: "+apellido, font = "MVBoli 16 bold")
        self.label2.grid(column=0,row=1)
        self.label3=tk.Label(self.ventana2, text="Sexo: "+sexo, font = "MVBoli 16 bold")
        self.label3.grid(column=0,row=2)
        self.label4=tk.Label(self.ventana2, text="Lenguajes: "+lenguaje, font = "MVBoli 16 bold")
        self.label4.grid(column=0,row=3)
        self.label5=tk.Label(self.ventana2, text="Telefono: "+telefono, font = "MVBoli 16 bold")
        self.label5.grid(column=0,row=4)
        self.label5=tk.Label(self.ventana2, text="Direccion: "+direccion, font = "MVBoli 16 bold")
        self.label5.grid(column=0,row=5)
        self.ventana2.mainloop()

aplicacion=Aplicacion()