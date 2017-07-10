import cv2
import numpy as np

path = "C:\\Users\\Rishabh Jain\\Desktop\\traffic_light.jpg" #Path to the image
img = cv2.imread(path,cv2.IMREAD_COLOR)

lower_red=np.array([0,0,100])
higher_red = np.array([50,40,255])

lower_yellow=np.array([0,180,180])
higher_yellow = np.array([224,255,255])

lower_green=np.array([0,100,0])
higher_green = np.array([90,255,100])

mask_red = cv2.inRange(img,lower_red,higher_red)
mask_yellow = cv2.inRange(img,lower_yellow,higher_yellow)
mask_green = cv2.inRange(img,lower_green,higher_green)

res = cv2.bitwise_or(img,img,mask=mask_red)
res = cv2.bitwise_or(img,img,mask=mask_yellow)
res = cv2.bitwise_or(img,img,mask=mask_green)

cnts_red = cv2.findContours(mask_red.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[-2]
cnts_yellow = cv2.findContours(mask_yellow.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[-2]
cnts_green= cv2.findContours(mask_green.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[-2]

cv2.drawContours(img, cnts_red, -1, (0,0,0), 3)
cv2.drawContours(img, cnts_yellow, -1, (0,0,0), 3)
cv2.drawContours(img, cnts_green, -1, (0,0,0), 3)

ans_red=0
ans_yellow=0
ans_green=0

if len(cnts_yellow) > 0:
    c = max(cnts_yellow, key=cv2.contourArea)
    ((x, y), radius) = cv2.minEnclosingCircle(c)
    M = cv2.moments(c)
    if M['m00']:
        center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
        if radius > 20:
            ans_yellow=ans_yellow+1
            cv2.circle(img, (int(x), int(y)), int(radius),(255, 0, 0), 2)

if len(cnts_green) > 0:
    c = max(cnts_green, key=cv2.contourArea)
    ((x, y), radius) = cv2.minEnclosingCircle(c)
    M = cv2.moments(c)
    center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
    if radius > 20:
        ans_green=ans_green+1
        cv2.circle(img, (int(x), int(y)), int(radius),(255, 0, 0), 2)


if len(cnts_red) > 0:
    c = max(cnts_red, key=cv2.contourArea)
    ((x, y), radius) = cv2.minEnclosingCircle(c)
    M = cv2.moments(c)
    center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
    if radius > 20:
        ans_red=ans_red+1
        cv2.circle(img, (int(x), int(y)), int(radius),(255, 0, 0), 2)


cv2.imshow('Final',img)

flag =False
if ans_red+ans_green+ans_yellow>=3:
    if ans_red==ans_yellow:
        if ans_yellow==ans_green:
            print('Traffic light Detected')
            flag=True
if flag==False:
    print('Sorry, we cannot detect a traffic light')

k=cv2.waitKey(0) & 0xFF

