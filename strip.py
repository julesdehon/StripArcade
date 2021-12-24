from colour import Colour


class Strip:
    def set_pixel(self, x: int, colour: Colour):
        pass

    def update(self):
        pass

    def __len__(self):
        return 0


class AsciiStrip(Strip):
    def __init__(self, size):
        self.strip = [Colour.clear()] * size

    def set_pixel(self, x: int, colour: Colour):
        self.strip[x] = colour

    def update(self):
        print(''.join(map(lambda col: '-' if (col.r == 0 and col.g == 0 and col.b == 0) else 'X', self.strip)),
              end="\r")

    def __len__(self):
        return len(self.strip)

