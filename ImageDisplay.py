import sys
import numpy as np
import cv2 as cv


def show(img):
    if img is None:
        sys.exit("Couldn't read image!")
    else:
        cv.imshow("Display window", img)
        key = cv.waitKey(0)

        if key == ord("s"):
            cv.imwrite("Images/image_view", img)


class ImageCv:
    img = None

    def __int__(self, image, img_format=cv.IMREAD_COLOR):
        self.img = cv.imread(image, img_format)

    def get_img(self):
        return self.img

    def show(self, image=None):
        if image is None:
            show(self.img)
        else:
            show(image)

    def convert(self, change_to):
        edit = cv.cvtColor(self.img, change_to)
        return edit

    def search(self, needle, method=cv.TM_CCOEFF_NORMED):
        # Search for matches to the needle image from source image
        result = cv.matchTemplate(self.img, needle, method)

        # Getting the percentage confidence of matching spots
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
        print("Best top left: ", str(max_loc))
        print("Best match: ", str(max_val))

        # Setting minimum confidence to consider a match
        threshold = 0.8
        if max_val < threshold:
            print("Object not found")
        else:
            print("Found")

            top_left = max_loc
            needle_w = needle.shape[1]  # width of needle
            needle_h = needle.shape[0]  # Height of needle

            # top_left + width & height of needle image
            bottom_right = (top_left[0] + needle_w, top_left[1] + needle_h)

            # Drawing a rectangle on found objects, Parameters:
            #  original image, top_left pos, bottom_right pos, colour, thickness, line_type
            cv.rectangle(self.img, top_left, bottom_right, (0, 255, 0), 1, cv.LINE_4)

            self.show()

        # show(result)
