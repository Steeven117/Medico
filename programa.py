from tkinter import*
from tkinter import messagebox
import tkinter as tk


#Funciones de la APP

















#Diseño de la app
ventana_principal = tk.Tk( )

# Cargar el archivo de imagen desde el disco.
icono = tk.PhotoImage(file="img/logo.png")

# Establecerlo como ícono de la ventana.
ventana_principal.iconphoto(True, icono)

#Titulo de la ventana
ventana_principal.title("Datos Medicos")

#Tamaño de la ventana
ventana_principal.geometry("500x800")

#Deshabilitar boton de maximizar
ventana_principal.resizable(0,0)

#color de fonde de la ventana
ventana_principal.config(bg="Sky blue2")

#Variables de control
Paciente = StringVar()
TI_CC = StringVar()


#Ventana secundaria superior
frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg="white", width=480, height=200)
frame_entrada.place(x=10, y=20)

#Logo de la ONG
logo = PhotoImage(file="img/icono.png")
lb_logo = Label(frame_entrada, image=logo, bg="white")
lb_logo.place(x=11, y=8)

#Informacion del paciente
lb_titulo = Label(frame_entrada, text="Datos del Usuario")
lb_titulo.config(bg="white", fg="Black", font=("Helvetica", 20))
lb_titulo.place(x=240, y=10)

#Etiqueta para Paciente
lb_a = Label(frame_entrada, text="Paciente: ")
lb_a.config(bg="white", fg="Red", font=("Helvetica", 20))
lb_a.place(x=235, y=60)

#Caja de texto 
entry_a = Entry(frame_entrada, textvariable=Paciente)
entry_a.config(bg="white", fg="Black", font=("Courier", 12))
entry_a.focus_set()
entry_a.place(x=355, y=60, width=115, height=30)

#Etiqueta para TI_CC
lb_b = Label(frame_entrada, text="TI_CC :")
lb_b.config(bg="white", fg="Red", font=("Helvetica", 20))
lb_b.place(x=235, y=100)

#Caja de texto 
entry_b = Entry(frame_entrada, textvariable=TI_CC)
entry_b.config(bg="white", fg="Black", font=("Courier", 12))
entry_b.place(x=355, y=100, width=115, height=30)

#Ventana secundaria intermedio
frame_operaciones = Frame(ventana_principal)
frame_operaciones.config(bg="white", width=480, height=270)
frame_operaciones.place(x=10, y=265)

#Etiqueta para Edad
lb_a = Label(frame_operaciones, text="Edad: ")
lb_a.config(bg="white", fg="Blue", font=("Helvetica", 20))
lb_a.place(x=90, y=60)



#Etiqueta para Altura




#Etiqueta para Peso corporal





#Ventana secundaria inferior
frame_resultados = Frame(ventana_principal)
frame_resultados.config(bg="white", width=485, height=180)
frame_resultados.place(x=10, y=600)





ventana_principal.mainloop()
