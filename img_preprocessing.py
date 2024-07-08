import cv2
import numpy as np
import matplotlib.pyplot as plt

def show_image(image, title="Image"):
    plt.figure(figsize=(6,6))
    plt.imshow(image, cmap='gray')  # Gri tonlamalı resimler için 'gray' kullanılır
    plt.title(title)
    plt.axis('off')  # Eksenleri gizle
    plt.show()

def preprocess_image(image_path):
    image = cv2.imread(image_path)
    show_image(image, "Original Image")
    
    # Resmi yeniden boyutlandırma
    resized_image = cv2.resize(image, (256, 256))
    show_image(resized_image, "Resized Image")

    # Gri tonlamaya çevirme
    gray_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)
    show_image(gray_image, "Grayscale Image")

    # Gürültü azaltma (Gaussian Blur uygulama)
    smooth_image = cv2.GaussianBlur(gray_image, (5, 5), 0)
    show_image(smooth_image, "Smoothed Image")

    # Normalizasyon
    normalized_image = cv2.normalize(smooth_image, None, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)
    show_image(normalized_image, "Normalized Image")

    # Binarizasyon
    _, binary_image = cv2.threshold(normalized_image, 0.5, 1, cv2.THRESH_BINARY)
    show_image(binary_image, "Binary Image")

    # Kontrast arttırma
    contrast_enhanced_image = cv2.equalizeHist(gray_image.astype(np.uint8))
    show_image(contrast_enhanced_image, "Contrast Enhanced Image")

    return contrast_enhanced_image


image_path = '/kaggle/input/kermany2018/OCT2017 /test/CNV/CNV-1016042-1.jpeg'
processed_image = preprocess_image(image_path)
