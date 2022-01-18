import tkinter as tk
import random
top = tk.Tk()
top.title("Dice Simulator.")
top.configure(background="grey")
top.geometry("600x600")
canvas = tk.Canvas(top,height=600,width=600)
def dice1 ():
    canvas.create_oval(280,280,320,320, fill="white")# circle size is 40 diameter.
def dice2 ():
    canvas.create_oval(240,280,280,320, fill="white")
    canvas.create_oval(320,280,360,320, fill="white")
def dice3 ():
    canvas.create_oval(230,330,270,370, fill="white")
    canvas.create_oval(280,280,320,320, fill="white")
    canvas.create_oval(330,230,370,270, fill="white")
def dice4 ():
    canvas.create_oval(230,230,270,270, fill="white")
    canvas.create_oval(330,230,370,270, fill="white")
    canvas.create_oval(230,330,270,370, fill="white")
    canvas.create_oval(330,330,370,370, fill="white")
def dice5 ():
    canvas.create_oval(230,230,270,270, fill="white")
    canvas.create_oval(330,230,370,270, fill="white")
    canvas.create_oval(230,330,270,370, fill="white")
    canvas.create_oval(330,330,370,370, fill="white")
    canvas.create_oval(280,280,320,320, fill="white")
def dice6 ():
    canvas.create_oval(230,230,270,270, fill="white")
    canvas.create_oval(330,230,370,270, fill="white")
    canvas.create_oval(230,330,270,370, fill="white")
    canvas.create_oval(330,330,370,370, fill="white")
    canvas.create_oval(230,280,270,320, fill="white")
    canvas.create_oval(330,280,370,320, fill="white")

def guess():
    canvas.delete("all")
    canvas.create_rectangle(200, 200, 400, 400, fill="black") #square size is 200
    number = random.choice([1,2,3,4,5,6])
    if number == 1:  
        dice1()
    elif number == 2:
        dice2()
    elif number == 3:
        dice3()
    elif number == 4:
        dice4()
    elif number == 5:
        dice5()
    else:
        dice6()
canvas.create_rectangle(200, 200, 400, 400, fill="black") #square size is 200
but = tk.Button(top, text="Shuffle", command = lambda: guess() )
but.pack()
but.place(in_=canvas)


 

canvas.pack()
top.mainloop()