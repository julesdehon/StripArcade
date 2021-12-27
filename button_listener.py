from interfaces.input_listener import InputListener, Command
from threading import Thread
import time
import RPi.GPIO as GPIO  # Import Raspberry Pi GPIO library
GPIO.setmode(GPIO.BCM)  # Use GPIO pin numbering


class ButtonListener(InputListener):
    def __init__(self, precision=0.15):
        super().__init__()
        self.precision = precision
        GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(8, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(9, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        self.worker = Thread(target=self.start, daemon=True)
        self.worker.start()

    def start(self):
        while True:
            if not GPIO.input(5):
                self.callback(Command.LEFT1)
                time.sleep(self.precision)

            if not GPIO.input(11):
                self.callback(Command.RIGHT1)
                time.sleep(self.precision)

            if not GPIO.input(8):
                self.callback(Command.MIDDLE1)
                time.sleep(self.precision)

            if not GPIO.input(25):
                self.callback(Command.LEFT2)
                time.sleep(self.precision)

            if not GPIO.input(9):
                self.callback(Command.RIGHT2)
                time.sleep(self.precision)

            if not GPIO.input(10):
                self.callback(Command.MIDDLE2)
                time.sleep(self.precision)

