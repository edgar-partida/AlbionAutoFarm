from src.util.Constants import MONITOR_NUMBER


class Dimension:
    def __init__(self, top, left, width, height):
        self.top = top
        self.left = left
        self.width = width
        self.height = height
        self.monitor = MONITOR_NUMBER

    def to_json(self):
        return {
            'top': self.top,
            'left': self.left,
            'width': self.width,
            'height': self.height,
            'monitor': 1
        }
