import cv2

car_cascade=cv2.CascadeClassifier("C:\\Users\\dinav\\OneDrive\\Desktop\\opencv\\cars.xml")

img=cv2.imread("araba.jpeg")
gray=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
cv2.namedWindow("arac",cv2.WINDOW_NORMAL)
cars=car_cascade.detectMultiScale(gray,1.6,2)
for x,y,w,h in cars :
    cv2.rectangle(gray,(x,y),(x+w,y+h),(0,0,255),2)

cv2.imshow("arac",img)
cv2.waitKey()
cv2.destroyAllWindows()