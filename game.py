from colour import Colour
from strip import Strip
from input_listener import InputListener, Command
import time


class Game:
    def __init__(self, strip: Strip, input_listener: InputListener, audio=None):
        self.strip = strip
        self.input_listener = input_listener
        self.game_should_end = False
        self.game_over_message = ""
        self.audio = audio

    def start(self):
        self.input_listener.set_input_callback(self.input_received)
        while True:
            self.advance()
            if self.game_should_end:
                break
        print(f"Game Over: {self.game_over_message}")

    def advance(self):
        pass

    def input_received(self, command: Command):
        pass

    def game_over(self, message):
        self.game_should_end = True
        self.game_over_message = message


class ClassicPong(Game):
    TIME_UNIT = 0.25
    RETURN_WINDOW = 0.2

    def __init__(self, strip: Strip, input_listener: InputListener, audio=None):
        super().__init__(strip, input_listener, audio=audio)
        self.last_update_time = time.time()
        self.start_time = time.time()
        self.pos = 0
        self.speed = 1
        for i in range(len(self.strip)):
            if self.is_in_end1(i) or self.is_in_end2(i):
                self.strip.set_pixel(i, Colour.blue())
            else:
                self.strip.set_pixel(i, Colour.clear())
        self.strip.set_pixel(self.pos, Colour.red())
        self.strip.update()
        self.num_rebounds = 1
        self.prev_col = Colour.clear()

    def advance(self):
        if (time.time() - self.last_update_time) < (ClassicPong.TIME_UNIT / abs(self.speed)):
            return

        self.strip.update()
        self.last_update_time = time.time()
        if self.is_in_end1() or self.is_in_end2():
            self.strip.set_pixel(self.pos, Colour.blue())
        else:
            self.strip.set_pixel(self.pos, Colour.clear())
        self.pos += self.unit_speed()
        if not (0 <= self.pos < len(self.strip)):
            self.game_over("Ball went out of bounds!")
            return
        self.strip.set_pixel(self.pos, Colour.red())

    def input_received(self, command: Command):
        if command == Command.MIDDLE1:
            if self.is_in_end1():
                self.num_rebounds += 1
                self.send_towards_end2()
                if self.audio:
                    self.audio.play_sound("pong.mp3")
            else:
                self.game_over("Player 1 swung and missed!")
        elif command == Command.MIDDLE2:
            if self.is_in_end2():
                self.num_rebounds += 1
                self.send_towards_end1()
                if self.audio:
                    self.audio.play_sound("pong.mp3")
            else:
                self.game_over("Player 2 swung and missed!")
        else:
            return
        if self.num_rebounds % 2 == 0:
            self.speed += self.unit_speed()

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

