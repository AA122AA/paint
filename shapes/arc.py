import tkinter

class Arc:
    def __init__(self, canvas, x1 = 0, y1 = 0, x2 = 100, y2 = 150,  start = 0, extent = 210, outline_color = "", fill_color= "", width = 2):
        canvas.create_arc(x1, y1, x2, y2, start = start, extent = extent, outline = outline_color, fill = fill_color, width = width)
