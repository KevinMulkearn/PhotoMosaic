from PIL import Image, ImageDraw
import glob

Image.MAX_IMAGE_PIXELS = None  # Remove pixel size limit

################################# Edit Here #################################
scl = 256  # Individual image size (64)
res_scl = 4  # Original image size scale up factor (3)
blendFactor = 0.4  # Percentage of original overlayed (for colour effect) (0.4)
#############################################################################

allImagesName = []
brightness = []
brightImages = [0] * 256
allImages = []

originalImg = Image.open("TestPic.jpg")

width, height = originalImg.size

width = width*res_scl
height = height*res_scl

originalImg = originalImg.resize((width, height), Image.LANCZOS)  # increase size to make tiles clearer
originalImg.save("OriginalScaled.jpg")

w = round(width / scl)
h = round(height / scl)

smaller = originalImg.resize((w, h))

draw = ImageDraw.Draw(originalImg)

files = glob.glob("C:/Users/kevin/OneDrive/Pictures/PreProcessedPictures/*.JPG")

for myFile in files:
    allImagesName.append(myFile)
    folderImage = Image.open(myFile)

    resizedImg = folderImage.resize((scl, scl), Image.LANCZOS)
    allImages.append(resizedImg)
    im_grey = resizedImg.convert('LA')  # Convert to grayscale
    fldImgWidth, fldImgHeight = resizedImg.size

    total = 0
    for x1 in range(0, fldImgWidth):
        for y1 in range(0, fldImgHeight):
            total += im_grey.getpixel((x1, y1))[0]

    mean = total / (fldImgWidth * fldImgHeight)
    brightness.append(mean)

for i in range(0, 256):
    record = 256
    for j in range(0, len(brightness)):
        diff = abs(i - brightness[j])
        if (diff < record):
            record = diff
            brightImages[i] = allImages[j]

for x in range(0, w):
    for y in range(0, h):
        xy = (x, y)
        pixel_rgb = smaller.getpixel(xy)

        r, g, b = pixel_rgb
        grey = int(round(0.2989 * r + 0.5870 * g + 0.1140 * b))

        #draw.rectangle(((x*scl, y*scl), (x*scl+scl, y*scl+scl)), fill=pixel_rgb, outline=0)
        originalImg.paste(brightImages[grey], (x * scl, y * scl, x * scl + scl, y * scl + scl))

# originalImg.show()
originalImg.save("TiledRaw.jpg")

rawTile = Image.open("TiledRaw.jpg")
colourImage = Image.open("OriginalScaled.jpg")
blendedImg = Image.blend(rawTile, colourImage, blendFactor)
blendedImg.save("Mosaic.jpg")