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

# Open base image
originalImg = Image.open("TestPic.jpg")
# Get dimensions
width, height = originalImg.size

# Scale up original image (increase size to make tiles clearer)
width = width*res_scl
height = height*res_scl
originalImg = originalImg.resize((width, height), Image.LANCZOS)
originalImg.save("OriginalScaled.jpg")

# Scale down image (used to map each pixel to an image tile)
scaled_w = round(width / scl)
scaled_h = round(height / scl)
smaller = originalImg.resize((scaled_w, scaled_h))

draw = ImageDraw.Draw(originalImg)

# Get all images in folder
files = glob.glob("C:/Users/kevin/OneDrive/Pictures/PreProcessedPictures/*.JPG")

for myFile in files:
    # List of Image names
    allImagesName.append(myFile)
    # Open image image
    folderImage = Image.open(myFile)
    # Scale down image
    resizedImg = folderImage.resize((scl, scl), Image.LANCZOS)
    # Add image to list
    allImages.append(resizedImg)
    # Convert to grayscale
    greyImg = resizedImg.convert('LA')

    # Find average brightness value of image
    total = 0
    # check every pixel
    for x1 in range(0, scl):
        for y1 in range(0, scl):
            total += greyImg.getpixel((x1, y1))[0]
    mean = total / (scl * scl)
    # Add average brightness value to list
    brightness.append(mean)

# Assign an image to each brightness value
for i in range(0, 256):  # For all levels
    record = 256
    for j in range(0, len(brightness)):  # For all average image brightness values
        diff = abs(i - brightness[j])
        if diff < record:
            # Find closest brightness
            record = diff
            # Assign image to brightness level
            brightImages[i] = allImages[j]

# Paste Image tile into correct position
for x in range(0, scaled_w):
    for y in range(0, scaled_h):
        # Pixel position
        xy = (x, y)
        # Get pixel value
        pixel_rgb = smaller.getpixel(xy)
        # Get RGB values
        r, g, b = pixel_rgb
        # Convert RGB to greyscale value
        grey = int(round(0.2989 * r + 0.5870 * g + 0.1140 * b))
        # Draw rectangle with RGB value
        #draw.rectangle(((x*scl, y*scl), (x*scl+scl, y*scl+scl)), fill=pixel_rgb, outline=0)
        # Paste Image with same brightness value
        originalImg.paste(brightImages[grey], (x * scl, y * scl, x * scl + scl, y * scl + scl))

# Save tiled image
originalImg.save("TiledRaw.jpg")
# Overall tiled image with original scaled image (better colour)
rawTile = Image.open("TiledRaw.jpg")
colourImage = Image.open("OriginalScaled.jpg")
blendedImg = Image.blend(rawTile, colourImage, blendFactor)
# Save final image
blendedImg.save("Mosaic.jpg")
