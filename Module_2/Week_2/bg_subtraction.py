import numpy as np
import cv2


def compute_difference(bg_img, input_img):
    difference_single_channel = cv2.absdiff(bg_img, input_img)
    return difference_single_channel


def compute_binary_mask(difference_single_channel):
    difference_binary = np.where(difference_single_channel == 0, 0, 255)
    difference_binary = difference_binary.astype(np.uint8)
    return difference_binary


def replace_background(bg1_image, bg2_image, ob_image):
    difference_single_channel = compute_difference(bg1_image, ob_image)
    binary_mask = compute_binary_mask(difference_single_channel)
    output = np.where(binary_mask == 0, bg2_image, ob_image)
    return output


if __name__ == "__main__":
    folder_path = './AIO-Exercise/Module_2/Week_2/img_data/'
    bg1_image = cv2.imread(folder_path+'GreenBackground.png', 1)
    bg1_image = cv2.resize(bg1_image, (678, 381))

    ob_image = cv2.imread(folder_path+'Object.png', 1)
    ob_image = cv2.resize(ob_image, (678, 381))

    bg2_image = cv2.imread(folder_path+'NewBackground.jpg', 1)
    bg2_image = cv2.resize(bg2_image, (678, 381))

    difference_single_channel = compute_difference(bg1_image, ob_image)
    difference_binary = compute_binary_mask(difference_single_channel)
    new_img = replace_background(bg1_image, bg2_image, ob_image)
    
    cv2.imwrite(folder_path+'ObjectWithNewBackground.png', new_img)