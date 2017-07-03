import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    temp , frame = cap.read()
    lower = np.array( [0,0,80]) #Set the lower value for color you want to detect ( BGR format )
    high = np.array( [ 50,50,255]) #Set the upper value for color you want to detect ( BGR format )

    mask=cv2.inRange(frame,lower,high)

    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]

    if len(cnts) > 0:
        c = max(cnts, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        M = cv2.moments(c)


        if M["m00"]: #Avoiding Divide By Zero Error
            center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
            if radius > 10:
                cv2.circle(frame, (int(x), int(y)), int(radius),(0, 255, 255), 2) 
                cv2.circle(frame, center, 5, (0, 0, 255), -1)

    cv2.imshow('Frame2', mask)
    cv2.imshow('Frame',frame)

    cv2.waitKey(10)

cap.release()
cv2.destroyAllWindows()
