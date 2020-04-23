from skimage import io
from skimage.util import img_as_ubyte

# You need to change this to a valid RGB file on your computer
input_image = 'C:/FILES/leaf.tif'

image_color = io.imread(input_image)
io.imshow(image_color); io.show()

image_gray = io.imread(input_image, as_gray=True)
io.imshow(image_gray); io.show()

image_gray = img_as_ubyte(image_gray)
io.imsave('C:/FILES/leaf_gray.tif', image_gray)
