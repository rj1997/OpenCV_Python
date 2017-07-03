#Shape Detection
import numpy as np
import cv2

path = "C:\\Users\\Rishabh Jain\\Desktop\\yellow.png"
img = cv2.imread(path)

#cv2.imshow('WM',img)
gray = cv2.imread(path,0)

ret,thresh = cv2.threshold(gray.copy(),140,255,1)

#cv2.imshow('TH',thresh)

#print(cv2.findContours(thresh,1,2))
_ , contours , h = cv2.findContours(thresh.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
count=0

for cnt in contours:
    approx = cv2.approxPolyDP(cnt,0.05*cv2.arcLength(cnt,True),True)
    if len(approx)==5:
        print("pentagon")
        cv2.drawContours(img,[cnt],0,(0,0,0),-1)
    elif len(approx) == 6:
        print("Hex")
        cv2.drawContours(img, [cnt], 0, (0, 0, 0), -1)
    elif len(approx) == 7:
        print("Hept")
        cv2.drawContours(img, [cnt], 0, (0, 0, 0), -1)
    elif len(approx) == 8:
        print("triangle")
        cv2.drawContours(img, [cnt], 0, (0, 0, 0), -1)
    elif len(approx)==3:
        print("Octa")
        cv2.drawContours(img,[cnt],0,(0,0,0),-1)
    elif len(approx)==4:
        print("square")
        cv2.drawContours(img,[cnt],0,(0,0,0),-1)
    elif len(approx) == 9:
        print("halfcirlce")
        cv2.drawContours(img,[cnt],0,(0,0,0),-1)
    elif len(approx) > 15:
        print("circle")
        cv2.drawContours(img,[cnt],0,(0,0,0),-1)

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()