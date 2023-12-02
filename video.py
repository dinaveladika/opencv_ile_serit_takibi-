import cv2
import numpy as np
import matplotlib.pylab as plt

def reigon_of_interest(image,vertices):
    mask=np.zeros_like(image)
    match_mask_color= 255
    cv2.fillPoly(mask,vertices,match_mask_color)
    masked_image=cv2.bitwise_and(image,mask)
    return masked_image
def draw_lines(image,lines):
    image=np.copy(image)
    blank_image=np.zeros((image.shape[0],image.shape[1],3), dtype=np.uint8)

    for line in lines:
        for x1,y1,x2,y2 in line:
            cv2.line(blank_image,(x1,y1),(x2,y2),(0,255,0),5)
    image=cv2.addWeighted(image,0.8,blank_image,1, 0.0)
    return image



    #img=cv2.imread("lane.jpg")
    #img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
def procces(img):  
    print(img.shape)
    height= img.shape[0]
    width= img.shape[1]

    reigon_of_interest_vertices=[
        (0,4*height/5),
        (width/2,height/2),
        (width,4*height/5),
        (width/2,height)
    ] 
    gray_image=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    canny_image=cv2.Canny(gray_image,100,450)

    cropped_image=reigon_of_interest(canny_image ,np.array([reigon_of_interest_vertices],np.int32),)


    lines= cv2.HoughLinesP(cropped_image,rho=6,theta=np.pi/60,threshold=160,lines=np.array([]),minLineLength=40,maxLineGap=25)

    image_with_lines=draw_lines(img,lines)
    return image_with_lines

cap=cv2.VideoCapture("highway.mp4")

while(cap.isOpened()):
    ret ,frame=cap.read()
    frame=procces(frame)
    cv2.imshow("frame",frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
