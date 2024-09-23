import cv2
import time
import numpy as np
import HandTrackingModule as htm
import math
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

######################################
wCam, hCam = 640, 480
######################################


cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

pTime = 0

detector = htm.handDetector()

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = interface.QueryInterface(IAudioEndpointVolume)
#volume.GetMute()
#volume.GetMasterVolumeLevel()
volRange = volume.GetVolumeRange()


minVolum = volRange[0]
maxVolum = volRange[1]
volbar = 400
vol = 0
volper = 0

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)
    if len(lmList) != 0:
        #print(lmList[4], lmList[8])
        
        x1, y1 = lmList[4][1], lmList[4][2]
        x2, y2 = lmList[8][1], lmList[8][2]
        cx, cy = (x1+x2)//2, (y1+y2)//2
        
        cv2.circle(img, (x1, y1), 10, (255,0,255), cv2.FILLED)
        cv2.circle(img, (x2, y2), 10, (255,0,255), cv2.FILLED)
        cv2.line(img, (x1,y1), (x2,y2), (255,0,255), 3)
        cv2.circle(img, (cx, cy), 10, (255,0,255), cv2.FILLED)
        
        lenght = math.hypot(x2 - x1, y2 - y1)
        #print(lenght)
        
        # Hand range 50 - 300
        # volum range -65 - 0
        
        vol = np.interp(lenght, [50, 300], [minVolum, maxVolum])
        volbar = np.interp(lenght, [50, 300], [400, 150])
        volper = np.interp(lenght, [50, 300], [0, 100])
        print(int(lenght), vol)
        volume.SetMasterVolumeLevel(vol, None)
        
        if lenght < 50:
            cv2.circle(img, (cx, cy), 10, (0,255,0), cv2.FILLED)
    
    cv2.rectangle(img, (50,150), (85,400), (255, 0, 0), 3)
    cv2.rectangle(img, (50, int(volbar)), (85,400), (255, 0, 0), cv2.FILLED)
    cv2.putText(img, f'{int(volper)}%', (40,450), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2)
    
    # FPS
    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime
    cv2.putText(img, f'FPS : {int(fps)}', (30,50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
    
    cv2.imshow("Image", img)
    cv2.waitKey(1)