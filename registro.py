from tkinter import *
from tkinter import messagebox

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

def confirmar_contraseña():
    password = contraseña_textbox.get()
    confirmar_contraseña = confirmar_contraseña_textbox.get()
    if password == "Ingrese su contraseña" or confirmar_contraseña == "Confirme su contraseña":
        messagebox.showerror("Error", "Debe ingresar una contraseña y confirmarla")
        return False
    elif password != confirmar_contraseña:
        messagebox.showerror("Error", "Las contraseñas no coinciden")
        return False
    else:
        messagebox.showinfo("Éxito", "Usuario registrado exitosamente")
        return True

root = Tk()
root.title("Registro")
root.geometry("360x360")

# Frame principal
frame = Frame(root)
frame.pack()
frame_boton = Frame(root)
frame_boton.pack()

label_registro = Label(frame, text="REGISTRO", font="Helvetica 15")
label_registro.grid(row=0, columnspan=2, pady=40)

label_nombre = Label(frame, text="Nombre", font="Helvetica 11")
label_nombre.grid(row=1, column=0, sticky=E, padx=10, pady=(0,5))

registro_textbox = Entry(frame, width=24, borderwidth=1, relief="solid")
registro_textbox.grid(row=1, column=1, padx=10, pady=(0,5))
set_placeholder(registro_textbox, "Ingrese su nombre")

label_contraseña = Label(frame, text="Contraseña", font="Helvetica 11")
label_contraseña.grid(row=2, column=0, sticky=E, padx=10, pady=(0,5))

contraseña_textbox = Entry(frame, width=24, borderwidth=1, relief="solid", show='●')
contraseña_textbox.grid(row=2, column=1, padx=10, pady=(0,5))
set_placeholder(contraseña_textbox, "Ingrese su contraseña")

label_confirmar_contraseña = Label(frame, text="Confirmar contraseña", font="Helvetica 11")
label_confirmar_contraseña.grid(row=3, column=0, sticky=E, padx=10, pady=(0,5))

confirmar_contraseña_textbox = Entry(frame, width=24, borderwidth=1, relief="solid", show='●')
confirmar_contraseña_textbox.grid(row=3, column=1, padx=10, pady=(0,5))
set_placeholder(confirmar_contraseña_textbox, "Confirme su contraseña")

boton = Button(frame_boton, text="Crear", bg="lightgrey", borderwidth=1, relief="solid", command=confirmar_contraseña)
boton.pack(pady=20)

root.mainloop()
