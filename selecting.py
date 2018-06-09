from easygui import *

import speech_recognition as sr
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def files(file):
 from PIL import Image
 arr=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
 with open(file) as f:
            while True:
                    c = f.read(1)
                    c=c.lower()
                    print(c,end="")
                    if not c:
                            print ("End of file")
                            break
                    else:			
                            if(c in arr):
                                                    ImageAddress = 'letters/'+c+'.jpg'
                                                    ImageItself = Image.open(ImageAddress)
                                                    ImageNumpyFormat = np.asarray(ImageItself)
                                                    plt.imshow(ImageNumpyFormat)
                                                    plt.draw()
                                                    plt.pause(.3) # pause how many seconds
						#
                            else:
                                                    continue
 plt.close()                                 
		
i=0
a=0
#while i<a :
image   = "file.jpg"
 
choices = ["file 1","file 2","file 3","file 4","file 5","exit"]
reply   = buttonbox(image=image,choices=choices)
if reply == choices[0]:
      aaa="trans.txt"
      files(aaa)
if reply ==choices[5]:
      quit()








      
	




