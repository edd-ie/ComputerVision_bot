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
shot.__int__('OpenCV – Test.py')
shot.findPos('Images/hazard.jpg', "rectangle", 0.85, method='win')  # pygui, pil, win
#shapes = marker, rectangle
#people
    #window = team - Paint
    # mike, bird
    #thresh = 0.75 - 0.85

    #window = pain -Paint
    # steve, steve1, steve2
    #thresh = 0.50, 0.65, 0.75
#Icons
    #window = Images
    # mike, bird, bell, folder, folderIcon, hazard
    #thresh = 0.6 and higher

    #window = OpenCV – Test.py
    # harzard, stack, bell
    #thresh = 0.6, 0.7, 0.75, 0.8
#Albion Online
    #window = farm -Paint
    # cabbage, hay, hay2
    #thresh = 0.49, 0.56, 0.65, 0.75