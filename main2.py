from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from random import *
import time
from datetime import datetime
from tkinter import ttk


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

health_kik = ['♥','♥','♥','♥','♥','♥','♥']
health_vio = ['♥','♥','♥','♥','♥','♥','♥']
health_mim = ['♥','♥','♥','♥','♥','♥','♥']
health_gin = ['♥','♥','♥','♥','♥','♥','♥']

hunger_kik = ['🍔','🍔','🍔','🍔','🍔']
hunger_vio = ['🍔','🍔','🍔','🍔','🍔']
hunger_mim = ['🍔','🍔','🍔','🍔','🍔']
hunger_gin = ['🍔','🍔','🍔','🍔','🍔']

ex_kik = ['⚡','⚡','⚡','⚡','⚡','⚡','⚡']
ex_vio = ['⚡','⚡','⚡','⚡','⚡','⚡','⚡']
ex_mim = ['⚡','⚡','⚡','⚡','⚡','⚡','⚡']
ex_gin = ['⚡','⚡','⚡','⚡','⚡','⚡','⚡']

bor_kik = ['😴','😴','😴','😴']
bor_vio = ['😴','😴','😴','😴']
bor_mim = ['😴','😴','😴','😴']
bor_gin = ['😴','😴','😴','😴']



##### Functions #####

def show_health () :
    health_bar_kik = Label(fenetre, text= health_kik, fg='red',bg = 'white', font="Arial 15 italic")
    health_bar_kik.place(x=100, y=260)

    health_bar_vio = Label(fenetre, text= health_vio, fg='red',bg = 'white', font="Arial 15 italic")
    health_bar_vio.place(x=350, y=260)

    health_bar_mim = Label(fenetre, text= health_mim, fg='red',bg = 'white', font="Arial 15 italic")
    health_bar_mim.place(x=575, y=260)

    health_bar_gin = Label(fenetre, text= health_gin, fg='red',bg = 'white', font="Arial 15 italic")
    health_bar_gin.place(x=800, y=260)

def show_hunger () :
    hunger_bar_kik = Label(fenetre, text= hunger_kik, fg='goldenrod2',bg = 'white', font="Arial 15 italic")
    hunger_bar_kik.place(x=100, y=230)

    hunger_bar_vio = Label(fenetre, text= hunger_vio, fg='goldenrod2',bg = 'white', font="Arial 15 italic")
    hunger_bar_vio.place(x=350, y=230)

    hunger_bar_mim = Label(fenetre, text= hunger_mim, fg='goldenrod2',bg = 'white', font="Arial 15 italic")
    hunger_bar_mim.place(x=575, y=230)

    hunger_bar_gin = Label(fenetre, text= hunger_gin, fg='goldenrod2',bg = 'white', font="Arial 15 italic")
    hunger_bar_gin.place(x=800, y=230)

def show_exhaustion () :
    ex_bar_kik = Label(fenetre, text= ex_kik, fg='gold',bg = 'white', font="Arial 15 italic")
    ex_bar_kik.place(x=100, y=200)

    ex_bar_vio = Label(fenetre, text= ex_vio, fg='gold',bg = 'white', font="Arial 15 italic")
    ex_bar_vio.place(x=350, y=200)

    ex_bar_mim = Label(fenetre, text= ex_mim, fg='gold',bg = 'white', font="Arial 15 italic")
    ex_bar_mim.place(x=575, y=200)

    ex_bar_gin = Label(fenetre, text= ex_gin, fg='gold',bg = 'white', font="Arial 15 italic")
    ex_bar_gin.place(x=800, y=200)

def show_boredom () :
    bor_bar_kik = Label(fenetre, text= bor_kik,fg='blue',bg = 'white', font="Arial 15 italic")
    bor_bar_kik.place(x=100, y=170)

    bor_bar_vio = Label(fenetre, text= bor_vio,fg='blue',bg = 'white', font="Arial 15 italic")
    bor_bar_vio.place(x=350, y=170)

    bor_bar_mim = Label(fenetre, text= bor_mim,fg='blue',bg = 'white', font="Arial 15 italic")
    bor_bar_mim.place(x=575, y=170)

    bor_bar_gin = Label(fenetre, text= bor_gin,fg='blue',bg = 'white', font="Arial 15 italic")
    bor_bar_gin.place(x=800, y=170)

#show_hunger()
#show_health()
#show_exhaustion()
#show_boredom()

life = Label(fenetre, text= "♥   :",fg='firebrick1',bg = 'white', font="Arial 15 italic")
life.place(x=10, y=150)

hunger = Label(fenetre, text= "🍔  :",fg='chocolate1',bg = 'white', font="Arial 15 italic")
hunger.place(x=5, y=173)

ex = Label(fenetre, text= "⚡ :",fg='goldenrod1',bg = 'white', font="Arial 15 italic")
ex.place(x=0, y=202)

bor = Label(fenetre, text= "😴 :",fg='cornflower blue',bg = 'white', font="Arial 15 italic")
bor.place(x=2, y=225)

##### Functions for buttons ######

def eat():
    canvas.itemconfig(tamagotchi, fill="green")

def sleep():
    canvas.itemconfig(tamagotchi, fill="blue")

def play():
    canvas.itemconfig(tamagotchi, fill="yellow")

# Création de la fenêtre principale
root = tk.Tk()

# Création du canvas
canvas = tk.Canvas(root, width=200, height=200)
canvas.pack()

# Création du tamagotchi
tamagotchi = canvas.create_oval(80, 50, 120, 90, fill="yellow")

# Création des boutons pour les actions
eat_button = tk.Button(root, text="Manger", command=eat)
eat_button.pack(side="left", padx=10)

sleep_button = tk.Button(root, text="Dormir", command=sleep)
sleep_button.pack(side="left", padx=10)

play_button = tk.Button(root, text="Jouer", command=play)
play_button.pack(side="left", padx=10)

root.mainloop()


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

#####################################################################################################################


progress_bar = ttk.Progressbar(fenetre, orient="horizontal", length=200, mode="determinate")
progress_bar.pack()

# maximum value of the progress bar
max_value = 100
progress_bar["maximum"] = max_value

# initial value of the progress bar
progress_bar["value"] = max_value

# Function that decrease the progress bar value every 5 seconds
def decrease_hunger():
    current_value = progress_bar["value"]
    if current_value > 0:
        progress_bar["value"] = current_value - 1
    fenetre.after(5000, decrease_hunger)


decrease_hunger()

fenetre.mainloop()

