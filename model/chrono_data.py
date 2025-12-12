from controllers.gui_controller import GuiController

# TODO Handle all id assignation in this class
class ChronoData:
    def __init__(self):
        self._data = {}
    
    def get_data(self):
        return self._data
    
    def get_data(self, id: int):
        return self._data.get(id)
    
    def add_data(self, id: int, time: int):
        if id not in self._data:
            self._data[id] = time
        # TODO Handle error return
            
    
    def update_data(self, id: int, time: int):
        if id in self._data:
            self._data[id] = time
            GuiController.update_chrono_total_time(id, time)
        # TODO Handle error return
    
    def remove_data(self, id: int):
        if id in self._data:
            self._data.pop(id)
        # TODO Handle error return

def init():
    global chrono_data
    chrono_data = ChronoData()