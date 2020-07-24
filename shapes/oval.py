import tkinter

class Oval:
    def __init__(self, canvas, x1 = 0, y1 = 0, x2 = 100, y2 = 150, width = 2, fill_color = "", outline_color = ""):
        canvas.create_oval((x1, y1), (x2, y2), width=width, fill = fill_color, outline = outline_color)

