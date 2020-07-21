
import tkinter

class Rectangle:
    def __init__(self, canvas, x1 = 10, y1 = 10, x2 = 100, y2 = 100, width = 3, outline='green'):
        canvas.create_rectangle((x1, y1), (x2, y2), outline = outline, width = width) 