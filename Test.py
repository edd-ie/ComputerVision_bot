import cv2 as cv
from ImageDisplay import ImageCv
from WindowCapture import WindowCapture, active_windows

source = ImageCv()
source.__int__('Images/farm.jpg', cv.IMREAD_UNCHANGED)

needle = ImageCv()
needle.__int__('Images/turnip.jpg', cv.IMREAD_UNCHANGED)

source.search(needle.get_img(), "marker", threshold=0.73)

# Using pyautogui (fps 19-32)
# WindowCapture.capture("pygui")

# Using PIL (fps 19-35)
# qprint("\nPIL")
# WindowCapture.capture("pil")


# Using win32 (fps 28-154), smaller screen the better
print("\n\nWin32")
active_windows()  # list of open windows

shot = WindowCapture()
shot.__int__('OpenCV')
shot.capture(method='win')  # pygui, pil, win
