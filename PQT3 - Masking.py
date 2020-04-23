import numpy as np
from skimage import io
from skimage.util import img_as_ubyte

# You need to change this to a valid image file on your computer
input_image = 'C:/FILES/leaf.tif'
# Set this to a valid threshold for your image
threshold = 165

gray_image = io.imread(input_image, as_gray=True)
gray_image = img_as_ubyte(gray_image)

binary_where = np.where(gray_image > threshold, 255, 0)
binary_where = img_as_ubyte(binary_where)

io.imshow(binary_where); io.show()

io.imsave('C:/FILES/leaf_thresholded.tif', binary_where)
