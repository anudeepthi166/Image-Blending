import cv2
from matplotlib import pyplot as plt
p1=cv2.imread("linux-logo.jpeg")
p2=cv2.imread("linux.jpg")
p1=cv2.cvtColor(p1,cv2.COLOR_BGR2RGB)
p2=cv2.cvtColor(p2,cv2.COLOR_BGR2RGB)
size=int(input())
p1=cv2.resize(p1,(size,size))
p2=cv2.resize(p2,(size,size))
dest=cv2.addWeighted(p1,0.5,p2,0.5,0)
plt.imshow(dest)
dest=cv2.cvtColor(dest,cv2.COLOR_RGB2BGR)
plt.imshow(dest)
cv2.imwrite("blend.jpg",dest)
