# PhotoMosaic
Create image from a matrix of smaller images

**originalImg** is the image you want to recreate into a mosaic. This is in the same folder as main.py.

**files** is the folder of all images to be used as tiles in the final image. Be sure to add correct extension (e.g. .JPG).

**Mosaic.jpg** is the name of the output image saved. This is saved in the same location as main.py.

**scl** is the tile dimersions in pixels (e.g. 64 x 64) res_scl is the factor in which the original image size is scaled up by (to increase tile image quality).

**res_scl** is the scale up factor size of the original image. 

Note: A lot of images are loaded into memory here, so script may fail. To fix this:

1. Decrease the number of images in folder
2. Decrease the tile size ('scl')
3. Decrease the image scale size ('res_scl')
4. Write more efficient code than this :)
