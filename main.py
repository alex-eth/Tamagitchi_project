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

#### variables

current_tama = "kiki"

##### Creation of variables and initialisation (not used for all) #####

health_kik = ['♥','♥','♥','♥','♥','♥','♥','♥','♥','♥']
health_vio = ['♥','♥','♥','♥','♥','♥','♥','♥','♥','♥']
health_mim = ['♥','♥','♥','♥','♥','♥','♥','♥','♥','♥']
health_gin = ['♥','♥','♥','♥','♥','♥','♥','♥','♥','♥']
#
#hunger_kik = ['🍔','🍔','🍔','🍔','🍔']
#hunger_vio = ['🍔','🍔','🍔','🍔','🍔']
#hunger_mim = ['🍔','🍔','🍔','🍔','🍔']
#hunger_gin = ['🍔','🍔','🍔','🍔','🍔']
#
ex_kik = ['⚡','⚡','⚡','⚡','⚡','⚡']
ex_vio = ['⚡','⚡','⚡','⚡','⚡','⚡']
ex_mim = ['⚡','⚡','⚡','⚡','⚡','⚡']
ex_gin = ['⚡','⚡','⚡','⚡','⚡','⚡']
#
#bor_kik = ['😴','😴','😴','😴']
#bor_vio = ['😴','😴','😴','😴']
#bor_mim = ['😴','😴','😴','😴']
#bor_gin = ['😴','😴','😴','😴']



##### Functions (show functions not used as well) #####

def show_health () :
    health_bar_kik = Label(fenetre, text= health_kik, fg='red',bg = 'white', font="Arial 15 italic")
    health_bar_kik.place(x=95, y=147)

    health_bar_vio = Label(fenetre, text= health_vio, fg='red',bg = 'white', font="Arial 15 italic")
    health_bar_vio.place(x=300, y=147)

    health_bar_mim = Label(fenetre, text= health_mim, fg='red',bg = 'white', font="Arial 15 italic")
    health_bar_mim.place(x=500, y=147)

    health_bar_gin = Label(fenetre, text= health_gin, fg='red',bg = 'white', font="Arial 15 italic")
    health_bar_gin.place(x=710, y=147)

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
    ex_bar_kik.place(x=80, y=200)

    ex_bar_vio = Label(fenetre, text= ex_vio, fg='gold',bg = 'white', font="Arial 15 italic")
    ex_bar_vio.place(x=300, y=200)

    ex_bar_mim = Label(fenetre, text= ex_mim, fg='gold',bg = 'white', font="Arial 15 italic")
    ex_bar_mim.place(x=500, y=200)

    ex_bar_gin = Label(fenetre, text= ex_gin, fg='gold',bg = 'white', font="Arial 15 italic")
    ex_bar_gin.place(x=700, y=200)

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
show_health()
show_exhaustion()
#show_boredom()

life = Label(fenetre, text= "♥   :",fg='firebrick1',bg = 'white', font="Arial 15 italic")
life.place(x=10, y=150)

hunger = Label(fenetre, text= "🍔  :",fg='chocolate1',bg = 'white', font="Arial 15 italic")
hunger.place(x=5, y=173)

ex = Label(fenetre, text= "⚡ :",fg='goldenrod1',bg = 'white', font="Arial 15 italic")
ex.place(x=8, y=202)

bor = Label(fenetre, text= "😴 :",fg='cornflower blue',bg = 'white', font="Arial 15 italic")
bor.place(x=2, y=225)

##### Functions for buttons ######

def eat ():
    increase_hunger()


def sleep ():
    canvas.itemconfig(tamagotchi, fill="blue")


def play ():
    canvas.itemconfig(tamagotchi, fill="yellow")

#root = tk.Tk()

#canvas = tk.Canvas(root, width=200, height=200)
#canvas.pack()

#tamagotchi = canvas.create_oval(80, 50, 120, 90, fill="yellow")

#eat_button = tk.Button(root, text="Eat", command=eat)
#eat_button.pack(side="left", padx=10)

#sleep_button = tk.Button(root, text="Sleep", command=sleep)
#sleep_button.pack(side="left", padx=10)

#play_button = tk.Button(root, text="Play", command=play)
#play_button.pack(side="left", padx=10)

#### Selction of tamagotchis ####


def use_kik () :
    global current_tama
    current_tama = "kiki"
    return current_tama

def use_vio () :
    global current_tama
    current_tama = "vio"
    print(current_tama)
    return current_tama

def use_mim () :
    global current_tama
    current_tama = "mimi"
    return current_tama

def use_gin () :
    global current_tama
    current_tama = "gin"
    return current_tama


###### Creation of the menu #####

menu_bar = tk.Menu(fenetre)
fenetre.config(menu=menu_bar)


file_menu = tk.Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label="Settings", menu=file_menu)


file_menu.add_command(label="Open", command=fenetre.destroy)
file_menu.add_command(label="Save", command=fenetre.destroy)


