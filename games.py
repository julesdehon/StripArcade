from interfaces.game import Game
from interfaces.colour import Colour
from interfaces.strip import Strip, AddressMode
from interfaces.input_listener import InputListener, Command
import time


class ClassicPong(Game):
    TIME_UNIT = 0.025
    RETURN_WINDOW = 0.2  # What proportion of the strip can the ball be returned in?
    RETURN_WINDOW_COLOUR = Colour(0, 0, 10)

    def __init__(self, strip: Strip, input_listener: InputListener, audio=None, initial_speed=1,
                 speedup_every=5):
        super().__init__(strip, input_listener, audio=audio)
        self.strip.set_addressing_mode(AddressMode.MIRRORED)
        self.pos = 0
        self.initial_speed = initial_speed
        self.base_speed = initial_speed
        self.speed = initial_speed
        self.speedup_every = speedup_every
        for i in range(len(self.strip)):
            if self.is_in_end1(i) or self.is_in_end2(i):
                self.strip.set_pixel(i, self.RETURN_WINDOW_COLOUR)
            else:
                self.strip.set_pixel(i, Colour.clear())
        self.strip.set_pixel(self.pos, Colour.red())
        self.strip.update()
        self.num_rebounds = 0
        self.prev_col = Colour.clear()

    def advance(self):
        if self.is_in_end1() or self.is_in_end2():
            self.strip.set_pixel(self.pos, self.RETURN_WINDOW_COLOUR)
        else:
            self.strip.set_pixel(self.pos, Colour.clear())
        self.pos += self.speed
        if not (0 <= self.pos < len(self.strip)):
            self.game_over("Ball went out of bounds!")
            return
        self.strip.set_pixel(self.pos, Colour.red())
        self.strip.update()
        time.sleep(self.TIME_UNIT)

    def input_received(self, command: Command):
        if command == Command.MIDDLE1:
            if self.is_in_end1():
                self.num_rebounds += 1
                self.send_towards_end2()
                if self.audio:
                    self.audio.play_sound("sounds/impact.wav")
            else:
                self.game_over("Player 1 swung and missed!")
        elif command == Command.MIDDLE2:
            if self.is_in_end2():
                self.num_rebounds += 1
                self.send_towards_end1()
                if self.audio:
                    self.audio.play_sound("sounds/impact.wav")
            else:
                self.game_over("Player 2 swung and missed!")
        else:
            return
        if self.num_rebounds > 0 and self.num_rebounds % self.speedup_every == 0:
            if self.audio:
                self.audio.play_sound("sounds/level-up.wav")
            self.base_speed += self.unit_speed()

    def is_in_end1(self, pos=None):
        pos = pos if pos else self.pos
        return pos < len(self.strip) * self.RETURN_WINDOW

    def is_in_end2(self, pos=None):
        pos = pos if pos else self.pos
        return pos >= len(self.strip) - len(self.strip) * self.RETURN_WINDOW

    def send_towards_end2(self):
        self.speed = abs(self.speed)

    def send_towards_end1(self):
        self.speed = -abs(self.speed)

    def unit_speed(self):
        return int(self.speed / abs(self.speed))

    def reset(self):
        super().reset()
        self.strip.set_addressing_mode(AddressMode.MIRRORED)
        self.pos = 0
        self.speed = self.initial_speed
        for i in range(len(self.strip)):
            if self.is_in_end1(i) or self.is_in_end2(i):
                self.strip.set_pixel(i, self.RETURN_WINDOW_COLOUR)
            else:
                self.strip.set_pixel(i, Colour.clear())
        self.strip.set_pixel(self.pos, Colour.red())
        self.strip.update()
        self.num_rebounds = 1
        self.prev_col = Colour.clear()

    def display_thumbnail(self):
        for i in range(len(self.strip)):
            if self.is_in_end1(i) or self.is_in_end2(i):
                self.strip.set_pixel(i, self.RETURN_WINDOW_COLOUR)
            else:
                self.strip.set_pixel(i, Colour.clear())
        self.strip.set_pixel(len(self.strip) // 2, Colour.red())
        self.strip.update()
