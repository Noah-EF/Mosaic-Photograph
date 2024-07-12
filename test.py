from transformers import *
import numpy as np
import cv2

flower = cv2.imread("images/flower.png")
flower_rect = cv2.imread("images/flower_rect.jpg")

""" Testing for average_area """

# checks that average area matches for a single pixel
a1 = average_area(flower[:1, :1])
assert False not in [a1[p] == flower[0, 0][p] for p in range(len(a1))]

# tests that the average area function calculation of the 2x2 top left corner matches a manual calculation
a2 = average_area(flower[:2, :2])
assert np.array_equal(a2, (flower[0, 0] / 4) + (flower[1, 0] / 4) + (flower[0, 1] / 4) + (flower[1, 1] / 4))

# checks datatype of average_area, float is fine here since its used as a scalar and isn't displayed directly
assert a1.dtype == np.float64


""" Testing for split """

# tests result size for square image
split1 = split(flower, (20, 20))
assert split1.shape == (20, 20, 3)

# tests result size for square image, non-factor size, not supposed to be supported, but just in case
# this is expected because 400 / 15 ~ 26.67, cast floors to 26, better than round
# round could potentially produce larger result which can cause issues trying to get data that doesn't exist
split2 = split(flower, (15, 15))
assert split2.shape == (26, 26, 3)

# tests result size for rect image
split3 = split(flower_rect, (30, 20))
assert split3.shape == (20, 20, 3)

# tests split for rect image, non proportional pixels
split4 = split(flower_rect, (20, 20))
assert split4.shape == (30, 20, 3)

""" Testing for shade """

# tests shade size for square image (output size should match input size
shade1 = shade(flower, (0, 0, 0))
assert shade1.shape == (400, 400, 3)

# tests shade size for rect image
shade2 = shade(flower_rect, (0, 0, 0))
assert shade2.shape == (600, 400, 3)

# same as above two but with different shading pixels, shouldn't matter
shade3 = shade(flower, (230, 100, 12))
assert shade3.shape == (400, 400, 3)

shade4 = shade(flower_rect, (124, 123, 90))
assert shade4.shape == (600, 400, 3)

""" Testing for create_mosaic """

# testing result size for no scale given, valid size given
mosaic1 = create_mosaic(flower, (20, 20))
assert mosaic1.dtype == np.uint8
assert mosaic1.shape == (400, 400, 3)

# testing result size rect, no scale given
mosaic2 = create_mosaic(flower_rect, (20, 20))
assert mosaic2.dtype == np.uint8
assert mosaic2.shape == (600, 400, 3)

# testing result size for square, with scale given
mosaic3 = create_mosaic(flower, (20, 20), 2)
assert mosaic3.dtype == np.uint8
assert mosaic3.shape == (800, 800, 3)

# testing result size for rect, with scale given
mosaic4 = create_mosaic(flower_rect, (20, 20), 2)
assert mosaic4.dtype == np.uint8
assert mosaic4.shape == (1200, 800, 3)

