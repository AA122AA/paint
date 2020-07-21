from tkinter import *
from shapes.line import Line
from shapes.oval import Oval
from shapes.rectangle import Rectangle
from shapes.triangle import Triangle

def main():
    root = Tk()
    paint(create_canvas(root))
    root.mainloop()

def create_canvas(root):
    w = 600
    h = 400
    canvas = Canvas(root, width=w, height=h, bg='white')
    canvas.pack()
    return canvas

def read_file():
    with open("instruction.txt", "r") as inst:
        text = inst.read().splitlines()
    return text

def paint(canvas):
    text = read_file()
    for line in text:
        if "rcl" in line or "va" in line:
            Oval(canvas)
        elif "ua" in line or "sq" in line:
            Rectangle(canvas)
        elif "tri" in line:
            Triangle(canvas)
        elif "in" in line:
            Line(canvas)


# Line(canvas)
# Oval(canvas)
# Rectangle(canvas)
# Triangle(canvas)

if __name__ == "__main__":
    main()