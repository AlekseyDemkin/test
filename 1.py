import cv2
import numpy as np


def rotate_image(image, c):
    height, width = image.shape[:2]
    center = (width // 2, height // 2)
    rotation_matrix = cv2.getRotationMatrix2D(center, c, 1.0)
    cos = np.abs(rotation_matrix[0, 0])
    sin = np.abs(rotation_matrix[0, 1])
    new_width = int((height * sin) + (width * cos))
    new_height = int((height * cos) + (width * sin))
    rotation_matrix[0, 2] += (new_width / 2) - center[0]
    rotation_matrix[1, 2] += (new_height / 2) - center[1]
    rotate = cv2.warpAffine(image, rotation_matrix, (new_width, new_height))
    return rotate


image = cv2.imread('6.png')
c = int(input("Введите угол поворота:"))
rotate = rotate_image(image, c)
cv2.imshow('Original', image)
cv2.imshow('Rotated', rotate)
cv2.waitKey(0)
cv2.destroyAllWindows()
