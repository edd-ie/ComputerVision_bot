from models.WindowCapture import WindowCapture

# source = ImageCv()
# source.__int__('Images/farm.jpg', cv.IMREAD_UNCHANGED)
# needle = ImageCv()
# needle.__int__('Images/turnip.jpg', cv.IMREAD_UNCHANGED)
# source.search(needle.get_img(), "marker", threshold=0.73)

# Using pyautogui (fps 19-32)
# Using PIL (fps 19-35)
# Using win32 (fps 28-154), smaller screen the better

WindowCapture.active_windows()  # list of open windows
print("\n\nWin32")

shot = WindowCapture()
shot.__int__('File Explorer')
shot.findPos('Images/folder.jpg', "marker", 0.6, method='win')  # pygui, pil, win
