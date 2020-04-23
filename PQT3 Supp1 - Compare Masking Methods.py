import numpy as np
import matplotlib.pyplot as plt
from skimage import io
from skimage.util import img_as_ubyte

# You need to change this to a valid image file on your computer
input_image = 'C:/FILES/leaf.tif'
# Set this to a valid threshold for your image
threshold = 165

# Read the image
gray_image = io.imread(input_image, as_gray=True)
gray_image = img_as_ubyte(gray_image)

# Thresholding is as easy as performing a comparison on an array
binary_bool = gray_image > threshold

# To get int output instead of bool, multiply by a mask value
binary_multiple = (gray_image > threshold) * 255

# np.where produces an equivalent result, but is slightly faster
binary_where = np.where(gray_image > threshold, 255, 0)


# Show all the images to see that they are essentially the same!
fig, ax = plt.subplots(1, 3)

ax[0].imshow(binary_bool)
ax[0].set_title(f"Arr>t  ->  {binary_bool.dtype}")

ax[1].imshow(binary_multiple)
ax[1].set_title(f"(Arr>t)*255  ->  {binary_multiple.dtype}")

ax[2].imshow(binary_where)
ax[2].set_title(f"np.where(Arr>t,255,0)  ->  {binary_where.dtype}")

for a in ax:
    a.axis('off')
    
plt.show()
