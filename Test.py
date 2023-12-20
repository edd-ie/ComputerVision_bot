import cv2 as cv
from ImageDisplay import ImageCv

source = ImageCv()
source.__int__('Images/sample.jpg', cv.IMREAD_UNCHANGED)

needle = ImageCv()
needle.__int__('Images/key.jpg', cv.IMREAD_UNCHANGED)

source.search(needle.get_img())
