class Command:
    LEFT1 = 0
    LEFT2 = 1
    MIDDLE1 = 2
    MIDDLE2 = 3
    RIGHT1 = 4
    RIGHT2 = 5


class InputListener:
    def __init__(self):
        self.callback = lambda x: print("Callback has not been set...")

    def set_input_callback(self, callback):
        print("changing the input callback!")
        self.callback = callback

