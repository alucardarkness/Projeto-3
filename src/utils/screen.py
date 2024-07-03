from pygame import surface, display
class Screen:
    def __init__(self, width:int=800, height:int=800, resolution:float=1) -> None:
        self.width = width
        self.height = height
        self.resolution = resolution
        self.surface = display.set_mode((height, width))