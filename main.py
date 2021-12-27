from games import ClassicPong
from menu import Menu
from computer_sound_player import ComputerSoundPlayer
from button_listener import ButtonListener
from rgb_strip import NeoPixelStrip


def main():
    strip = NeoPixelStrip()
    input_listener = ButtonListener()
    sound_device = ComputerSoundPlayer()
    games = [
        ClassicPong(strip, input_listener, audio=sound_device, initial_speed=2)
    ]
    menu = Menu(strip, input_listener, sound_device, games)
    menu.start()


if __name__ == '__main__':
    main()
