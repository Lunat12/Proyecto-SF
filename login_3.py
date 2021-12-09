import tkinter as tk
from tkinter.constants import FLAT
from typing import Sized, Text
from tkinter import *
import pruebasSQL

root=Tk()
miFrame = Frame(root, width=960, height = 540)
miFrame.pack()
miImage = PhotoImage(file="nvbm.PNG")
Label(miFrame, image = miImage).place(x=0, y =0)

#colores
fondo_entrar="#004AAD"
fondo_salir="#FF1616"
fondo_correcto="#8C52FF"
fondo_incorrecto="#FF5757"
fondo_entrada="#D9D9D9"
blanco = "#FFFFFF"


usuario=tk.StringVar()
password=tk.StringVar()

#Entradas/registro

entrada=tk.Entry(root,textvariable=usuario,width=40)
entrada.place(x=440,y=262)

entrada1=tk.Entry(root,textvariable=password,width=40,show="*")
entrada1.place(x=440,y=385)



#login

# def registro():
#     s = Toplevel()   # For secondary window use Toplevel 
#     s.title('Small Preset Shirt (Not fit to scale)')
#     canvas = Canvas(s, width = 800, height = 100)
#     canvas.pack()
#     miFrame2 = Frame(root, width=960, height = 540)
#     miFrame2.pack()
#     miImage = PhotoImage(file="login.png")
#     Label(miFrame2, image = miImage).place(x=0, y =0)
    

def registro():
    root.withdraw()
    window7=tk.Toplevel()
    miFrame = Frame(window7, width=960, height = 540)
    miFrame.pack()
    window7.title("casa")
    fondo=tk.Label(window7,image=miImage)
    fondo.place(x=0,y=0)

    usuarioLog=tk.StringVar()
    passwordLog=tk.StringVar()

    def regreso2():
        window7.withdraw()
        root.deiconify()
    
    entrada=tk.Entry(window7,textvariable=usuarioLog,width=40)
    entrada.place(x=440,y=262)

    entrada1=tk.Entry(window7,textvariable=passwordLog,width=40,show="*")
    entrada1.place(x=440,y=385)

    boton2=tk.Button(window7,command = lambda: entryUser(usuarioLog.get(),passwordLog.get()),text="Registrado", cursor="hand2",bg="#92B805",width=19,relief="flat",font=("Arial",12))
    boton2.place(x=490,y=460)
        
    imgBut13=PhotoImage(file="next.png")
    imgBut13=imgBut13.subsample(10)
    boton_casa13=tk.Button(window7,image=imgBut13,command=regreso2,cursor="hand2",width=80,height=60,relief="flat").place(x=0,y=455)
    boton_casa13.config(TOP)

def entryUser(user, passw):
    if len(str(user)) > 0 and len(str(password))>0:

        con = pruebasSQL.sql_connection()
        myID = pruebasSQL.sql_fetchID(con)
        fetchU = pruebasSQL.sql_fetchUsername(con)
        add = pruebasSQL.addInfo(myID,user,passw)

        users = []
        for u in fetchU:
            users.append(u[0])
        
        if user in users:
            print('This user already exists')
        else:
            pruebasSQL.sql_insert(con, add)
            

    else:
        print('you must fill the information first')

def login():
    
    con = pruebasSQL.sql_connection()
    print(con)
    fetchU = pruebasSQL.sql_fetchUsername(con)
    print(fetchU)
    fetchP = pruebasSQL.sql_fetchPassword(con)
    print(fetchP)

    state = pruebasSQL.logIn(fetchU, fetchP,usuario.get(), password.get())
    
    if state:
        correcta()
    else:
        incorrecta()



def correcta():
    root.withdraw()
    window=tk.Toplevel()
    window.title("Bienvenido")
    window.geometry("800x800+500+50")
    window.resizable(width=False,height=False)


    def regreso():
       window.withdraw()
       root.deiconify()
       #Boton
    boton3=tk.Button(window,text="Regresar",command=regreso,cursor="hand2",relief="flat",bg=fondo_correcto,font=("Comic Sans MS",12,"bold"))
    boton3.place(x=180,y=400)

def incorrecta():
    window=tk.Toplevel()
    window.title("Error")
    window.geometry("800x800+500+50")
    window.resizable(width=False,height=False)

    def regreso3():
        window.withdraw()
        root.deiconify()
    
    boton31=tk.Button(window,text="Intentar de nuevo.",command=regreso3,cursor="hand2",width=19,relief="flat",bg=fondo_incorrecto,font=("Comic Sans MS",12,"bold"))
    boton31.place(x=148,y=400)
#ventanas_botones


def botonCasa():
    root.withdraw()
    window=tk.Toplevel()
    miFrame = Frame(window, width=960, height = 540)
    miFrame.pack()
    window.title("casa")
    fondo=tk.Label(window,image=miImage)
    fondo.place(x=0,y=0)
    
    def regreso1():
       window.withdraw()
       root.deiconify()
     
    imgBut11=PhotoImage(file="next.png")
    imgBut11=imgBut11.subsample(10)
    boton_casa11=tk.Button(window,image=imgBut11,command=regreso1,cursor="hand2",width=80,height=60,relief="flat").place(x=0,y=455)
    boton_casa11.config(TOP)
    

