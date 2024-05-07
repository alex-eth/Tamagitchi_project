def eat():
    canvas.itemconfig(tamagotchi, fill="green")

def sleep():
    canvas.itemconfig(tamagotchi, fill="blue")

def play():
    canvas.itemconfig(tamagotchi, fill="yellow")

root = tk.Tk()

canvas = tk.Canvas(root, width=200, height=200)
canvas.pack()

tamagotchi = canvas.create_oval(80, 50, 120, 90, fill="yellow")

eat_button = tk.Button(root, text="Eat", command=eat)
eat_button.pack(side="left", padx=10)

sleep_button = tk.Button(root, text="Sleep", command=sleep)
sleep_button.pack(side="left", padx=10)

play_button = tk.Button(root, text="Play", command=play)
play_button.pack(side="left", padx=10)
