from strip import AsciiStrip
from game import ClassicPong
from input_listener import KeyboardListener, InputListener
from gui_adapters import get_gui_adapters
from audio import ComputerSoundPlayer


def main():
    # strip = AsciiStrip(40)
    strip, input_listener = get_gui_adapters(20)
    sound_device = ComputerSoundPlayer()
    # input_listener = KeyboardListener()
    game = ClassicPong(strip, input_listener, audio=sound_device)
    game.start()


if __name__ == '__main__':
    main()
