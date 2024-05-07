def eat():
    canvas.itemconfig(tamagotchi, fill="green")

def sleep():
    canvas.itemconfig(tamagotchi, fill="blue")

def play():
    canvas.itemconfig(tamagotchi, fill="yellow")

def change_background(color):
    canvas.config(bg=color)

root = tk.Tk()

canvas = root.children["canvas"]

tamagotchi = canvas.find_all()[0]

eat_button = tk.Button(root, text="Eat", command=eat)
eat_button.pack(side="left", padx=10)

sleep_button = tk.Button(root, text="Sleep", command=sleep)
sleep_button.pack(side="left", padx=10)

play_button = tk.Button(root, text="Play", command=play)
play_button.pack(side="left", padx=10)

bg_button1 = tk.Button(root, text="Light Background", command=lambda: change_background("lightgrey"))
bg_button1.pack(side="right", padx=10)

bg_button2 = tk.Button(root, text="Dark Background", command=lambda: change_background("darkgrey"))
bg_button2.pack(side="right", padx=10)

root.mainloop()

