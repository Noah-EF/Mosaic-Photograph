import numpy as np
import cv2
from transformers import split, shade


def create_mosaic(image_path, output_path):
    # Load the image
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError("Image not found or unable to load.")

    # Determine the size of each tile
    h, w, _ = image.shape
    tile_size = int(np.sqrt(h * w / 1000))  # Adjust 1000 based on desired tile count

    # Split the image into smaller sections to calculate average colors
    small_images = split(image, tile_size)

    # Create a blank canvas for the mosaic
    mosaic_image = np.zeros_like(image)

    # Create the smaller version of the input image for the mosaic tiles
    shrunk = cv2.resize(image, (tile_size, tile_size))

    # Fill the mosaic image with shaded smaller versions of the input image
    for y in range(0, h, tile_size):
        for x in range(0, w, tile_size):
            # Calculate the position in the small_images array
            sub_img_y = y // tile_size
            sub_img_x = x // tile_size

            if sub_img_y < small_images.shape[0] and sub_img_x < small_images.shape[1]:
                avg_color = small_images[sub_img_y, sub_img_x]
                
                # Shade the shrunk image to match the average color
                shaded_img = shade(shrunk, avg_color)
                y_end = min(y + tile_size, h)
                x_end = min(x + tile_size, w)
                slice_y = y_end - y
                slice_x = x_end - x

                # Place the shaded image in the mosaic
                mosaic_image[y:y_end, x:x_end] = shaded_img[:slice_y, :slice_x]
    cv2.imwrite(output_path, mosaic_image)
    print(f"Mosaic image saved to {output_path}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Create a mosaic from an image.")
    parser.add_argument("image_path", help="Path to the input image.")
    parser.add_argument("output_path", help="Path to save the output mosaic image.")
    args = parser.parse_args()

    create_mosaic(args.image_path, args.output_path)