import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

color = [9, 9, 202]  # BGR
bg_color = [255, 255, 255]  # BGR
pen_size = 10
eraser_is_active = False
bg_color_is_active = False
drawing = False
ix = 0
iy = 0


def change_pen_size(x):
    global pen_size, setting
    pen_size = x
    setting[6:58, 640:750] = (255, 255, 255)
    cv.putText(setting, str(pen_size), (650, 43), cv.FONT_HERSHEY_COMPLEX, 1, 0, 2)


def show_color():
    if bg_color_is_active:
        board[...] = bg_color
    else:
        setting[10:54, 910:1019, :] = color


def change_b(val):
    global color, bg_color
    if bg_color_is_active:
        bg_color[0] = val
    else:
        color[0] = val
    show_color()


def change_g(val):
    global color, bg_color
    if bg_color_is_active:
        bg_color[1] = val
    else:
        color[1] = val
    show_color()


def change_r(val):
    global color, bg_color
    if bg_color_is_active:
        bg_color[2] = val
    else:
        color[2] = val
    show_color()


def draw(event, x, y, flags, param):
    if y >= 64:
        y -= 64
        global ix, iy, drawing, color, eraser_is_active, pen_size
        if event == cv.EVENT_LBUTTONDOWN:
            drawing = True
            ix = x
            iy = y
        if event == cv.EVENT_MOUSEMOVE:
            if drawing == True:
                if eraser_is_active:
                    cv.line(board, (ix, iy), (x, y), bg_color, pen_size)
                else:
                    cv.line(board, (ix, iy), (x, y), color, pen_size)
                ix = x
                iy = y
        if event == cv.EVENT_LBUTTONUP:
            if eraser_is_active:
                cv.circle(board, (x, y), pen_size // 2, bg_color, -1)
            else:
                cv.circle(board, (x, y), pen_size // 2, color, -1)
            drawing = False

    else:
        if event == cv.EVENT_LBUTTONUP:
            if 20 < x < 150 and 10 < y < 52:
                eraser_event()
            elif 170 < x < 335 and 10 < y < 52:
                bg_color_event()


def eraser_event():
    global eraser_is_active
    setting[9:55, 10:160, :] = (255, 255, 255)
    if eraser_is_active:
        cv.rectangle(setting, (20, 10), (150, 52), (230, 230, 230), -1)
        cv.rectangle(setting, (20, 10), (150, 52), 0, 2)
        cv.putText(setting, "Eraser", (30, 41), cv.FONT_HERSHEY_COMPLEX, 1, 0, 2)
    else:
        cv.rectangle(setting, (20, 10), (150, 52), (90, 90, 90), -1)
        cv.rectangle(setting, (20, 10), (150, 52), 0, 2)
        cv.putText(
            setting, "Eraser", (30, 41), cv.FONT_HERSHEY_COMPLEX, 1, (250, 250, 250), 2
        )
    eraser_is_active = not eraser_is_active


def bg_color_event():
    global bg_color_is_active, color, bg_color
    setting[159:205, 10:160, :] = (255, 255, 255)
    if bg_color_is_active:
        cv.rectangle(setting, (170, 10), (335, 52), (230, 230, 230), -1)
        cv.rectangle(setting, (170, 10), (335, 52), 0, 2)
        cv.putText(setting, "Bg color", (180, 41), cv.FONT_HERSHEY_COMPLEX, 1, 0, 2)
        bg_color_is_active = False
        cv.setTrackbarPos("Red", "paint", color[2])
        cv.setTrackbarPos("Green", "paint", color[1])
        cv.setTrackbarPos("Blue", "paint", color[0])
    else:
        cv.rectangle(setting, (170, 10), (335, 52), (90, 90, 90), -1)
        cv.rectangle(setting, (170, 10), (335, 52), 0, 2)
        cv.putText(
            setting,
            "Bg color",
            (180, 41),
            cv.FONT_HERSHEY_COMPLEX,
            1,
            (250, 250, 250),
            2,
        )
        bg_color_is_active = True
        cv.setTrackbarPos("Red", "paint", bg_color[2])
        cv.setTrackbarPos("Green", "paint", bg_color[1])
        cv.setTrackbarPos("Blue", "paint", bg_color[0])


img = np.zeros((576, 1024, 3), np.uint8)
setting = np.zeros((64, 1024, 3), np.uint8)
setting[...] = (255, 255, 255)
setting[59:64, :, :] = (0, 0, 0)
setting[0:5, :, :] = (0, 0, 0)
cv.putText(setting, "color:", (800, 40), cv.FONT_HERSHEY_COMPLEX, 1, 0, 2)
cv.putText(setting, "pen size:", (480, 40), cv.FONT_HERSHEY_COMPLEX, 1, 0, 2)
cv.putText(setting, str(pen_size), (650, 43), cv.FONT_HERSHEY_COMPLEX, 1, 0, 2)
cv.rectangle(setting, (20, 10), (150, 52), (230, 230, 230), -1)
cv.rectangle(setting, (20, 10), (150, 52), 0, 2)
cv.putText(setting, "Eraser", (30, 41), cv.FONT_HERSHEY_COMPLEX, 1, 0, 2)
cv.rectangle(setting, (170, 10), (335, 52), (230, 230, 230), -1)
cv.rectangle(setting, (170, 10), (335, 52), 0, 2)
cv.putText(setting, "Bg color", (180, 41), cv.FONT_HERSHEY_COMPLEX, 1, 0, 2)
board = np.zeros((512, 1024, 3), np.uint8)
board[...] = bg_color


cv.namedWindow("paint")
cv.createTrackbar("Red", "paint", color[2], 255, change_r)
cv.createTrackbar("Green", "paint", color[1], 255, change_g)
cv.createTrackbar("Blue", "paint", color[0], 255, change_b)
cv.createTrackbar("Pen Size", "paint", pen_size, 200, change_pen_size)
cv.setMouseCallback("paint", draw)

while True:
    img[0:64, :, :] = setting
    img[64:576, :, :] = board
    cv.imshow("paint", img)
    if cv.waitKey(5) & 0xFF == 27:
        break

cv.destroyAllWindows()