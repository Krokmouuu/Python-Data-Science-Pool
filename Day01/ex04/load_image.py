import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import os


def ft_load(path: str) -> np.array:
    """Load an image from a path and display it"""
    try:
        if (path == ""):
            raise FileNotFoundError
        assert type(path) == str, "The path is not a string"
        assert Image.open(path), "The path is not a valid image"
        image = Image.open(path)
        if image.format not in ['JPEG', 'PNG', 'JPG']:
            raise AttributeError("The image is not a JPEG | JPG or PNG")
        print("The shape of image is: " + str(plt.imread(path).shape))
        arr = np.array(plt.imread(path))
        print(arr.flatten().astype(int))
    except AssertionError as e:
        print("AssertionError:", e)
        exit()
    except FileNotFoundError:
        print(f"Could not find file: {os.path.abspath(path)}")
        exit()
    except AttributeError as e:
        print("AttributeError:", e)
        exit()
    return arr
