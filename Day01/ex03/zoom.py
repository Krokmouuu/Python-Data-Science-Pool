from load_image import ft_load
import matplotlib.pyplot as plt
import numpy as np


def main():
    """Main function"""
    path = "animal.jpeg"
    image = ft_load(path)
    image = image[95:495, 455:855]
    img_gray = np.dot(image[..., :3], [0.2989, 0.5870, 0.1140])
    print("New shape after slicing:", img_gray.shape)
    print(img_gray.flatten().astype(int))  # See a readable array
    # print(img_gray.shape)  # See a disgusting array
    plt.imshow(img_gray, cmap='gray')
    plt.show()
    return 0


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print("AssertionError:", e)
        exit()
