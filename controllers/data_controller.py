import model.chrono_data

class DataController:
    def add_chrono(id: int):
        model.chrono_data.chrono_data.add_data(id, 0)

    def update_chrono_time(id: int, time: int):
        model.chrono_data.chrono_data.update_data(id, time)