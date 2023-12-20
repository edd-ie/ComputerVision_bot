import cv2 as cv
from ImageDisplay import ImageCv

source = ImageCv()
source.__int__('Images/farm.jpg', cv.IMREAD_UNCHANGED)

needle = ImageCv()
needle.__int__('Images/turnip.jpg', cv.IMREAD_UNCHANGED)

source.search(needle.get_img(), "marker", threshold=0.73)
