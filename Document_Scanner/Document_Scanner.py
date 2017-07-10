import cv2
import numpy as np

def distance(x1,y1,x2,y2):
    return np.sqrt(((x1-x2)**2)+((y1-y2)**2))

def point_orderer(pts):

    rect = np.zeros((4,2),dtype="float32")

    s = pts.sum(axis=1)
    rect[0]=pts[np.argmin(s)] #Top-Left
    rect[2]=pts[np.argmax(s)] #Bottom-Right

    differ = np.diff(pts,axis=1)
    rect[1]=pts[np.argmin(differ)] #Top-Right
    rect[3]=pts[np.argmax(differ)] # Bottom-Left

    return rect

def four_point_transform(img,pts):

    rect = point_orderer(pts)
    ( tl ,tr, br, bl) = rect

    width1 = distance(bl[0],bl[1],br[0],br[1])
    width2 = distance(tl[0],tl[1],tr[0],tr[1])
    maxwidth = int(max(width1,width2))

    height1 = distance(bl[0], bl[1], tl[0], tl[1])
    height2 = distance(br[0], br[1], tr[0], tr[1])
    maxheight = int(max(height1, height2))

    actual_dist = np.array( [
    [0,0],
    [maxwidth-1,0],
    [maxwidth-1,maxheight-1],
    [0,maxheight-1]
    ], dtype="float32")

    M = cv2.getPerspectiveTransform(rect,actual_dist)
    warped = cv2.warpPerspective(img, M, (maxwidth,maxheight))

    return warped

#Work starts here
path = "C:\\Users\\Rishabh Jain\\Desktop\\bill.jpg" # Path where image is located

img = cv2.imread(path,0)
edged = cv2.Canny(img,100,200)

red, cnts , _ = cv2.findContours(edged.copy(),cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)

cnts = sorted(cnts,key=cv2.contourArea,reverse=True)

for c in cnts:
    peri = cv2.arcLength(c,True)
    approx = cv2.approxPolyDP(c,0.1*peri,True)

    if len(approx)==4:
        screencnt = approx
        print(approx)
        break

cv2.drawContours(img,[screencnt],-1,(0,255,0),2)
height, width = img.shape[:2]
cv2.imshow('Orig Image with Contour',img)
warped = four_point_transform(img,screencnt.reshape(4,2))

thresh = cv2.adaptiveThreshold(warped,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)

cv2.imshow('Fianl Img',thresh)

cv2.waitKey(0)

cv2.destroyAllWindows()