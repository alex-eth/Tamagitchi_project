from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from random import *
import time
from datetime import datetime

##### Creation of the window #####
fenetre = Tk()
fenetre.title("Tamagotchi simulator")
fenetre.configure(bg='white')

fenetre.geometry("1000x800")

##### Placement of the tamagotchis #####
tama = Image.open("tama.png").resize((875, 225))
tama = ImageTk.PhotoImage(tama)

label_tama = Label(fenetre, image=tama)
label_tama.pack()

label_tama.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

##### Creation of variables and initialisation #####

health_kik = ['♥','♥','♥','♥','♥']
health_vio = ['♥','♥','♥','♥','♥']
health_mim = ['♥','♥','♥','♥','♥']
health_gin = ['♥','♥','♥','♥','♥']

hunger_kik = ['🍔','🍔','🍔','🍔','🍔']
hunger_vio = ['🍔','🍔','🍔','🍔','🍔']
hunger_mim = ['🍔','🍔','🍔','🍔','🍔']
hunger_gin = ['🍔','🍔','🍔','🍔','🍔']

##### Functions #####

def show_health () :
    health_bar_kik = Label(fenetre, text= health_kik, fg='red',bg = 'white', font="Arial 15 italic")
    health_bar_kik.place(x=100, y=260)

    health_bar_vio = Label(fenetre, text= health_vio, fg='red',bg = 'white', font="Arial 15 italic")
    health_bar_vio.place(x=350, y=260)

    health_bar_mim = Label(fenetre, text= health_mim, fg='red',bg = 'white', font="Arial 15 italic")
    health_bar_mim.place(x=575, y=260)

    health_bar_kik = Label(fenetre, text= health_kik, fg='red',bg = 'white', font="Arial 15 italic")
    health_bar_kik.place(x=800, y=260)

def show_hunger () :
    hunger_bar_kik = Label(fenetre, text= health_kik, fg='red',bg = 'white', font="Arial 15 italic")
    health_bar_kik.place(x=100, y=260)

    health_bar_vio = Label(fenetre, text= health_vio, fg='red',bg = 'white', font="Arial 15 italic")
    health_bar_vio.place(x=350, y=260)

    health_bar_mim = Label(fenetre, text= health_mim, fg='red',bg = 'white', font="Arial 15 italic")
    health_bar_mim.place(x=575, y=260)

    health_bar_kik = Label(fenetre, text= health_kik, fg='red',bg = 'white', font="Arial 15 italic")
    health_bar_kik.place(x=800, y=260)


show_health()

###### Creation of the menu #####

menu_bar = tk.Menu(fenetre)
fenetre.config(menu=menu_bar)


file_menu = tk.Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label="Settings", menu=file_menu)


file_menu.add_command(label="Open", command=fenetre.destroy)
file_menu.add_command(label="Save", command=fenetre.destroy)


##### Creation of the buttons #####
bouton_eat = Button(fenetre,text = " Eat ",bg = 'chocolate2',border=round(5), command = fenetre.destroy)
bouton_eat.configure(height=4, width=22)
bouton_eat.place(x=10,y=600)

bouton_play = Button(fenetre,text = " Play ",bg = 'green yellow',border=round(5), command = fenetre.destroy)
bouton_play.configure(height=4, width=22)
bouton_play.place(x=250,y=600)

bouton_sleep = Button(fenetre,text = " Sleep ",bg = 'cornflowerblue',border=round(5), command = fenetre.destroy)
bouton_sleep.configure(height=4, width=22)
bouton_sleep.place(x=500,y=600)



fenetre.mainloop()

