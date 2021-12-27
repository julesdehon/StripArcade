from interfaces.colour import Colour
from interfaces.strip import Strip, AddressMode
import board
import neopixel


class NeoPixelStrip(Strip):
    def __init__(self):
        super().__init__()
        self.pixels = neopixel.NeoPixel(
            board.D12, 288, brightness=0.2, auto_write=False, pixel_order=neopixel.GRB
        )

    def set_pixel(self, x: int, colour: Colour):
        if self.address_mode == AddressMode.MIRRORED:
            self.pixels[x] = (colour.r, colour.g, colour.b)
            self.pixels[len(self.pixels) - 1 - x] = (colour.r, colour.g, colour.b)
        elif self.address_mode == AddressMode.CONTINUOUS:
            self.pixels[x] = (colour.r, colour.g, colour.b)

    def update(self):
        self.pixels.show()

    def clear(self):
        for i in range(len(self.pixels)):
            self.pixels[i] = (0, 0, 0)
        self.pixels.show()

    def __len__(self):
        if self.address_mode == AddressMode.MIRRORED:
            return 288 // 2
        elif self.address_mode == AddressMode.CONTINUOUS:
            return 288
        return 288
