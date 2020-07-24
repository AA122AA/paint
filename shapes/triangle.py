import tkinter

class Triangle:
    def __init__(self, canvas, x1 = 0, y1 = 0, x2 = 100, y2 = 100, x3 = 50, y3 = 50, width = 2, fill_color = "", outline_color = ""):
        canvas.create_polygon((x1, y1), (x2, y2), (x3, y3), width = width, fill = fill_color, outline = outline_color)
