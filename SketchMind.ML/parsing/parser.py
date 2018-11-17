# -*- coding: utf-8 -*-

import cv2
import numpy as np
import dir_manager as dm


def check_in(piece, total):
    x_p = piece[0]
    y_p = piece[1]
    w_p = piece[2]
    h_p = piece[3]
    for temp_piece in total:
        if((x_p > temp_piece[0] and x_p < (temp_piece[0]+temp_piece[2])) and (y_p > temp_piece[1] and y_p < (temp_piece[1]+temp_piece[3]))):
            return True
    return False


img = cv2.imread('img/test1.png')
result = img.copy()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(gray, 166, 255, cv2.THRESH_BINARY)
cv2.imwrite("thresh.jpg", thresh)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (20, 20))
eroded = cv2.erode(thresh, kernel)
cv2.imwrite("eroded.jpg", eroded)

binary, contours, hierarchy = cv2.findContours(
    eroded, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

color = (0, 255, 0)

temp_result = []
temp_pos = []
for c in contours:
    x, y, w, h = cv2.boundingRect(c)
    if x == 0:
        continue

    #cv2.rectangle(img, (x, y), (x + w, y + h), color, 1)
    temp = result[y:(y + h), x:(x + w)]
    if not(w < 50 and h < 50):
        if(not(check_in([x, y, w, h], temp_pos))):
            cv2.rectangle(img, (x, y), (x + w, y + h), color, 1)
            temp_pos.append([x, y, w, h])
            temp_result.append(temp)
        #cv2.imwrite("./result/" + str(x) + ".jpg", temp)

i = 0
for p in temp_result:
    cv2.imwrite("./result/" + str(temp_pos[i][0]) + ".jpg", p)
    i = i + 1

cv2.imwrite("result.jpg", img)
