import cv2
import time
from numpy import *
from PIL import ImageGrab
from matplotlib import pyplot as plt

#Constant Settings
Kernel=cv2.getStructuringElement(cv2.MORPH_RECT,(6,6))
F=993.95

#Color Histogram
def CH_Plot(img):
    Color=('b','g','r')
    for i,col in enumerate(Color):
        Hist=cv2.calcHist([img],[i],None,[256],[0,256])
        plt.plot(Hist,Color=col)
    plt.xlim([0,256])
    plt.show()

#Red Cube Filter
def RedFilter(RGB):
    lower_red1=array([0,0,100])
    upper_red1=array([85,85,255])
    mask1=cv2.inRange(RGB,lower_red1,upper_red1)
    mask=cv2.dilate(mask1,Kernel)
    return mask1

#Draw Rectangle
def Draw(img,origin):
    img_cp=img.copy()
    _,cnts,_=cv2.findContours(img_cp,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    if len(cnts)==0: return [[0,0],[0,0],[0,0],[0,0]]
    cnt_fst=sorted(cnts,key=cv2.contourArea,reverse=True)[0]
    box=cv2.minAreaRect(cnt_fst)
    Points=int0(cv2.boxPoints(box))
    cv2.rectangle(origin,tuple(Points[0]),tuple(Points[2]),(255,255,255))
    return (Points)

#Focus Calculation
def CalcF(Pix,Dist):
    return (Pix*Dist/4)

print("进入图像测试......")
while (1):
    im=ImageGrab.grab((5,46,900,570))
    im.save('1.jpg')
    origin=cv2.imread('1.jpg')
    cv2.imshow('Res',res)
    if cv2.waitKey(1) & 0xFF==ord('y'):
        break    
    time.sleep()

print("5秒后进入物体识别模式......")
time.sleep(5)
while (1):
    im=ImageGrab.grab((5,46,900,570))
    im.save('1.jpg')
    origin=cv2.imread('1.jpg')
    #cv2.imshow('origin',origin)
    #CH_Plot(origin)
    F1=RedFilter(origin)
    res=cv2.bitwise_and(origin,origin,mask=F1)
    Points=Draw(F1,res)
    Pix=Points[:,1].max()-Points[:,1].min()
    Dist=4*F/Pix
    print("Distance: ",Dist)
    cv2.imshow('Res',res)
    if cv2.waitKey(1) & 0xFF==ord(' '):
        break    
    time.sleep(0.5)

cv2.destroyAllWindows()    
    
#sample=cv2.imread('imgsave\sample.jpg')
#cv2.imshow('sample',sample)
#CH_Plot(sammple)

