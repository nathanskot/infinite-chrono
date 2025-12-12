from tkinter import Tk, Canvas, Button, Menu, StringVar
from gui.chrono_opened import ChronoOpened
from controllers.data_controller import DataController
import settings
import utils

class ChronoButton:
    def __init__(self, window: Tk, canvas: Canvas):
        global chrono_buttons

        self.id = settings.total_created_buttons + 1
        DataController.add_chrono(self.id)
        
        self.x = settings.chrono_button_x
        self.y = settings.chrono_button_y
        self.name_label = f"New chrono {self.id}"

        self.root = window
        self.canvas = canvas

        self.total_time_str = StringVar(
            master = self.root,
            value = f"{self.name_label}" + '\n' + "00:00:00"
        )

        self.button = Button(
            textvariable = self.total_time_str
        )
        self.button.place(
            x = self.x,
            y = self.y,
            width = 160,
            height = 50,
        )

        chrono_buttons.append(self)
        self.popup()
        self.button.bind("<Button-3>", self.do_popup)
        self.button.bind("<Button-1>", self.open_chrono)

        settings.total_created_buttons += 1
        settings.chrono_button_y += 55
    
    def __del__(self):
        print("Deleting chrono")

    def popup(self):
        self.popup_menu = Menu(
            self.root,
            tearoff = 0
        )
        self.popup_menu.add_command(
            label = "Rename",
            command = lambda:self.rename("renamed!")
        )
        self.popup_menu.add_command(
            label = "Delete",
            command = self.delete
        )
    
    def do_popup(self, event):
        try:
            self.popup_menu.tk_popup(
                event.x_root,
                event.y_root
            )
        finally:
            self.popup_menu.grab_release()

    def rename(self, s:str):
        self.name_label = s
        self.button.config(text = s)
    
    def delete(self):
        global chrono_buttons

        self.button.destroy()
        pos = chrono_buttons.index(self)
        chrono_buttons.remove(self)

        for chrono in chrono_buttons[pos:]:
            chrono.y -= 55
            chrono.button.place(x = chrono.x, y = chrono.y)

        settings.chrono_button_y -= 55

        if settings.current_opened_chrono is not None:
            if settings.current_opened_chrono.id == self.id:
                settings.current_opened_chrono.close()
    
    def open_chrono(self, event):
        if settings.current_opened_chrono is None:
            settings.current_opened_chrono = ChronoOpened(self.id, self.name_label, self.root, self.canvas)
        elif settings.current_opened_chrono.id != self.id:
            settings.current_opened_chrono.close()
            settings.current_opened_chrono = ChronoOpened(self.id, self.name_label, self.root, self.canvas)
    
    def update_total_time_label(self, time: int):
        self.total_time_str.set(f"{self.name_label}" + '\n' + utils.seconds_to_formatted_time(time))

chrono_buttons = list[ChronoButton]()
