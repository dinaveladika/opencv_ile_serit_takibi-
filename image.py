import cv2
import numpy as np
import matplotlib.pylab as plt

def reigon_of_interest(image,vertices):
    mask=np.zeros_like(image)# bu metod , resmimiz ile aynı ancak degerleri  0 olan bir matris olusturur.
    match_mask_color= 255 # kırmızı rengi
    cv2.fillPoly(mask,vertices,match_mask_color)# bu metod ile köşe kordinatlari verilen bir cokgenin içini boyariz. 
    masked_image=cv2.bitwise_and(image,mask)# olusturdugumuz maske ile orjinal resmin ,bitwise_and işlemi yaptık. burda resmin ve maskenin karşılıklı pixelleri arasında and işlemi yapılır. 0 varsa 0 döner boylece fillpoly ile boyadiğimiz  alanı (ilgilendiğimiz alanı) elde ederiz ve diger alanlar maskelenir. 
    return masked_image # figure_4 gibi


def draw_lines(image,lines): # resimdeki cizgilerin baslangiç ve bitiş kordinatlari kullanarak  cv2.line metodu ile cizgiler cizeriz
    image=np.copy(image)
    blank_image=np.zeros((image.shape[0],image.shape[1],3), dtype=np.uint8)

    for line in lines:
        for x1,y1,x2,y2 in line:
            cv2.line(blank_image,(x1,y1),(x2,y2),(0,255,0),5)
    image=cv2.addWeighted(image,0.8,blank_image,1, 0.0)
    return image



img=cv2.imread("lane.jpg")# resmi okuduk
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)# resmi RGB renk uzayı ile tanımlıyoruz
print(img.shape)# shape metodo ise ,resmimiz  renkli ise 3 elemanlı bir tupple döndürür.(yukseklik,genişlik,renk kanal sayısı(RGB de 3 renk kanalı var) )
height= img.shape[0]
width= img.shape[1]
# ilgili alanın köşe kordinatlari
reigon_of_interest_vertices=[
    (0,4*height/5),
    (width/2,height/2),
    (width,4*height/5),
    (width/2,height)
] 
gray_image=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)# resmi gri rengine donuşturur
canny_image=cv2.Canny(gray_image,100,450)# bu metod , resimdeki pixellerin  yogun oldugu noktaları cizgi olarak gosterir >> figure_3 gibi

cropped_image=reigon_of_interest(canny_image ,np.array([reigon_of_interest_vertices],np.int32),) # yazdıgımız fonksiyon ile resmi maskeliyoruz

# houghline donusumu ile dogruları algılıyoruz ve bunları lines adlı bir dizide atıyoruz
lines= cv2.HoughLinesP(cropped_image,rho=6,theta=np.pi/60,threshold=160,lines=np.array([]),minLineLength=40,maxLineGap=25)

image_with_lines=draw_lines(img,lines)

plt.imshow(image_with_lines)
plt.show()
