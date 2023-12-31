# Atharva Wadekar 21103A2004

import os
import cv2
from scipy import ndimage

PATH = 'Dataset/'
RESULTS = 'Results/'

def enhanceImage(path):

	for filename in os.listdir(path):

		try:
			image = cv2.imread(path+filename)
			if image is not None:
				# Convert image to gray scale
				gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

				# Non-Linear filter for noise removal
				deNoised = ndimage.median_filter(gray_image, 3)

				#Histogram Equalizer
				#High pass filter for improving the contrast of the image
    			#Contrast Limited Adaptive Histogram Equalization
				clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
				highPass = clahe.apply(deNoised)

				#Gamma Transformation
				#Prevent bleaching or darkening of images
				gamma = highPass/255.0
				gammaFilter = cv2.pow(gamma,1.5)
				gammaFilter = gammaFilter * 255

				cv2.imwrite(RESULTS+filename,gammaFilter)

		except:
		    print('Image not found')



print("--------IMAGE ENHANCEMENT TECHNIQUE----------")
print("---------------------------------------------")
print("--------INITIALIZED IMAGE PROCESSING---------")
# Enhance Image Quality
enhanceImage(path=PATH)
print("--------IMAGE PROCESSING COMPLETED-----------")

