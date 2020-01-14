from desktopmagic.screengrab_win32 import getRectAsImage, getDisplayRects


def get_average_screen():
    image = getRectAsImage(get_current_bbox())
    return image


def get_current_bbox():
    return getDisplayRects()[0]
