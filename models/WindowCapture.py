from time import time
from PIL import ImageGrab
import cv2 as cv
import numpy as np
import pyautogui
import win32con
import win32gui
import win32ui
from models.Search import ImageSearch


class WindowCapture:
    hwnd = None
    w = 1920  # set this
    h = 1080  # set this
    crop_x = 0
    crop_y = 0
    screen_pos_x = 0
    screen_pos_y = 0

    def __int__(self, window_name=None):
        if window_name is None:
            self.hwnd = win32gui.GetDesktopWindow()
        else:
            self.hwnd = win32gui.FindWindow(None, window_name)
            if not self.hwnd:
                raise Exception('Window not found: {}'.format(window_name))

        window_rect = win32gui.GetWindowRect(self.hwnd)  # get top left pos and bottom right pos
        self.w = window_rect[2] - window_rect[0]
        self.h = window_rect[3] - window_rect[1]

        # Removing border (Optional)
        borders = 8
        title_bar = 20
        self.crop_x = borders
        self.crop_y = title_bar

        self.screen_pos_x = self.w - borders
        self.screen_pos_y = self.h - title_bar
        self.w = self.w - (borders * 2)
        self.h = self.h - (title_bar + borders)

    # Using Win32
    def window_capture(self):
        # bmp_filename_name = "Images/out.bmp"  # set this if you want to save screenshot

        # Getting Image data
        w_dc = win32gui.GetWindowDC(self.hwnd)
        dc_obj = win32ui.CreateDCFromHandle(w_dc)
        c_dc = dc_obj.CreateCompatibleDC()
        data_bitmap = win32ui.CreateBitmap()
        data_bitmap.CreateCompatibleBitmap(dc_obj, self.w, self.h)
        c_dc.SelectObject(data_bitmap)
        c_dc.BitBlt((0, 0), (self.w, self.h), dc_obj, (self.crop_x, self.crop_y), win32con.SRCCOPY)

        # Saving image
        # data_bitmap.SaveBitmapFile(c_dc, bmp_filename_name)

        # Converting to np.array
        data_set = data_bitmap.GetBitmapBits(True)
        img = np.frombuffer(data_set, dtype='uint8')
        img.shape = (self.h, self.w, 4)

        # Free Resources
        dc_obj.DeleteDC()
        c_dc.DeleteDC()
        win32gui.ReleaseDC(self.hwnd, w_dc)
        win32gui.DeleteObject(data_bitmap.GetHandle())

        # drop alpha channel/transparency
        img = img[..., :3]
        img = np.ascontiguousarray(img)

        return img

    def findPos(self,  img_path, shape="rectangle", threshold=0.49, method="win",):
        search = ImageSearch(img_path, shape, threshold)

        loop_t = time()
        while True:
            # take a screenshot
            if method == "pygui":
                screen = self.colour_convert(pyautogui.screenshot())
            elif method == "pil":
                screen = self.colour_convert(ImageGrab.grab())
            else:
                screen = self.window_capture()

            # display
            # cv.imshow("Window capture", screen)
            center_points = search.search(screen)

            print('FPS: {}'.format(1 / (time() - loop_t)))
            loop_t = time()

            if cv.waitKey(1) == ord('q'):
                cv.destroyAllWindows()
                break

    def getScreenPos(self, pos):
        return pos[0] + self.screen_pos_x, pos[1] + self.screen_pos_y

    @staticmethod
    def colour_convert(data):
        # convert to a matrix
        screen = np.array(data)
        # invert colours
        screen = cv.cvtColor(screen, cv.COLOR_RGB2BGR)
        return screen

    @staticmethod
    # Show active windows
    def active_windows():
        def winEnumHandler(hwnd, ctx):
            if win32gui.IsWindowVisible(hwnd):
                print("Address: ", hex(hwnd), ",   Name: ", win32gui.GetWindowText(hwnd))

        win32gui.EnumWindows(winEnumHandler, None)
