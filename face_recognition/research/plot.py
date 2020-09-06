import os
import cv2
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
img1 = cv2.imread(BASE_DIR + '/images/user.123.6.jpg')
gray_img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

def Binary_pattern(im):                               # creating function to get local binary pattern
    img= np.zeros_like(im)
    n=3                                             
    for i in range(0,im.shape[0]-n):                 
      for j in range(0,im.shape[1]-n):              
            x  = im[i:i+n,j:j+n]                     
            center       = x[1,1]                    
            img1        = (x >= center)*1.0          
            img1_vector = img1.T.flatten()            
            img1_vector = np.delete(img1_vector,4)  
            digit = np.where(img1_vector)[0]         
            if len(digit) >= 1:                     
                num = np.sum(2**digit)              
            else:                                    
                num = 0
            img[i+1,j+1] = num
    return(img)




imgLBP_1=Binary_pattern(gray_img1)           
vectorLBP_1 = imgLBP_1.flatten()              
fig_1=plt.figure(figsize=(20,8))             
ax_1  = fig_1.add_subplot(1,3,1)
ax_1.imshow(gray_img1)
ax_1.set_title("gray scale image")
ax_1  = fig_1.add_subplot(1,3,2)
ax_1.imshow(imgLBP_1,cmap="gray")
ax_1.set_title("LBP converted image")
ax_1  = fig_1.add_subplot(1,3,3)
freq,lbp, _ = ax_1.hist(vectorLBP_1,bins=2**8)       
ax_1.set_ylim(0,15000)
lbp = lbp[:-1]


## print the LBP values when frequencies are high
largeTF = freq > 1000
for x, fr in zip(lbp[largeTF],freq[largeTF]):
     ax_1.text(x,fr, "{:6.0f}".format(x),color="magenta")
ax_1.set_title("LBP histogram")
plt.savefig(BASE_DIR + '/plot_images/LBP_plot.png') #saving as LBP_plot.png instead of manually saving
plt.show()