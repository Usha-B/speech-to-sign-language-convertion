import speech_recognition as sr
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from easygui import *
import os
#import selecting
# obtain audio from the microphone
def func():
        r = sr.Recognizer()
        arr=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        with sr.Microphone() as source:

                r.adjust_for_ambient_noise(source)
                i=0
                while True:	    
                        print('Say something')
                        audio = r.listen(source)

                                                        # recognize speech using Sphinx
                        try:
                                a=r.recognize_google(audio)
                                print("you said " + a)
                                if(a=='goodbye'):
                                        print("oops!Time To say good bye")				
                                        break
                                for i in range(len(a)):
                                                #a[i]=a[i].lower()
                                                if(a[i] in arr):
                                                        ImageAddress = 'letters/'+a[i]+'.jpg'
                                                        ImageItself = Image.open(ImageAddress)
                                                        ImageNumpyFormat = np.asarray(ImageItself)
                                                        plt.imshow(ImageNumpyFormat)
                                                        plt.draw()
                                                        plt.pause(0.3) # pause how many seconds
                                                        #plt.close()
                                                else:
                                                        continue
                                
                        except:
                               print("Could not listen")
                        plt.close()

#func()
while 1:
  image   = "signlang.png"
  msg="HEARING IMPAIRMENT ASSISTANT"
  choices = ["Live Voice","All Done!","Recorded Audio"]
  reply   = buttonbox(msg,image=image,choices=choices)
  if reply ==choices[0]:
        func()
  if reply == choices[1]:
        quit()
  if reply==choices[2]:
        os.system("selecting.py")

