class Colour:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    @staticmethod
    def red():
        return Colour(255, 0, 0)

    @staticmethod
    def green():
        return Colour(0, 255, 0)

    @staticmethod
    def blue():
        return Colour(0, 0, 255)

    @staticmethod
    def clear():
        return Colour(0, 0, 0)

