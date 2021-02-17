from tkinter import *
import math
import random

 #la fenêtre
window = Tk()
window.title("")
window.geometry("500x500")
window.config(background='white')

#frame
frame= Frame(window,bg='black')

#bouton annuler
button_annuler = Button(frame, text ="Annuler",bg='black',fg="blue")
button_annuler.pack(side=LEFT)

#carré de 50 vert
def carre():
    x = rd.randint(0, 50)
    y =  rd.randint(0, 50)
    canvas.create_rectangle((x, y), (x, y), fill = 'green')
    carre.pack(side=LEFT)
#carré de 50 jaune
#carré de 50 bleu

#cercle
CANVAS_WIDTH, CANVAS_HEIGHT = 600, 400

if __name__ == '__main__':
    root = Tk('window')
    canvas = Canvas(root, width = CANVAS_WIDTH, height = CANVAS_HEIGHT)
    x0 = 50
    x1 = CANVAS_WIDTH - 50
    y = CANVAS_HEIGHT / 2
    canvas.create_oval(x0 - 50, y + 50, x0 + 50, y - 50)

#ajouter
frame.pack(side=LEFT)
canvas.pack(expand=YES)

#afficher
canvas.pack()
window.mainloop()