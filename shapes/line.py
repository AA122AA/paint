import tkinter

class Line:
    def __init__(self, canvas, x1 = 0, y1 = 0, x2 = 100, y2 = 100, width = 2, fill_color = ""):
        canvas.create_line((x1, y1), (x2, y2), width = width, fill = fill_color)
    
        