def botonCash():
    root.withdraw()
    window2=tk.Toplevel()
    miFrame = Frame(window2, width=960, height = 540)
    miFrame.pack()
    window2.title("Cash")
    fondo=tk.Label(window2,image=miImage)
    fondo.place(x=0,y=0)
    

    def regreso2():
       window2.withdraw()
       root.deiconify()
     
    imgBut13=PhotoImage(file="next.png")
    imgBut13=imgBut13.subsample(10)
    boton_casa13=tk.Button(window2,image=imgBut13,command=regreso2,cursor="hand2",width=80,height=60,relief="flat").place(x=0,y=455)
    boton_casa13.config(TOP)
    

def botonEstadistic():
    root.withdraw()
    window3=tk.Toplevel()
    miFrame = Frame(window3, width=960, height = 540)
    miFrame.pack()
    window3.title("estadistic")
    fondo=tk.Label(window3,image=miImage)
    fondo.place(x=0,y=0)
    window3.resizable(width=False,height=False)

    def regreso3():
       window3.withdraw()
       root.deiconify()
     
    imgBut14=PhotoImage(file="next.png")
    imgBut14=imgBut14.subsample(10)
    boton_casa14=tk.Button(window3,image=imgBut14,command=regreso3,cursor="hand2",width=80,height=60,relief="flat").place(x=0,y=455)
    boton_casa14.config(TOP)
  

def botonPerfil():
    root.withdraw()
    window4=tk.Toplevel()
    miFrame = Frame(window4, width=960, height = 540)
    miFrame.pack()
    window4.title("Perfil")
    fondo=tk.Label(window4,image=miImage)
    fondo.place(x=0,y=0)
    window4.resizable(width=False,height=False)
    

    def regreso4():
       window4.withdraw()
       root.deiconify()
     
    imgBut15=PhotoImage(file="next.png")
    imgBut15=imgBut15.subsample(10)
    boton_casa15=tk.Button(window4,image=imgBut15,command=regreso4,cursor="hand2",width=80,height=60,relief="flat").place(x=0,y=455)
    boton_casa15.config(TOP)


def botonNews():
    root.withdraw()
    window5=tk.Toplevel()
    miFrame = Frame(window5, width=960, height = 540)
    miFrame.pack()
    window5.title("News")
    fondo=tk.Label(window5,image=miImage)
    fondo.place(x=0,y=0)
    window5.resizable(width=False,height=False)
    
    def regreso5():
       window5.withdraw()
       root.deiconify()
     
    imgBut16=PhotoImage(file="next.png")
    imgBut16=imgBut16.subsample(10)
    boton_casa16=tk.Button(window5,image=imgBut16,command=regreso5,cursor="hand2",width=80,height=60,relief="flat").place(x=0,y=455)
    boton_casa16.config(TOP)



def Salir():
    root.destroy()

#Botones_login

boton=tk.Button(root,text="Entrar",cursor="hand2",command=login,bg="#92B805",width=12,relief="flat",font=("Arial",12))
boton.place(x=450,y=450)


boton1=tk.Button(root,text="Salir",command=Salir,cursor="hand2",bg="#C46248",width=12,relief="flat",font=("Arial",12))
boton1.place(x=600,y=450)

boton2=tk.Button(root,text="¿ No estás registrad@ ?",command=registro,cursor="hand2",bg="#C46248",width=19,relief="flat",font=("Arial",12))
boton2.place(x=490,y=505)

#menu_botones



imgButton1=PhotoImage(file="casa.png")
imgButton1=imgButton1.subsample(10)
boton_casa=tk.Button(root,compound="center",image=imgButton1,command=botonCasa,cursor="hand2",width=80,height=60,relief="flat").place(x=0,y=80)


imgButton2=PhotoImage(file="cash.png")
imgButton2=imgButton2.subsample(8)
boton_dinero=tk.Button(root,image=imgButton2,command=botonCash,cursor="hand2",width=80,height=60,relief="flat").place(x=0,y=155)


imgButton3=PhotoImage(file="escala.png")
imgButton3=imgButton3.subsample(10)
boton_escala=tk.Button(root,image=imgButton3,command=botonEstadistic,cursor="hand2",bg=fondo_entrada,width=80,height=60,relief="flat").place(x=0,y=230)

imgButton4=PhotoImage(file="perfil1.png")
imgButton4=imgButton4.subsample(40)
boton_perfil=tk.Button(root,image=imgButton4,command=botonPerfil,cursor="hand2",bg=fondo_entrada,width=80,height=60,relief="flat").place(x=0,y=305)

imgButton5=PhotoImage(file="news.png")
imgButton5=imgButton5.subsample(8)
boton_news=tk.Button(root,image=imgButton5,command=botonNews,cursor="hand2",bg=fondo_entrada,width=80,height=60,relief="flat").place(x=0,y=380)





root.mainloop()