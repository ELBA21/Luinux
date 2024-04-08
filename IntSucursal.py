from tkinter import *
from tkinter import font

root = Tk() 

root.config(bg="white")
root.title("Sucursales")
root.geometry("720x480")

bold_font = font.Font(family="Helvetica", size=12, weight="bold")


frame_sucursales = Frame(root, bg="white", borderwidth=1, relief="solid")
frame_sucursales.grid(row=0, column=0, padx=5, pady=15, sticky="e", columnspan=3)

lbl1 = Label(frame_sucursales, text="Sucursales", bg="white", fg="black", font=bold_font)
lbl1.pack(side=LEFT, padx=5)

frame_editar = Frame(root)
frame_editar.grid(row=0, column=4, padx=5, pady=5, sticky="e")

btn0 = Button(frame_editar, text="Editar", bg="gray", padx=15,fg="white")
btn0.pack()

frame_buttons = Frame(root, borderwidth=1, relief="solid")
frame_buttons.grid(row=1, column=0, columnspan=5, padx=5, pady=5)

btn1 = Button(frame_buttons, text="1", bg="lightgray")
btn1.grid(row=0, column=0, padx=10, pady=15, sticky="w", ipady=15, ipadx=15)
btn2 = Button(frame_buttons, text="2", bg="lightgray")
btn2.grid(row=0, column=1, padx=10, pady=15, sticky="w", ipady=15, ipadx=15)
btn3 = Button(frame_buttons, text="3", bg="lightgray")
btn3.grid(row=0, column=2, padx=10, pady=15, sticky="w", ipady=15, ipadx=15)
btn4 = Button(frame_buttons, text="4", bg="lightgray")
btn4.grid(row=0, column=3, padx=10, pady=15, sticky="w", ipady=15, ipadx=15)
btn5 = Button(frame_buttons, text="5", bg="lightgray")
btn5.grid(row=1, column=0, padx=10, pady=5, sticky="w", ipady=15, ipadx=15)
btn6 = Button(frame_buttons, text="6", bg="lightgray")
btn6.grid(row=1, column=1, padx=10, pady=5, sticky="w", ipady=15, ipadx=15)
btn7 = Button(frame_buttons, text="7", bg="lightgray")
btn7.grid(row=1, column=2, padx=10, pady=5, sticky="w", ipady=15, ipadx=15)
btn8 = Button(frame_buttons, text="8", bg="lightgray")
btn8.grid(row=1, column=3, padx=10, pady=5, sticky="w", ipady=15, ipadx=15)

root.mainloop()
