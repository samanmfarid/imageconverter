from .gif import GIF
from .jpeg import JPEG
from .png import PNG

from .imageconverter import ImageConverter

class ImageFactory:
    def create_Image(self, name, width, height, *args):
        self.imageConvs_Classes = {
            "GIF": GIF,
            "JPEG": JPEG,
            "PNG": PNG,
        }

        image_Class = self.imageConvs_Classes.get(name)
        return image_Class(name, width, height, *args)
    
    def convert_To(self, imageObject, outputformat, *args):
        if(type(outputformat) is not str):
            raise ValueError("Invalid conversion")
        
        targetImageObject = self.imageConvs_Classes.get(outputformat)

        return targetImageObject(outputformat, imageObject.width, imageObject.height, *args)