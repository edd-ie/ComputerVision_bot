import cv2 as cv
import numpy as np
import sys


class ImageSearch:
    # Instance variables
    needle = None
    method = None
    threshold = 0
    needle_w = 0
    needle_h = 0
    shape = ''

    def __init__(self, needle_path, shape="rectangle", threshold=0.49, method=cv.TM_CCOEFF_NORMED):
        # needle - image being searched
        self.needle = cv.imread(needle_path, cv.IMREAD_UNCHANGED)
        self.needle_w = self.needle.shape[1]  # width of needle
        self.needle_h = self.needle.shape[0]  # Height of needle

        self.shape = shape
        self.threshold = threshold

        #   method - the method of image matching
        #   [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED, cv.TM_CCORR, cv.TM_CCOEFF_NORMED
        #   cv.TM_CCOEFF, cv.TM_CCOEFF_NORMED]
        self.method = method

    def search(self, image):
        # image - source image
        result = cv.matchTemplate(image, self.needle, self.method)

        locations = np.where(result >= self.threshold)

        # zip locations to multiple tuples
        locations = list(zip(*locations[::-1]))

        # Store drawn rectangles
        rectangles = []

        for location in locations:
            rect = [int(location[0]), int(location[1]), self.needle_w, self.needle_h]
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

                if self.shape == "marker":
                    color = (0, 0, 255)  # BGR
                    cv.drawMarker(image, (center_x, center_y), color, markerType=cv.MARKER_TILTED_CROSS,
                                  markerSize=9)
                else:
                    # Drawing a rectangle Parameters:
                    #  source, top_left pos, bottom_right pos, colour, thickness, line_type
                    cv.rectangle(image, top_left, bottom_right, (0, 255, 0), 1, cv.LINE_4)

        print(center_points)
        if image is None:
            sys.exit("Couldn't read image!")
        else:
            cv.imshow("Matches", image)

        return center_points
