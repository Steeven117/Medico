from tkinter import*
from tkinter import messagebox
import tkinter as tk


#Funciones de la APP




def salir():
    messagebox.showinfo("Datos Medicos", "La APP se cerrara, ¿Desea continuar?")
    ventana_principal.destroy()











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
Edad = StringVar()
Altura = StringVar()
Peso = StringVar()

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
lb_c = Label(frame_operaciones, text="Edad: ")
lb_c.config(bg="white", fg="Blue", font=("Helvetica", 20))
lb_c.place(x=10, y=30)

#Caja de texto
entry_c = Entry(frame_operaciones, textvariable=Edad)
entry_c.config(bg="white", fg="Black", font=("Courier", 12))
entry_c.place(x=100, y=35, width=115, height=30)

#Etiqueta para Altura
lb_d = Label(frame_operaciones, text="Altura: ")
lb_d.config(bg="white", fg="Blue", font=("Helvetica", 20))
lb_d.place(x=10, y=95)

#Caja de texto
entry_d = Entry(frame_operaciones, textvariable=Altura)
entry_d.config(bg="white", fg="Black", font=("Courier", 12))
entry_d.place(x=100, y=100, width=115, height=30)

#Etiqueta para Peso corporal
lb_e = Label(frame_operaciones, text="Peso: ")
lb_e.config(bg="white", fg="Blue", font=("Helvetica", 20))
lb_e.place(x=10, y=160)

#Caja de texto
entry_e = Entry(frame_operaciones, textvariable=Peso)
entry_e.config(bg="white", fg="Black", font=("Courier", 12))
entry_e.place(x=100, y=165, width=115, height=30)

#Boton de calcular
bt_calcular=Button(frame_operaciones, text="calcular", command=calcular)
bt_calcular.place(x=200, y=220,width=100, height=30)

#Ventana secundaria inferior
frame_resultados = Frame(ventana_principal)
frame_resultados.config(bg="white", width=485, height=180)
frame_resultados.place(x=10, y=600)

#Area de texto para resultados
t_resultados=Text(frame_resultados)
t_resultados.config(bg="black", fg="green", font=("Courier", 20))
t_resultados.place(x=10, y=10, width=460, height=160)

#Boton de salir
bt_salir=Button(frame_resultados, text="salir", command=salir)
bt_salir.place(x=200, y=145,width=100, height=30)





ventana_principal.mainloop()