##### Creation of the buttons #####
bouton_eat = Button(fenetre,text = " Eat ",bg = 'chocolate2',border=round(5), command = eat)
bouton_eat.configure(height=4, width=22)
bouton_eat.place(x=10,y=600)

bouton_play = Button(fenetre,text = " Play ",bg = 'green yellow',border=round(5), command = fenetre.destroy)
bouton_play.configure(height=4, width=22)
bouton_play.place(x=250,y=600)

bouton_sleep = Button(fenetre,text = " Sleep ",bg = 'cornflowerblue',border=round(5), command = fenetre.destroy)
bouton_sleep.configure(height=4, width=22)
bouton_sleep.place(x=500,y=600)

#### Selection buttons ####

bouton_select_kik = Button(fenetre,text = " Use kik ",bg = 'yellow2',border=round(5), command = use_kik)
bouton_select_kik.configure(height=2, width=10)
bouton_select_kik.place(x=110,y=500)


bouton_select_vio = Button(fenetre,text = " Use vio ",bg = 'MediumOrchid1',border=round(5), command = use_vio)
bouton_select_vio.configure(height=2, width=10)
bouton_select_vio.place(x=350,y=500)


bouton_select_mim = Button(fenetre,text = " Use mim ",bg = 'ivory2',border=round(5), command = use_mim)
bouton_select_mim.configure(height=2, width=10)
bouton_select_mim.place(x=580,y=500)


bouton_select_gin = Button(fenetre,text = " Use gin ",bg = 'SkyBlue2',border=round(5), command = use_gin)
bouton_select_gin.configure(height=2, width=10)
bouton_select_gin.place(x=810,y=500)


#####################################################################################################################

###### hunger bar kiki ################
hunger_bar_ki = ttk.Progressbar(fenetre, orient="horizontal", length=200, mode="determinate")
hunger_bar_ki.place(x = 80, y =178)

# maximum value of the progress bar
max_value = 100
hunger_bar_ki["maximum"] = max_value

# initial value of the progress bar
hunger_bar_ki["value"] = max_value



# Function that decrease the progress bar value every 5 seconds
def decrease_hunger_ki():
    current_value = hunger_bar_ki["value"]
    if current_value > 0:
         hunger_bar_ki["value"] = current_value - 1
    fenetre.after(5000, decrease_hunger_ki)

############################################


###### hunger bar vio ################
hunger_bar_vio = ttk.Progressbar(fenetre, orient="horizontal", length=200, mode="determinate")
hunger_bar_vio.place(x = 285, y =178)

# maximum value of the progress bar
max_value = 100
hunger_bar_vio["maximum"] = max_value

# initial value of the progress bar
hunger_bar_vio["value"] = max_value



# Function that decrease the progress bar value every 5 seconds
def decrease_hunger_vio():
    current_value = hunger_bar_vio["value"]
    if current_value > 0:
         hunger_bar_vio["value"] = current_value - 1
    fenetre.after(5000, decrease_hunger_vio)

############################################

###### hunger bar mimi ################
hunger_bar_mim = ttk.Progressbar(fenetre, orient="horizontal", length=200, mode="determinate")
hunger_bar_mim.place(x = 490, y =178)

# maximum value of the progress bar
max_value = 100
hunger_bar_mim["maximum"] = max_value

# initial value of the progress bar
hunger_bar_mim["value"] = max_value



# Function that decrease the progress bar value every 5 seconds
def decrease_hunger_mim():
    current_value = hunger_bar_mim["value"]
    if current_value > 0:
         hunger_bar_mim["value"] = current_value - 1
    fenetre.after(5000, decrease_hunger_mim)

############################################

###### hunger bar gin ################
hunger_bar_gin = ttk.Progressbar(fenetre, orient="horizontal", length=200, mode="determinate")
hunger_bar_gin.place(x = 695, y =178)

# maximum value of the progress bar
max_value = 100
hunger_bar_gin["maximum"] = max_value

# initial value of the progress bar
hunger_bar_gin["value"] = max_value



# Function that decrease the progress bar value every 5 seconds
def decrease_hunger_gin():
    current_value = hunger_bar_gin["value"]
    if current_value > 0:
         hunger_bar_gin["value"] = current_value - 1
    fenetre.after(5000, decrease_hunger_gin)

############################################



def increase_hunger():
    global current_tama
    print(current_tama)
    if current_tama == "kiki" :
        current_value = hunger_bar_ki["value"]
        hunger_bar_ki["value"] = current_value + 10

    elif current_tama == "vio" :
        current_value = hunger_bar_vio["value"]
        hunger_bar_vio["value"] = current_value + 10


    elif current_tama == "mimi" :
        current_value = hunger_bar_mim["value"]
        hunger_bar_mim["value"] = current_value + 10

    elif current_tama == "gin" :
        current_value = hunger_bar_gin["value"]
        hunger_bar_gin["value"] = current_value + 10




decrease_hunger_ki()
decrease_hunger_vio()
decrease_hunger_mim()
decrease_hunger_gin()

fenetre.mainloop()

