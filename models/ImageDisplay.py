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

    def search(self, needle, shape="rectangle", threshold=0.49, method=cv.TM_CCOEFF_NORMED):
        needle_w = needle.shape[1]  # width of needle
        needle_h = needle.shape[0]  # Height of needle

        # Search for matches to the needle image from source image
        # Parameters(img, templ, method):
        #   img -  source image
        #   templ - image being searched
        #   method - the method of image matching
        #   [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED, cv.TM_CCORR, cv.TM_CCOEFF_NORMED
        #   cv.TM_CCOEFF, cv.TM_CCOEFF_NORMED]
        result = cv.matchTemplate(self.img, needle, method)

        locations = np.where(result >= threshold)

        # zip locations to multiple tuples
        locations = list(zip(*locations[::-1]))

        # Store drawn rectangles
        rectangles = []

        for location in locations:
            rect = [int(location[0]), int(location[1]), needle_w, needle_h]
            # Appending twice to ensure no single detection is removed during grouping
            rectangles.append(rect)
            rectangles.append(rect)

        # Removing multiple rectangle from one location
        # Parameters: rectangle list, minimum num of rectangles, Relative difference between sides to marge
        rectangles, weights = cv.groupRectangles(rectangles, 1, 0.5)
        center_points = []

        if len(rectangles):
            print("Found")

            for (x, y, w, h) in rectangles:
                top_left = (x, y)
                bottom_right = (x + w, y + h)

                center_x = x + int(w / 2)
                center_y = y + int(h / 2)
                center_points.append((center_x, center_y))

                if shape == "marker":
                    color = (0, 255, 0)  # BGR
                    cv.drawMarker(self.img, (center_x, center_y), color, markerType=cv.MARKER_TILTED_CROSS,
                                  markerSize=8)
                else:
                    # Drawing a rectangle Parameters:
                    #  source, top_left pos, bottom_right pos, colour, thickness, line_type
                    cv.rectangle(self.img, top_left, bottom_right, (0, 255, 0), 1, cv.LINE_4)

            print(center_points)
            self.show()

        # # Getting the percentage confidence of matching spots (Uncomment for best match)
        # min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
        # print("Best top left: ", str(max_loc))
        # print("Best match: ", str(max_val))
        #
        # # Setting minimum confidence to consider a match
        # threshold = 0.8
        # if max_val < threshold:
        #     print("Object not found")
        # else:
        #     print("Found")
        #
        #     top_left = max_loc
        #     needle_w = needle.shape[1]  # width of needle
        #     needle_h = needle.shape[0]  # Height of needle
        #
        #     # top_left + width & height of needle image
        #     bottom_right = (top_left[0] + needle_w, top_left[1] + needle_h)
        #
        #     # Drawing a rectangle on found objects, Parameters:
        #     #  original image, top_left pos, bottom_right pos, colour, thickness, line_type
        #     cv.rectangle(self.img, top_left, bottom_right, (0, 255, 0), 1, cv.LINE_4)
        #
        #     self.show()
