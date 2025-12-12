import gui.chrono_button, gui.chrono_opened

class GuiController:
    def update_chrono_total_time(id: int, time: int):
        for b in gui.chrono_button.chrono_buttons:
            if b.id == id:
                b.update_total_time_label(time)
                break
