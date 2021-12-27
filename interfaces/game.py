from .strip import Strip
from .input_listener import InputListener, Command


class Game:
    def __init__(self, strip: Strip, input_listener: InputListener, audio=None):
        self.strip = strip
        self.input_listener = input_listener
        self.game_should_end = False
        self.game_over_message = ""
        self.audio = audio

    def start(self):
        self.input_listener.set_input_callback(self.input_received)
        self.reset()
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
        if self.audio:
            self.audio.play_sound("sounds/game_over.wav")

    def reset(self):
        self.game_should_end = False
        self.game_over_message = ""

    def display_thumbnail(self):
        pass