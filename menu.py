from typing import List

from interfaces.strip import Strip, AddressMode
from interfaces.input_listener import InputListener, Command
from interfaces.sound_player import SoundPlayer
from interfaces.game import Game
from interfaces.colour import Colour
import time


class Menu:
    def __init__(self, strip: Strip, input_listener: InputListener, audio: SoundPlayer, games: List[Game]):
        self.strip = strip
        self.input = input_listener
        self.audio = audio
        self.input.set_input_callback(self.key_pressed)
        self.games = games
        self.current_game = 0
        self.start_game = False
        print("Currently selected game 0")

    def start(self):
        self.strip.clear()
        old_game = self.current_game
        self.games[self.current_game].display_thumbnail()
        while True:
            if old_game != self.current_game:
                self.games[self.current_game].display_thumbnail()
                old_game = self.current_game
            if self.start_game:
                self.start_game = False
                self.start_game_animation()
                self.games[self.current_game].start()
                self.input.set_input_callback(self.key_pressed)
                self.game_over_animation()
                self.strip.clear()
                self.games[self.current_game].display_thumbnail()

    def start_game_animation(self):
        self.strip.clear()
        self.strip.set_addressing_mode(AddressMode.MIRRORED)
        mid_point = len(self.strip) // 2 + 1
        for i in range(len(self.strip) // 2):
            self.strip.set_pixel(mid_point - i, Colour.green())
            self.strip.set_pixel(mid_point + i, Colour.green())
            self.strip.update()
        self.flash_strip(5, Colour.green())

    def game_over_animation(self):
        self.strip.clear()
        self.strip.set_addressing_mode(AddressMode.MIRRORED)
        self.flash_strip(5, Colour.red())

    def flash_strip(self, times, colour):
        for _ in range(times):
            for i in range(len(self.strip)):
                self.strip.set_pixel(i, colour)
            self.strip.update()
            time.sleep(0.05)

            for i in range(len(self.strip)):
                self.strip.set_pixel(i, Colour.clear())
            self.strip.update()
            time.sleep(0.05)

    def key_pressed(self, key):
        if key == Command.RIGHT1 or key == Command.RIGHT2:
            self.current_game = (self.current_game + 1) % len(self.games)
            self.audio.play_sound("sounds/slide.wav")
            print(f"Now selected game {self.current_game}")
        elif key == Command.LEFT1 or key == Command.LEFT2:
            self.current_game = (self.current_game - 1) % len(self.games)
            self.audio.play_sound("sounds/slide.wav")
            print(f"Now selected game {self.current_game}")
        else:
            print(f"Launching game {self.current_game}")
            self.start_game = True
