from pynput import keyboard


class Command:
    LEFT1 = 0
    LEFT2 = 1
    MIDDLE1 = 2
    MIDDLE2 = 3
    RIGHT1 = 1
    RIGHT2 = 2


class InputListener:
    def __init__(self):
        self.callback = lambda x: print("Callback has not been set...")

    def set_input_callback(self, callback):
        self.callback = callback


class KeyboardListener(InputListener):
    def __init__(self):
        super().__init__()
        self.listener = keyboard.Listener(on_press=self.key_pressed)
        self.listener.start()

    def key_pressed(self, key):
        try:
            if key.char == 'a':
                self.callback(Command.MIDDLE2)
            elif key.char == 'd':
                self.callback(Command.MIDDLE1)
        except AttributeError:
            pass
