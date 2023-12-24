import cv2

car_cascade=cv2.CascadeClassifier("C:\\Users\\dinav\\OneDrive\\Desktop\\opencv\\cars.xml")

cap=cv2.VideoCapture("C:\\Users\\dinav\\OneDrive\\Desktop\\opencv\\video1.mp4")
while 1:
    ret,frame=cap.read()
    frame=cv2.resize(frame,(500,500))
    gray=cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)
    cv2.namedWindow("arac",cv2.WINDOW_NORMAL)
    cars=car_cascade.detectMultiScale(gray,1.2,4)


    for x,y,w,h in cars :
     cv2.rectangle(gray,(x,y),(x+w,y+h),(0,0,255),4)
       # araba konumu =(x+(w/2),y+(h/2))
     cv2.imshow("arac",frame)

     if cv2.waitKey(1) & 0xFF==ord("q"):
        break
     


cap.release()
cv2.destroyAllWindows()