__author__ = "macaw"
import os
from tkinter import *
from tkinter import messagebox

main = Tk()
main.geometry("1366x768")
main.title("El Corral")
main.resizable(0, 0)
def Exit():
    sure = messagebox.askyesno("Salir","¿Seguro que quieres salir?", parent=main)
    if sure == True:
        main.destroy()
        
main.protocol("WM_DELETE_WINDOW", Exit)

def emp():
    main.withdraw()
    os.system("python employee.py")
    main.deiconify()


def adm():
    main.withdraw()
    os.system("python admin.py")
    main.deiconify()

label1 = Label(main)
label1.place(relx=0, rely=0, width=1366, height=768)
img = PhotoImage(file="./images/main1.png")
label1.configure(image=img)

label_title = Label(main, text="INGRESAR", font=("Impact", 40), bg="#27374D", fg="#d46c91")
label_title.place(relx=0.5, rely=0.2, anchor="center")

button1 = Button(main)
button1.place(relx=0.316, rely=0.446, width=146, height=130)
button1.configure(relief="flat")
button1.configure(overrelief="flat")
button1.configure(activebackground="#ffffff")
button1.configure(cursor="hand2")
button1.configure(foreground="#ffffff")
button1.configure(background="#27374D")
button1.configure(borderwidth="0")
img2 = PhotoImage(file="./images/empleado.png")
button1.configure(image=img2)
button1.configure(command=emp)

label2 = Label(text="Empleado", bg="#27374D",fg="#d46c91",font=("Arial", 15))
label2.place(relx=0.316, rely=0.446 + 0.175, width=146, height=30)

button2 = Button(main)
button2.place(relx=0.566, rely=0.448, width=146, height=130)
button2.configure(relief="flat")
button2.configure(overrelief="flat")
button2.configure(activebackground="#ffffff")
button2.configure(cursor="hand2")
button2.configure(foreground="#ffffff")
button2.configure(background="#27374D")
button2.configure(borderwidth="0")
img3 = PhotoImage(file="./images/administrador.png")
button2.configure(image=img3)
button2.configure(command=adm)

label2 = Label(text="Administrador", bg="#27374D",fg="#d46c91",font=("Arial", 15))
label2.place(relx=0.566, rely=0.446 + 0.175, width=146, height=30)
main.mainloop()
