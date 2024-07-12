import numpy as np
import cv2
from transformers import *



"""# creates a few images for use testing, flower is mostly used currently
flower = cv2.imread("images/flower.png")
flowerG = cv2.imread("images/flower.png", cv2.IMREAD_GRAYSCALE)
image_test = cv2.imread("images/blueSky.png")
image_testG = cv2.imread("images/blueSky.png", cv2.IMREAD_GRAYSCALE)

# gets split of flower image into 20 by 20 blocks
flower_splits = split(flower, 20)
cv2.imshow("Flower", flower)

# shrinks the main image down for use as a mosaic tile without making the mosaic file too massive
shrunk = cv2.resize(flower, (20, 20))

# Shades the shrunken image according the flower_splits array
mosaic = np.concatenate([np.hstack([shade(shrunk, flower_splits[y][x]) for x in range(len(flower_splits[0]))]) for y in range(len(flower_splits))])

# this will hopefully create a large mosaic with a greater resolution of the main image than the first set
flower_splits2 = split(flower, 10)
# basically same as shrunk but better resolution, will result in larger final output though
shrunk2 = cv2.resize(flower, (40, 40))

# basically same code as mosaic just using the differently sized splits and shrinks
mosaicHuge2 = np.concatenate([np.hstack([shade(shrunk2, flower_splits2[y][x]) for x in range(len(flower_splits2[0]))]) for y in range(len(flower_splits2))])
cv2.imwrite("output_images/big_mosaic2.PNG", mosaicHuge2)
cv2.imshow("Mosaic", mosaicHuge2)
cv2.waitKey(0)"""

"""flower_rect = cv2.imread("images/flower_rect.jpg")
mosaic = create_mosaic(flower_rect, (20, 30))
cv2.imshow("Mosaic", mosaic)
cv2.waitKey(0)"""

