from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import re
import requests
import urllib.request
import binascii
import struct
from PIL import Image
import numpy as np
import scipy
import scipy.misc
import scipy.cluster
from webcolors import hex_to_name

colorlist = []
a = 1


def imagecalc():
	NUM_CLUSTERS = 5
	print('reading image')
	im = Image.open('img/image.jpg')
	im = im.resize((150, 150))  # optional, to reduce time
	ar = np.asarray(im)
	shape = ar.shape
	ar = ar.reshape(scipy.product(shape[:2]), shape[2]).astype(float)

	codes, dist = scipy.cluster.vq.kmeans(ar, NUM_CLUSTERS)

	vecs, dist = scipy.cluster.vq.vq(ar, codes)  # assign codes
	counts, bins = scipy.histogram(vecs, len(codes))  # count occurrences

	index_max = scipy.argmax(counts)  # find most frequent
	peak = codes[index_max]
	colour = binascii.hexlify(bytearray(int(c) for c in peak)).decode('ascii')
	colourHSV = convertToHSV(colour)
	colorlist.append(colourHSV)

def convertToHSV(rgbColor):
		h = rgbColor
		rgb = tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
		r = rgb[0]
		g = rgb[1]
		b = rgb[2]

		r, g, b = r / 255.0, g / 255.0, b / 255.0
  
	# h, s, v = hue, saturation, value 
		cmax = max(r, g, b)    # maximum of r, g, b 
		cmin = min(r, g, b)    # minimum of r, g, b 
		diff = cmax-cmin       # diff of cmax and cmin. 
  
	# if cmax and cmax are equal then h = 0 
		if cmax == cmin:  
			h = 0
	  
	# if cmax equal r then compute h 
		elif cmax == r:  
			h = (60 * ((g - b) / diff) + 360) % 360
  
	# if cmax equal g then compute h 
		elif cmax == g: 
			h = (60 * ((b - r) / diff) + 120) % 360
  
	# if cmax equal b then compute h 
		elif cmax == b: 
			h = (60 * ((r - g) / diff) + 240) % 360
  
		# if cmax equal zero 
		if cmax == 0: 
			s = 0
		else: 
			s = (diff / cmax) * 100
  
	# compute v 
		v = cmax * 100
		
		hsvTuple = (h,s,v)
		print(hsvTuple)
		return hsvTuple



count = 0
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--log-level=3")

driver = webdriver.Chrome(options=chrome_options)
driver.get("http://4chan.org/biz/catalog")
images = driver.find_elements_by_tag_name('img')

for image in images:
	urllib.request.urlretrieve(image.get_attribute('src'), 'img/image.jpg')
	try:
		imagecalc()
	except:
		print("oof")
	count += 1

driver.close()

print(colorlist)

redTotal = 0
greenTotal = 0
imageTotal = 0
hueTotal = 0
satTotal = 0
vTotal = 0

for rgbValue in colorlist:
	hue = rgbValue[0]
	sat = rgbValue[1]
	v = rgbValue[2]

	##grey / blackness check
	if sat and v > 30:
		##check for red / green
		if hue > 0 and hue < 60:
			redTotal += 1
			
		elif hue > 100 and hue < 180:
			greenTotal += 1

	hueTotal += hue
	satTotal += sat
	vTotal += v
	imageTotal += 1
	
hueAvg = hueTotal / imageTotal
satAvg = satTotal / imageTotal
vAvg = vTotal / imageTotal
##TODO: show reddest & greenest image lol?

print(greenTotal)
print(redTotal)
print(imageTotal)
print(hueAvg)
print(satAvg)
print(vAvg)

results = {
    "greenTotal": greenTotal,
    "redTotal": redTotal,
    "imageTotal": imageTotal,
    "hueAvg": hueAvg,
    "satAvg": satAvg,
	"vAvg": vAvg
}