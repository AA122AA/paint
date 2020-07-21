from tkinter import *
from shapes.line import Line
from shapes.oval import Oval
from shapes.rectangle import Rectangle
from shapes.triangle import Triangle

def main():
    root = Tk()
    create_canvas()
    root.mainloop()

def create_canvas():
    w = 600
    h = 400
    canvas = Canvas(root, width=w, height=h, bg='white')
    canvas.pack()

Line(canvas)
Oval(canvas)
Rectangle(canvas)
Triangle(canvas)