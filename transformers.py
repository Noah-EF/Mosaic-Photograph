import numpy as np
import cv2


# return average pixel for matrix a
def average_area(a):
    pix = np.sum(np.sum(a, 0), 0)
    num = a.shape[0] * a.shape[1]
    return np.round(pix / num)


# takes in image and desired size of subsets
# returns the image divided into smaller images of input size
def split(image, size):
    a = []
    for y in range(int(image.shape[0] / size[0])):
        row = []
        for x in range(int(image.shape[1] / size[1])):
            row.append(average_area(image[y * size[0]: (y + 1) * size[0], x * size[1]: (x + 1) * size[1]]))
        a.append(row)
    return np.array(a).astype(np.uint8)


# returns the image shaded to on average match the color of the input pixel
def shade(image, pixel):
    a = average_area(image)
    scale = pixel / a
    out = np.multiply(np.int32(image), scale)
    # allows conversion back without overflow
    out = np.maximum(np.minimum(out, np.array([255])), [0])
    return np.uint8(out)

# image parameter is input
# size is a tuple (width, height) describing the desired size of sections of the input image taken to be replaced with shrunk images
# pixel_scale determines the resolution of the pixel images, one would result in an output image the same resolution as input
# higher values would produce a larger output
def create_mosaic(image, size, pixel_scale=1):
    splits = split(image, size)
    shrunk = cv2.resize(image, (size[1] * pixel_scale, size[0] * pixel_scale))
    mosaic = np.concatenate([np.hstack([shade(shrunk, splits[y][x]) for x in range(len(splits[0]))])
                             for y in range(len(splits))])
    return mosaic


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Create a mosaic from an image.")
    parser.add_argument("image_path", help="Path to the input image.")
    parser.add_argument("output_path", help="Path to save the output mosaic image.")
    parser.add_argument("size_H", help="Height of sections to divide input into. Preferably factor of input height")
    parser.add_argument("size_W", help="Width of sections to divide input into. Preferably factor of input width")
    parser.add_argument("-pixel_scale", "--scale", help="Scale value for resolution of output. Optional", required=False, default=1)
    args = parser.parse_args()
    image = cv2.imread(args.image_path)
    mosaic = create_mosaic(image, (int(args.size_H), int(args.size_W)), int(args.scale))
    cv2.imwrite(args.output_path, mosaic)

