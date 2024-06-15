
from .imageconverter import ImageConverter

class GIF(ImageConverter):
    def __init__(self, name, width, height ):
        super().__init__(name, width, height)
        
    def getFinalFileSize(self):
        finalValue = self.width * self.height 
       
        
    
