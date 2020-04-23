from skimage import io
from skimage.util import img_as_ubyte
import numpy as np
from timeit import timeit

# You need to change this to a valid image file on your computer
input_image = 'C:/FILES/leaf.tif'
# Set this to a valid threshold for your image
threshold = 165

# Function for the (Arr>t)*val method
def mask_to_bool(array, threshold, val):
    return (array > threshold) * val

# Function for the np.where(Arr>t,val,0) method
def mask_w_where(array, threshold, val):
    return np.where(array>threshold, val, 0)

# If you do this on your own, point to valid file paths!
gray_image = io.imread(input_image, as_gray=True)

# Time both methods
t_where = timeit('mask_w_where(gray_image, 150, 255)',
                 'from __main__ import mask_w_where, gray_image, np', number=10) / 10.0
t_bool = timeit('mask_to_bool(gray_image, 150, 255)',
                'from __main__ import mask_to_bool, gray_image', number=10) / 10.0

# Print results
print(f"\nFor an image with dimensions {gray_image.shape}; size {gray_image.size}:")
print(f"np.where(array > threshold, val, 0) averages {round(t_where, 5)} s to run")
print(f"(array * threshold) * val averages {round(t_bool, 5)} s to run")
