import os
from tkinter import *
from Administrador import *
from Usuario import *
from Sucursal import *
from Productos import *
import json
import registro

def guardar(admin):
    admin_dict = admin.to_dict()
    json_data = json.dumps(admin_dict)
    with open('datos.json', 'w') as archivo:
        archivo.write(json_data)

def cargar(admin, datos):
    usuarios = {}
    for _, usuario_dic in datos["usuarios"].items():
        usuario = Usuario(usuario_dic["nombre_usuario"], usuario_dic["password"])
        sucursales = {}
        for _, sucursal_dic in usuario_dic["sucursales"].items():
            sucursal = Sucursal(sucursal_dic["nombre"])
            productos = {}
            for _, producto_dic in sucursal_dic["productos"].items():
                producto = Productos.from_dict(producto_dic)
                productos[producto.get_id()] = producto
            sucursal.set_productos(productos)
            sucursales[sucursal.get_nombre()] = sucursal
        usuario.set_sucursales(sucursales)
        usuarios[usuario.get_nombre_usuario()] = usuario
    admin.set_usuarios(usuarios)

admin = Administrador()

if os.path.exists("datos.json"):
    with open('datos.json', 'r') as archivo:
        datos = json.load(archivo)
        cargar(admin, datos)

def set_placeholder(entry, placeholder_text):
    entry.insert(0, placeholder_text)
    entry.config(fg='grey')
    
    def on_focus_in(event):
        if entry.get() == placeholder_text:
            entry.delete(0, END)
            entry.config(fg='black')
    
    def on_focus_out(event):
        if entry.get() == '':
            entry.insert(0, placeholder_text)
            entry.config(fg='grey')

    entry.bind("<FocusIn>", on_focus_in)
    entry.bind("<FocusOut>", on_focus_out)

def procedimiento():
    def usuario():
        return usuario_textbox.get()

    def contrasenia():
        return password_textbox.get()
    
    def registrarse_action():
        admin.registrarUsuario(usuario(), contrasenia())
        guardar(admin)

    def loguearse_action():
        from sucursal_pagina_2 import abrir_usuario
        if usuario() in admin.usuarios:
            if contrasenia() == admin.usuarios[usuario()].get_password():
                print("LOGUEADOOOOOOO PAAAAA")
                abrir_usuario(usuario())
            else:
                print("CONTRA INCORRECTA")
        else:
            print("Usuario no encontrado")
    
    root = Tk() 

    #==============FRAMES==============
    frame_usuarios = Frame(root)
    frame_usuarios.pack(pady=(80,0))
    frame1_usuarios = Frame(root)
    frame1_usuarios.pack(pady=(45,0))
    frame2_usuarios = Frame(root)
    frame2_usuarios.pack(pady=5)
    #==================================

    root.title("Inventario") 
    root.geometry("480x480") 

    lbl_iniciar = Label(frame_usuarios, text="INICIAR SESIÓN", font="Helvetica 15")
    lbl_iniciar.pack()

    lbl_usuario = Label(frame1_usuarios, text="Usuario", font="Helvetica 11")
    lbl_usuario.pack()

    usuario_textbox = Entry(frame2_usuarios, width=24, borderwidth=1, relief="solid")
    usuario_textbox.pack(pady=(0,5))
    set_placeholder(usuario_textbox, "Ingrese su usuario")

    lbl_password = Label(frame2_usuarios, text="Contraseña", font="Helvetica 11")
    lbl_password.pack()

    password_textbox = Entry(frame2_usuarios, width=24, show="●", borderwidth=1, relief="solid")
    password_textbox.pack(pady=5)
    set_placeholder(password_textbox, "Ingrese su contraseña")

    btn = Button(frame2_usuarios, text="Iniciar sesion", command=loguearse_action, bg="lightgrey", borderwidth=1, relief="solid")
    btn.pack(pady=5)

    registrarse = Button(frame2_usuarios, text="Registrarse", command=registro.procedimiento, bg="lightgrey", borderwidth=1, relief="solid")
    registrarse.pack()

    root.mainloop()