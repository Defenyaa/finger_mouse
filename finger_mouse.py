import cv2
import numpy
import HandTracking as htm
import time
import autopy

#############################
# 1920*1080
wCam, hCam = 800, 600



#############################
cap = cv2.VideoCapture(0)
cap.set(3,wCam)
cap.set(4, hCam)
pTime = 0
detector = htm.handDetector(maxHands=1)

cx,cy = 0,0
while True:
    #1
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img)
    #2
    if len(lmList) != 0:
        # 食指
        x1, y1 = lmList[8][1:]

        if abs(cx-x1) <= 1 or abs(cy-y1) <= 1:
            continue
        cx, cy = x1,y1
        # print(cx1,cy1)

        # print(lmList)
        # print(x1,y1,x2,y2)

        #3
        px = abs(int((x1-715)*5.567))
        py = abs(int((y1-460)*5.567))
        print(px,py)
        if px>=1920 or px<=0 or py>=1080 or py<=0:
            continue
        else:

                autopy.mouse.move(px,py)



    #11
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv2.rectangle(img, (368, 280), (715, 460), (255, 0, 0), 3, 1, 0)
    cv2.putText(img, str(int(fps)), (20, 50), cv2.FONT_HERSHEY_PLAIN, 3,
    (255,0,0), 3)




    cv2.imshow("image", img)
    cv2.waitKey(1)





    pass



