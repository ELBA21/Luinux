from tkinter import *

root = Tk() 

root.config(bg="white")
root.title("Test")
root.geometry("720x480")


lbl1 = Label(root, text="Sucursales", bg="yellow")
btn0 = Button(root, text="Editar", bg="gray")
btn1 = Button(root, text="1", bg="lightgray")
btn2 = Button(root, text="2", bg="lightgray")
btn3 = Button(root, text="3", bg="lightgray")
btn4 = Button(root, text="4", bg="lightgray")
btn5 = Button(root, text="5", bg="lightgray")
btn6 = Button(root, text="6", bg="lightgray")
btn7 = Button(root, text="7", bg="lightgray")
btn8 = Button(root, text="8", bg="lightgray")


lbl1.grid(row=0, column=0, padx=5, pady= 15, sticky="e", ipady=5, ipadx= 40)
btn0.grid(row=0, column=4, padx=5, pady=5, sticky="e", ipady=5, ipadx= 25)
btn1.grid(row=1, column=1, padx=10, pady=15, sticky="w", ipady=15, ipadx= 15)
btn2.grid(row=1, column=2, padx=10, pady=15, sticky="w", ipady=15, ipadx= 15)
btn3.grid(row=1, column=3, padx=10, pady=15, sticky="w", ipady=15, ipadx= 15)
btn4.grid(row=1, column=4, padx=10, pady=15, sticky="w", ipady=15, ipadx= 15)
btn5.grid(row=2, column=1, padx=10, pady=5, sticky="w", ipady=15, ipadx= 15)
btn6.grid(row=2, column=2, padx=10, pady=5, sticky="w", ipady=15, ipadx= 15)
btn7.grid(row=2, column=3, padx=10, pady=5, sticky="w", ipady=15, ipadx= 15)
btn8.grid(row=2, column=4, padx=10, pady=5, sticky="w", ipady=15, ipadx= 15)

root.mainloop()