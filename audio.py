from playsound import playsound
import threading


class SoundDevice:
    def play_sound(self, sound_path: str):
        pass


class ComputerSoundPlayer(SoundDevice):
    def play_sound(self, sound_path: str):
        threading.Thread(target=playsound, args=(sound_path,), daemon=True).start()
