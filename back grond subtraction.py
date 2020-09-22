import cv2


#cap=cv2.VideoCapture('vtest.avi')
import sys
import video
try:
    fn = sys.argv[1]
except IndexError:
    fn = 0
cap = video.create_capture(fn)









#MOG MOG2 GMG KNN
#fgbg = cv2.createBackgroundSubtractorMOG2()
kernal = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(4,4))
fgbg = cv2.createBackgroundSubtractorKNN(detectShadows= None)

while(cap.isOpened()):

 _,img =cap.read()


 frame =fgbg.apply(img)
# frame = cv2.morphologyEx(frame,cv2.MORPH_OPEN
 #                         ,kernal)

 cv2.imshow('image',img)
 cv2.imshow('subtraced',frame)
 if cv2.waitKey(30) ==ord('q'):
   break

cap.release()
cv2.destroyAllWindows()