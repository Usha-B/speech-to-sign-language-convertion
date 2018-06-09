import speech_recognition as sr
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# obtain audio from the microphone
r = sr.Recognizer()
arr=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
with sr.Microphone() as source:

	r.adjust_for_ambient_noise(source)
	i=0
	while True:	    
		audio = r.listen(source)

						# recognize speech using Sphinx
		try:
			a=r.recognize_google(audio)
			print("Sphinx thinks you said " + a)
			if(a=='bye bye'):
				print("Oops!Time To say good bye")				
				break
			for i in range(len(a)):
					if(a[i] in arr):
						ImageAddress = 'letters/'+a[i]+'.jpg'
						ImageItself = Image.open(ImageAddress)
						ImageNumpyFormat = np.asarray(ImageItself)
						plt.imshow(ImageNumpyFormat)
						plt.draw()
						plt.pause(1) # pause how many seconds
						plt.close()
					else:
						continue
			
		except:
		       print("Could not listen")


             