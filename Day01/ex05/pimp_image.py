import numpy as np
import matplotlib.pyplot as plt


def ft_invert(arr: np.array) -> np.array:
    """Inverts the color of the image received"""
    copy = arr.copy()
    copy = 255 - copy
    plt.imshow(copy)
    plt.show()
    return arr


def ft_red(arr: np.array) -> np.array:
    """Make the image red"""

    copy = arr.copy()
    copy[:, :, 1] = 0
    copy[:, :, 2] = 0
    plt.imshow(copy)
    plt.show()
    return arr


def ft_green(arr: np.array) -> np.array:
    """Make the image green"""

    copy = arr.copy()
    copy[:, :, 0] = 0
    copy[:, :, 2] = 0
    plt.imshow(copy)
    plt.show()
    return arr


def ft_blue(arr: np.array) -> np.array:
    """Make the image blue"""

    copy = arr.copy()
    copy[:, :, 0] = 0
    copy[:, :, 1] = 0
    plt.imshow(copy)
    plt.show()
    return arr


def ft_grey(arr: np.array) -> np.array:
    """Make the image grey"""
    copy = arr.copy()
    copy = np.dot(copy[..., :3], [0.2989, 0.5870, 0.1140])
    plt.imshow(copy, cmap='gray')
    plt.show()
    return arr
