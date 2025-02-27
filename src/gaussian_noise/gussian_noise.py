import cv2
import numpy as np

# 读取图像
image = cv2.imread('image.jpg')

# 添加高斯噪声
def gaussian_noise(image, mean=0, var=0.01):
    row, col, ch = image.shape
    sigma = var**0.5
    gaussian = np.random.normal(mean, sigma, (row, col, ch))
    noisy_image = np.array(image, dtype=float)
    noisy_image += gaussian * 255
    noisy_image = np.clip(noisy_image, 0, 255)
    return noisy_image.astype(np.uint8)

# 增加高斯噪声到原图
noisy_image_gaussian = gaussian_noise(image, mean=0, var=0.01)

# 保存带有高斯噪声的原图
cv2.imwrite('noisy_image_gaussian.jpg', noisy_image_gaussian)

# 应用均值滤波
mean_filtered_gaussian = cv2.blur(noisy_image_gaussian, (5, 5))
cv2.imwrite('mean_filtered_image_gaussian.jpg', mean_filtered_gaussian)

# 应用高斯滤波
gaussian_filtered_gaussian = cv2.GaussianBlur(noisy_image_gaussian, (5, 5), 1.5)
cv2.imwrite('gaussian_filtered_image_gaussian.jpg', gaussian_filtered_gaussian)

# 应用中值滤波
median_filtered_gaussian = cv2.medianBlur(noisy_image_gaussian, 5)
cv2.imwrite('median_filtered_image_gaussian.jpg', median_filtered_gaussian)

# 应用双边滤波
bilateral_filtered_gaussian = cv2.bilateralFilter(noisy_image_gaussian, 15, 75, 75)
cv2.imwrite('bilateral_filtered_image_gaussian.jpg', bilateral_filtered_gaussian)
