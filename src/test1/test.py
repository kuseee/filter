import cv2
import numpy as np

# 读取图像
image = cv2.imread('image.jpg')

# 应用均值滤波
mean_filtered = cv2.blur(image, (5, 5))
cv2.imwrite('mean_filtered_image.jpg', mean_filtered)

# 应用高斯滤波
gaussian_filtered = cv2.GaussianBlur(image, (5, 5), 1.5)
cv2.imwrite('gaussian_filtered_image.jpg', gaussian_filtered)

# 应用中值滤波
median_filtered = cv2.medianBlur(image, 5)
cv2.imwrite('median_filtered_image.jpg', median_filtered)

# 应用双边滤波
bilateral_filtered = cv2.bilateralFilter(image, 15, 75, 75)
cv2.imwrite('bilateral_filtered_image.jpg', bilateral_filtered)
