import cv2
import numpy as np


def generate_bayer_masks(height, width, pattern):
    mask_R = np.zeros((height, width), dtype=np.float32)
    mask_G = np.zeros((height, width), dtype=np.float32)
    mask_B = np.zeros((height, width), dtype=np.float32)

    if pattern == 'RGGB':
        mask_R[0::2, 0::2] = 1
        mask_G[0::2, 1::2] = 1
        mask_G[1::2, 0::2] = 1
        mask_B[1::2, 1::2] = 1
    elif pattern == 'BGGR':
        mask_B[0::2, 0::2] = 1
        mask_G[0::2, 1::2] = 1
        mask_G[1::2, 0::2] = 1
        mask_R[1::2, 1::2] = 1
    elif pattern == 'GRBG':
        mask_G[0::2, 0::2] = 1
        mask_R[0::2, 1::2] = 1
        mask_B[1::2, 0::2] = 1
        mask_G[1::2, 1::2] = 1
    elif pattern == 'GBRG':
        mask_G[0::2, 0::2] = 1
        mask_B[0::2, 1::2] = 1
        mask_R[1::2, 0::2] = 1
        mask_G[1::2, 1::2] = 1

    return mask_R, mask_G, mask_B


def demosaic_image(raw, pattern):
    height, width = raw.shape
    mask_R, mask_G, mask_B = generate_bayer_masks(height, width, pattern)

    rgb = np.zeros((height, width, 3), dtype=np.float32)

    R = raw * mask_R
    G = raw * mask_G
    B = raw * mask_B

    kernel_RB = np.array([[0.25, 0.5, 0.25],
                          [0.5, 1.0, 0.5],
                          [0.25, 0.5, 0.25]])
    kernel_G = np.array([[0.0, 0.25, 0.0],
                         [0.25, 1.0, 0.25],
                         [0.0, 0.25, 0.0]])

    G = cv2.filter2D(G, -1, kernel_G)
    R = cv2.filter2D(R, -1, kernel_RB)
    B = cv2.filter2D(B, -1, kernel_RB)

    rgb[:, :, 0] = B
    rgb[:, :, 1] = G
    rgb[:, :, 2] = R

    rgb = rgb.clip(0, 65535).astype(np.uint16)
    return rgb


def calculate_vng_gradients(image, i, j):
    gradients = {
        'N': abs(image[i - 1, j] - image[i + 1, j]),
        'S': abs(image[i + 1, j] - image[i - 1, j]),
        'W': abs(image[i, j - 1] - image[i, j + 1]),
        'E': abs(image[i, j + 1] - image[i, j - 1]),
        'NE': abs(image[i - 1, j + 1] - image[i + 1, j - 1]),
        'NW': abs(image[i - 1, j - 1] - image[i + 1, j + 1]),
        'SE': abs(image[i + 1, j + 1] - image[i - 1, j - 1]),
        'SW': abs(image[i + 1, j - 1] - image[i - 1, j + 1]),
    }
    return gradients


def vng_demosaic(raw, pattern):
    height, width = raw.shape
    rgb = np.zeros((height, width, 3), dtype=np.float32)
    raw = raw.astype(np.float32)

    mask_R, mask_G, mask_B = generate_bayer_masks(height, width, pattern)

    R = raw * mask_R
    G = raw * mask_G
    B = raw * mask_B

    for i in range(1, height - 1):
        for j in range(1, width - 1):
            if mask_G[i, j] == 0:
                G[i, j] = (raw[i - 1, j] + raw[i + 1, j] + raw[i, j - 1] + raw[i, j + 1]) / 4

    for i in range(2, height - 2):
        for j in range(2, width - 2):
            if mask_R[i, j] == 1:
                gradients = calculate_vng_gradients(G, i, j)
                min_gradient = min(gradients, key=gradients.get)
                if min_gradient in ['N', 'S']:
                    G[i, j] = (G[i - 1, j] + G[i + 1, j]) / 2
                elif min_gradient in ['W', 'E']:
                    G[i, j] = (G[i, j - 1] + G[i, j + 1]) / 2
                elif min_gradient in ['NE', 'SW']:
                    G[i, j] = (G[i - 1, j + 1] + G[i + 1, j - 1]) / 2
                elif min_gradient in ['NW', 'SE']:
                    G[i, j] = (G[i - 1, j - 1] + G[i + 1, j + 1]) / 2
                B[i, j] = np.mean([B[i - 1, j - 1], B[i - 1, j + 1], B[i + 1, j - 1], B[i + 1, j + 1]])
            elif mask_B[i, j] == 1:
                gradients = calculate_vng_gradients(G, i, j)
                min_gradient = min(gradients, key=gradients.get)
                if min_gradient in ['N', 'S']:
                    G[i, j] = (G[i - 1, j] + G[i + 1, j]) / 2
                elif min_gradient in ['W', 'E']:
                    G[i, j] = (G[i, j - 1] + G[i, j + 1]) / 2
                elif min_gradient in ['NE', 'SW']:
                    G[i, j] = (G[i - 1, j + 1] + G[i + 1, j - 1]) / 2
                elif min_gradient in ['NW', 'SE']:
                    G[i, j] = (G[i - 1, j - 1] + G[i + 1, j + 1]) / 2
                R[i, j] = np.mean([R[i - 1, j - 1], R[i - 1, j + 1], R[i + 1, j - 1], R[i + 1, j + 1]])

    rgb[:, :, 0] = R
    rgb[:, :, 1] = G
    rgb[:, :, 2] = B

    return rgb.clip(0, 65535).astype(np.uint16)
