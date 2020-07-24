from tkinter import *
from shapes.line import Line
from shapes.oval import Oval
from shapes.rectangle import Rectangle
from shapes.triangle import Triangle
from shapes.arc import Arc

def main():
    root = Tk()
    paint(create_canvas(root))
    root.mainloop()

def create_canvas(root):
    w = 1000
    h = 700
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
            prop = line.split(", ")
            Oval(canvas, prop[1], prop[2], prop[3], prop[4], prop[5], prop[6], prop[7])
        elif "ua" in line or "rect" in line:
            prop = line.split(", ")
            Rectangle(canvas, prop[1], prop[2], prop[3], prop[4], prop[5], prop[6], prop[7])
        elif "tri" in line:
            prop = line.split(", ")
            Triangle(canvas, prop[1], prop[2], prop[3], prop[4], prop[5], prop[6], prop[7], prop[8], prop[9])
        elif "in" in line:
            prop = line.split(", ")
            Line(canvas, prop[1], prop[2], prop[3], prop[4], prop[5], prop[6])
        elif "arc" in line:
            prop = line.split(", ")
            Arc(canvas, prop[1], prop[2], prop[3], prop[4], prop[5], prop[6], prop[7], prop[8], prop[9])

if __name__ == "__main__":
    main()