from Convertclasses.factory import ImageConverter

imageFactory = ImageConverter()

img_GIF = imageFactory.create_Image('GIF', 640 , 480 )
print(f"GIF Image Size:  {img_GIF.getFinalFileSize()} bytes.")

img_JPEG = imageFactory.create_Image('JPEG', 1280 , 720 )
print(f"JPEG Image Size:  {img_JPEG.getFinalFileSize()} bytes.")

img_PNG = imageFactory.create_Image('PNG', 1920 , 1080 )
print(f"PNG Image Size:  {img_PNG.getFinalFileSize()} bytes.")

