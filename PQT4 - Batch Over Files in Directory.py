import os
from skimage import io
from skimage.util import img_as_ubyte

# You need to change these to valid directories on your computer
input_dir = os.path.dirname('C:/FILES/leaves/')
output_dir = os.path.dirname('C:/FILES/leaves converted/')

for f in os.listdir(input_dir):
    if f.lower().endswith('.png') is True:
        image_gray = io.imread(os.path.join(input_dir, f), as_gray=True)
        image_gray = img_as_ubyte(image_gray)
        output_file = f.replace('.png', '_gray.tiff')
        io.imsave(os.path.join(output_dir, output_file), image_gray)
