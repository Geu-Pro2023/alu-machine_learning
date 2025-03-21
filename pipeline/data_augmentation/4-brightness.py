#!/usr/bin/env python3

import tensorflow as tf
import tensorflow_datasets as tfds
import matplotlib.pyplot as plt

def change_brightness(image, max_delta):
    """
    Randomly changes the brightness of an image.
    - image: tf.Tensor, 3D tensor representing the image to adjust.
    - max_delta: float, the maximum amount the image brightness should change.
    - A tf.Tensor of the altered image.
    """
    adjusted_image = tf.image.random_brightness(image, max_delta=max_delta)
    return adjusted_image

if __name__ == "__main__":
    doggies = tfds.load("stanford_dogs", split="train", as_supervised=True)
    for image, _ in doggies.shuffle(10).take(1):
        plt.imshow(change_brightness(image, 0.3))
        plt.show()
