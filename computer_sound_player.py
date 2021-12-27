from pygame import mixer
from interfaces.sound_player import SoundPlayer


class ComputerSoundPlayer(SoundPlayer):
    def __init__(self):
        mixer.init()

    def play_sound(self, sound_path: str):
        sound = mixer.Sound(sound_path)
        sound.play()
