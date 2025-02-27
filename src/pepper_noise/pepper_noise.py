import cv2
import numpy as np
import random

# 读取图像
image = cv2.imread('image.jpg')

# 添加椒盐噪声
def salt_and_pepper_noise(image, salt_prob, pepper_prob):
    noisy_image = image.copy()
    total_pixels = noisy_image.size
    salt_pixels = int(total_pixels * salt_prob)
    pepper_pixels = int(total_pixels * pepper_prob)

    # 添加盐噪声（白色像素）
    for _ in range(salt_pixels):
        x, y = random.randint(0, noisy_image.shape[0]-1), random.randint(0, noisy_image.shape[1]-1)
        noisy_image[x, y] = [255, 255, 255]

    # 添加椒噪声（黑色像素）
    for _ in range(pepper_pixels):
        x, y = random.randint(0, noisy_image.shape[0]-1), random.randint(0, noisy_image.shape[1]-1)
        noisy_image[x, y] = [0, 0, 0]

    return noisy_image

# 增加椒盐噪声到原图
noisy_image_sp = salt_and_pepper_noise(image, salt_prob=0.02, pepper_prob=0.02)

# 保存带有椒盐噪声的原图
cv2.imwrite('noisy_image_sp.jpg', noisy_image_sp)

# 应用均值滤波
mean_filtered_sp = cv2.blur(noisy_image_sp, (5, 5))
cv2.imwrite('mean_filtered_image_sp.jpg', mean_filtered_sp)

# 应用高斯滤波
gaussian_filtered_sp = cv2.GaussianBlur(noisy_image_sp, (5, 5), 1.5)
cv2.imwrite('gaussian_filtered_image_sp.jpg', gaussian_filtered_sp)

# 应用中值滤波
median_filtered_sp = cv2.medianBlur(noisy_image_sp, 5)
cv2.imwrite('median_filtered_image_sp.jpg', median_filtered_sp)

# 应用双边滤波
bilateral_filtered_sp = cv2.bilateralFilter(noisy_image_sp, 15, 75, 75)
cv2.imwrite('bilateral_filtered_image_sp.jpg', bilateral_filtered_sp)
