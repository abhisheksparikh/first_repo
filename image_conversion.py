from PIL import Image
import numpy as np

im = np.array(Image.open('D:\\FourierImages\\raw_images\\vivek_portrait.png').convert('L').resize((256, 256)))
print(type(im))

th = 128
im_bool = im > th
im_bin_128 = (im > th) * 255

im_bin_64 = (im > 100) * 255
im_bin_192 = (im > 192) * 255

im_bin = np.concatenate((im_bin_64, im_bin_128, im_bin_192), axis=1)
Image.fromarray(np.uint8(im_bin)).save('D:\\FourierImages\\raw_images\\vivek_portrait_BW.png')
