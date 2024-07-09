import os
from tkinter import *
from Administrador import *
from Usuario import *
from Sucursal import *
from Producto import *
import json
import registro
from functools import partial

def guardar(admin):
    admin_dict = admin.to_dict()
    json_data = json.dumps(admin_dict)
    with open('datos.json', 'w') as archivo:
        archivo.write(json_data)

def cargar(admin, datos):
    usuarios = {}
    for _, usuario_dic in datos["usuarios"].items():
        usuario = Usuario(usuario_dic["nombre_usuario"], usuario_dic["password"])
        print("cargando " + usuario.get_nombre_usuario())
        sucursales = {}
        for _, sucursal_dic in usuario_dic["sucursales"].items():
            sucursal = Sucursal(sucursal_dic["nombre"])
            print("cargando " + sucursal.get_nombre() + ".bsp")#referencias al mapping de source
            productos = {}
            for _, producto_dic in sucursal_dic["productos"].items():
                producto = Producto.from_dict(producto_dic)
                print("cargando " + producto.get_nombre() + ".vmt")
                productos[producto.get_id()] = producto
            print("productos en" + sucursal.get_nombre() + " " + str(len(productos)))
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

def ischarok(string, space): #funcion que bloquea los simbolos en las entradas
    if space:                #esta funcion es una de piton
        return string.isalnum() or string.isspace()
    else:
        return string.isalnum()

def validate_command(entry, space):
    vcmd = (entry.register(partial(ischarok, space=space)), '%S') #el '%S' es el caracter que se esta intentando ingresar
    entry.config(validate='key', validatecommand=vcmd) #cambiamos la config del entry para que solo acepte los chars que queremos
    #ocupamos partial de functools para pasar el booleano a la funcion y decidir si queremos espacios o no
def isnumok(int):
    if int in "1234567890": #hacemos lo mismo pero con numeros para los precios
        return True
    else:
        print("hola andres")
        return False

def validate_command_numerin(entry):
    vcmd = (entry.register(isnumok), '%S')
    entry.config(validate='key', validatecommand=vcmd)
    #hola andres
def procedimiento():
    def usuario():
        return usuario_textbox.get()

    def contrasenia():
        return password_textbox.get()
    
    def registrarse_action():
        admin.registrarUsuario(usuario(), contrasenia())
        guardar(admin)
    root = Tk() 
    def loguearse_action():
        from sucursal_pagina_2 import abrir_usuario
        if usuario() in admin.usuarios:
            if contrasenia() == admin.usuarios[usuario()].get_password():
                print("Logueado")
                abrir_usuario(usuario(),root)

            else:
                print("CONTRA INCORRECTA")
        else:
            print("Usuario no encontrado")
    
    

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

    lbl_iniciar = Label(frame_usuarios, text="Iniciar sesión", font="Helvetica 15")
    lbl_iniciar.pack()

    lbl_usuario = Label(frame1_usuarios, text="Usuario", font="Helvetica 11")
    lbl_usuario.pack()

    usuario_textbox = Entry(frame2_usuarios, width=24, borderwidth=1, relief="solid")
    usuario_textbox.pack(pady=(0,5))
    validate_command(usuario_textbox, False)
    #set_placeholder(usuario_textbox, "Ingrese su usuario")

    lbl_password = Label(frame2_usuarios, text="Contraseña", font="Helvetica 11")
    lbl_password.pack()

    password_textbox = Entry(frame2_usuarios, width=24, show="●", borderwidth=1, relief="solid")
    password_textbox.pack(pady=5)
    set_placeholder(password_textbox, "Ingrese su contraseña")

    btn = Button(frame2_usuarios, text="Iniciar sesión", command=loguearse_action, bg="lightgrey", borderwidth=1, relief="solid")
    btn.pack(pady=5)

    registrarse = Button(frame2_usuarios, text="Registrarse", command=registro.procedimiento, bg="lightgrey", borderwidth=1, relief="solid")
    registrarse.pack()

    root.mainloop()