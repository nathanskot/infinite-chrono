from tkinter import Tk, Canvas, Button, Menu

class Chrono:
    def __init__(self, window: Tk, canvas: Canvas):
        self.root = window
        self.canvas = canvas

        self.canvas.create_rectangle(
            400,
            400,
            600,
            600,
            fill="#FFA4A4",
            outline="#000000"
        )