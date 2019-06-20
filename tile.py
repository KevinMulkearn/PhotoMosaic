from PIL import Image
import glob
from random import randint

scl = 256  # Individual image size

files = glob.glob("C:/Users/kevin/OneDrive/Pictures/PreProcessedPictures/*.JPG")
filesSize = len(files)

index = randint(0, filesSize-1)
ImgName = files[index]

imgFullSize = Image.open(ImgName)
width1, height1 = imgFullSize.size
print("Original Size: ", width1, height1)

tileImg = imgFullSize.resize((scl, scl))
width2, height2 = tileImg.size
print("Tile Size: ", width2, height2)
tileImg.show()
tileImg.save("TileTest.jpg")
