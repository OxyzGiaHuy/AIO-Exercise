import matplotlib.image as mpimg
import numpy as np

folder_path = "./AIO-Exercise/Module_2/Week_1/assets/"
img_path = folder_path + "dog.jpeg"
img = mpimg.imread(img_path)

# cau 12 - Lightness
gray_img_01 = (np.max(img, axis=2) + np.min(img, axis=2)) / 2
mpimg.imsave(folder_path + "dog_grey_1.jpeg", gray_img_01)
print(gray_img_01[0, 0])


# cau 13 - Average
gray_img_02 = np.mean(img, axis=2)
mpimg.imsave(folder_path + "dog_grey_2.jpeg", gray_img_02)
print(gray_img_02[0, 0])


# cau 14 - Luminosity
gray_img_03 = img[:, :, 0]*0.21 + img[:, :, 1]*0.72 + img[:, :, 2]*0.07
mpimg.imsave(folder_path + "dog_grey_3.jpeg", gray_img_03)
print(gray_img_03[0, 0])