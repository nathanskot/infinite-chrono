from tkinter import Tk, Canvas, Button, Menu
import settings

class Chrono:
    def __init__(self, id:int, label:str, window: Tk, canvas: Canvas):
        self.id = id
        self.label = label
        self.root = window
        self.canvas = canvas
        self.canvas_ids = list[int]()

        rectangle_id = self.canvas.create_rectangle(
            250,
            50,
            1100,
            300,
            fill="#FFBABA",
            outline="#000000"
        )

        label_id = self.canvas.create_text(
            255,
            55,
            text=self.label,
            anchor='nw',
            font=("Helvetica", 20, "bold")
        )
        
        self.close_button = Button(
            text = "Close",
            command = self.close
        )
        self.close_button.place(
            x = 1100,
            y = 50,
            anchor = 'ne'
        )

        self.canvas_ids.append(rectangle_id)
        self.canvas_ids.append(label_id)
    
    def close(self):
        for id in self.canvas_ids:
            self.canvas.delete(id)
        self.close_button.destroy()

        settings.current_opened_chrono = None
