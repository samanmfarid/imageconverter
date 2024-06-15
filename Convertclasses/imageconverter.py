from abc import ABC, abstractmethod

class ImageConverter(ABC): 
    def __init__(self, name, width, height):
        if(width < 0 or height < 0):
            raise ValueError("Pay attention! the numbers cant be nagative")

        self.name = name
        self.width = width
        self.height = height

    @abstractmethod
    def getFinalFileSize(self):
        pass