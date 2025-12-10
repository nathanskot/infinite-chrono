from tkinter import Tk, Canvas, Button, Menu
from chrono import Chrono
import settings

class ChronoButton:
    def __init__(self, window: Tk, canvas: Canvas):
        global total_created_buttons
        global chronos
        global chrono_button_y

        self.id = total_created_buttons + 1
        self.x = chrono_button_x
        self.y = chrono_button_y
        self.label = f"New chrono {self.id}"

        self.root = window
        self.canvas = canvas
        self.button = Button(
            text=self.label
        )
        self.button.place(
            x=self.x,
            y=self.y,
            width=160,
            height=50,
        )

        chronos.append(self)
        self.popup()
        self.button.bind("<Button-3>", self.do_popup)
        self.button.bind("<Button-1>", self.open_chrono)

        total_created_buttons += 1
        chrono_button_y += 55
    
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
        self.label = s
        self.button.config(text = s)
    
    def delete(self):
        global chronos
        global chrono_button_y

        self.button.destroy()
        pos = chronos.index(self)
        chronos.remove(self)

        for chrono in chronos[pos:]:
            chrono.y -= 55
            chrono.button.place(x=chrono.x, y=chrono.y)

        chrono_button_y -= 55

        if settings.current_opened_chrono.id == self.id:
            settings.current_opened_chrono.close()
    
    def open_chrono(self, event):
        if settings.current_opened_chrono == None:
            settings.current_opened_chrono = Chrono(self.id, self.label, self.root, self.canvas)
        elif settings.current_opened_chrono.id != self.id:
            settings.current_opened_chrono.close()
            settings.current_opened_chrono = Chrono(self.id, self.label, self.root, self.canvas)

total_created_buttons = 0
chronos = list[ChronoButton]()
chrono_button_x = 20
chrono_button_y = 200
