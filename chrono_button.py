from tkinter import Tk, Button, Menu

total_created_buttons = 0
chronos = []
chrono_x = 20
chrono_y = 200

class ChronoButton:
    def __init__(self, window: Tk):
        global total_created_buttons
        global chronos
        global chrono_x
        global chrono_y

        self.root = window
        self.button = Button(
            text=f"New chrono {total_created_buttons + 1}"
        )
        self.button.place(
            x=chrono_x,
            y=chrono_y,
            width=160,
            height=50,
        )
        #self.button.pack()

        chronos.append(self)
        self.popup()
        self.button.bind("<Button-3>", self.do_popup)

        total_created_buttons += 1
        chrono_y += 55
    
    def __del__(self):
        print("Deleting chrono")

    def popup(self):
        self.popup_menu = Menu(
            self.root,
            tearoff = 0
        )
        self.popup_menu.add_command(
            label = "Rename",
            command = lambda:self.do_rename("renamed!")
        )
        self.popup_menu.add_command(
            label = "Delete",
            command = self.do_delete
        )
    
    def do_popup(self, event):
        try:
            self.popup_menu.tk_popup(
                event.x_root,
                event.y_root
            )
        finally:
            self.popup_menu.grab_release()

    def do_rename(self, s:str):
        self.button.config(text = s)
    
    def do_delete(self):
        global chronos
        global chrono_y

        self.button.destroy()
        chronos.remove(self)

        chrono_y -= 55