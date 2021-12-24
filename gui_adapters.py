import PySimpleGUI as sg
from colour import Colour
from strip import Strip
from input_listener import InputListener, Command, KeyboardListener
from threading import Thread


class GuiStrip(Strip):
    def __init__(self, size, input_listener):
        layout = [[sg.Text('Some text on Row 1')],
                  [sg.Graph(canvas_size=(400, 400), graph_bottom_left=(0, 0), graph_top_right=(400, 400),
                            background_color='white', key='graph')]]
        self.window = sg.Window('Strip Arcade', layout, return_keyboard_events=True, finalize=True)
        graph = self.window['graph']
        self.leds = []
        for i in range(size):
            y_bottom = 20 + (i * (400 - 40) / size)
            y_top = y_bottom + 20
            self.leds.append(graph.DrawRectangle((190, y_bottom), (210, y_top), fill_color='black'))
        self.input_listener = input_listener
        Thread(target=self.listener_event_loop, daemon=True).start()

    def set_pixel(self, x: int, colour: Colour):
        c = f"#{colour.r:02X}{colour.g:02X}{colour.b:02X}"
        self.window['graph'].TKCanvas.itemconfig(self.leds[x], fill=c)

    def update(self):
        self.window.finalize()
        print("Finalized")
        # event, values = self.window.read(0)
        # if event == "w":
        #     self.input_listener.callback(Command.MIDDLE1)
        # elif event == "s":
        #     self.input_listener.callback(Command.MIDDLE2)

    def listener_event_loop(self):
        while True:
            event, values = self.window.read(0)
            print("Read")
            if event == "w":
                self.input_listener.callback(Command.MIDDLE1)
            elif event == "s":
                self.input_listener.callback(Command.MIDDLE2)
            elif event == "d":
                self.input_listener.callback(Command.RIGHT1)
            elif event == "f":
                self.input_listener.callback(Command.RIGHT2)
            elif event == "a":
                self.input_listener.callback(Command.LEFT1)
            elif event == "q":
                self.input_listener.callback(Command.LEFT2)

    def __del__(self):
        self.window.close()

    def __len__(self):
        return 20


def get_gui_adapters(size):
    listener = InputListener()
    # listener = KeyboardListener()
    strip = GuiStrip(size, listener)
    return strip, listener
