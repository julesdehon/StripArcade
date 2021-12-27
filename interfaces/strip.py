from .colour import Colour


class AddressMode:
    MIRRORED = 0
    CONTINUOUS = 1


class Strip:
    def __init__(self, address_mode=AddressMode.MIRRORED):
        self.address_mode = address_mode

    def set_pixel(self, x: int, colour: Colour):
        pass

    def set_addressing_mode(self, address_mode):
        self.address_mode = address_mode

    def update(self):
        pass

    def clear(self):
        pass

    def __len__(self):
        return 0

