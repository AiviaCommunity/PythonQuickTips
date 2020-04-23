import numpy as np
import matplotlib.pyplot as plt
from skimage import io
from skimage.util import img_as_ubyte

# You need to change this to a valid image file on your computer
input_image = 'C:/FILES/leaf.tif'

gray_image = io.imread(input_image, as_gray=True)
gray_image = img_as_ubyte(gray_image)
io.imshow(gray_image); io.show()

print(f"Image shape: {gray_image.shape} and size: {gray_image.size}")
print(f"Unraveled shape: {gray_image.ravel().shape} and size: {gray_image.ravel().size}")

ax = plt.hist(gray_image.ravel(), bins=256)
plt.show()

approx_median = np.percentile(gray_image, 50)

ax = plt.hist(gray_image.ravel(), bins=256)
plt.axvline(approx_median, color='orange')
plt.show()

quartiles = [25, 50, 75]
ax = plt.hist(gray_image.ravel(), bins=256)
for q in np.percentile(gray_image, quartiles):
    plt.axvline(q, color='orange')
plt.show()
