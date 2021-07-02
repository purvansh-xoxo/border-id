import cv2 as cv
import numpy as np

img = cv.imread('ques.png',0)
_, ans = cv.threshold(img, 127, 255, cv.THRESH_BINARY)

cv.imshow("QUES", img)
cv.imshow("ANS", ans)

cv.waitKey(0)
cv.destroyAllWindows()