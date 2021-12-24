from typing import List

from strip import Strip
from input_listener import InputListener, Command
from audio import SoundDevice
from game import Game


class Menu:
    def __init__(self, strip: Strip, input_listener: InputListener, audio: SoundDevice, games: List[Game]):
        self.strip = strip
        self.input = input_listener
        self.audio = audio
        self.input.set_input_callback(self.key_pressed)
        self.games = games
        self.current_game = 0
        print("Currently selected game 0")

    def start(self):
        while True:
            pass

    def key_pressed(self, key):
        if key == Command.RIGHT1 or key == Command.RIGHT2:
            self.current_game = (self.current_game + 1) % len(self.games)
            print(f"Now selected game {self.current_game}")
        elif key == Command.LEFT1 or key == Command.LEFT2:
            self.current_game = (self.current_game - 1) % len(self.games)
            print(f"Now selected game {self.current_game}")
        else:
            print(f"Launching game {self.current_game}")
            self.games[self.current_game].start()
            self.input.set_input_callback(self.key_pressed)
