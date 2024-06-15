
from .imageconverter import ImageConverter

class PNG(ImageConverter):
    def __init__(self, name, width, height ):
        super().__init__(name, width, height)
        
    def getFinalFileSize(self):
        finalValue = self.width * self.height 
       
        
    
