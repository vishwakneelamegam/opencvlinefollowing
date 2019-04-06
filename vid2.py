import cv2
import numpy as np
import time
c=cv2.VideoCapture(0)
while True:
    ret,frame=c.read()
    cv2.line(frame,(0,400),(800,400),(0,255,0),1)
    cv2.line(frame,(0,397),(800,397),(0,255,0),1)
    cv2.line(frame,(79,350),(79,450),(0,255,0),1)
    cv2.line(frame,(81,350),(81,450),(0,255,0),1)
    cv2.line(frame,(99,350),(99,450),(0,255,0),1)
    cv2.line(frame,(101,350),(101,450),(0,255,0),1)
    cv2.line(frame,(449,350),(449,450),(0,255,0),1)
    cv2.line(frame,(451,350),(451,450),(0,255,0),1)
    cv2.line(frame,(469,350),(469,450),(0,255,0),1)
    cv2.line(frame,(471,350),(471,450),(0,255,0),1)
    font = cv2.FONT_HERSHEY_SIMPLEX
    g = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    px2 = frame[398,100]
    px4 = frame[398,470]
    px1 = frame[398,450]
    px3 = frame[398,80]
    v1  = 0
    v2  = 0
    v3  = 0
    v4  = 0
    ans = 0
    if px3[0]>100:
        cv2.putText(frame,'LEFT1',(10,100), font, 2, (200,255,155), 5)
        v1 = 1
    if px2[0]>100:
        cv2.putText(frame,'LEFT',(10,100), font, 2, (200,255,155), 5)
        v2 = 1
    if px2[0]<50 and px1[0]<50 and px3[0]<50 and px4[0]<50:
        cv2.putText(frame,'GO',(10,100), font, 2, (200,255,155), 5)
        v1 = 0
        v2 = 0
    if px1[0]>100:
        cv2.putText(frame,'RIGHT',(10,100), font, 2, (200,255,155), 5)
        v3 = 1
    if px4[0]>100:
        cv2.putText(frame,'RIGHT1',(10,100), font, 2, (200,255,155), 5)
        v4 = 1
    ans      = v1 + v2
    leftans  = (float(ans)/float(2))*float(100)
    ans1     = v3 + v4
    rightans = (float(ans1)/float(2))*float(100)
    #print (ans)
    #print (ans1)
    print "left side percentage  : ",leftans
    print "right side percentage : ",rightans
    time.sleep(0.1)
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
c.release()
cv2.destroyAllWindows()  
