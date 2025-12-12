from tkinter import Tk, Canvas, Button, Label, DoubleVar, StringVar
from controllers import data_controller
import settings
import utils

class ChronoOpened:
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
            fill = "#FFBABA",
            outline = "#000000"
        )

        label_id = self.canvas.create_text(
            255,
            55,
            text = self.label,
            anchor = 'nw',
            font = ("Helvetica", 20, "bold")
        )

        self.start_button = Button(
            text = "Start chrono",
            command = self.start
        )
        self.start_button.place(
            x = 984,
            y = 50,
            anchor = 'ne'
        )

        self.stop_button = Button(
            text = "Stop chrono",
            command = self.stop
        )
        self.stop_button.place(
            x = 1060,
            y = 50,
            anchor = 'ne'
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

        self.timer = 0
        self.timer_str = StringVar(master = self.root, value = "00:00:00")
        self.is_running = False

        self.timer_display = Label(
            self.root,
            textvariable = self.timer_str,
            font = ("Helvetica", 40, "bold"),
            background = "#FFBABA"
        )
        self.timer_display.place(
            x = 550,
            y = 140,
            anchor = 'nw'
        )

        self.canvas_ids.append(rectangle_id)
        self.canvas_ids.append(label_id)
    
    def start(self):
        if self.is_running:
            return
        self.is_running = True
        self.increment_session_time()
    
    def stop(self):
        self.is_running = False

    def close(self):
        self.is_running = False

        data_controller.DataController.update_chrono_time(self.id, self.timer)

        for id in self.canvas_ids:
            self.canvas.delete(id)
        self.start_button.destroy()
        self.stop_button.destroy()
        self.close_button.destroy()
        self.timer_display.destroy()

        settings.current_opened_chrono = None
    
    def increment_session_time(self):
        self.timer += 1
        self.timer_str.set(utils.seconds_to_formatted_time(self.timer))
        if self.is_running:
            self.root.after(1000, self.increment_session_time)
