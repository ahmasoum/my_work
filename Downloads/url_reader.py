#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 13:54:28 2021

@author: faraadid
"""
from imutils import paths
import argparse
import requests
import cv2
import os

ap = argparse.ArgumentParser()
ap.add_argument("-u", "--urls", required=True,
	help="path to file containing image URLs")
ap.add_argument("-o", "--output", required=True,
	help="path to output directory of images")
ap.add_argument("-n", "--numbers", required=True,
	help="numbers of image you want")
args = vars(ap.parse_args())
# grab the list of URLs from the input file, then initialize the
# total number of images downloaded thus far
rows = open(args["urls"]).read().strip().split("\n")
total = 1
print("ttttt", total)
for url in rows:
	try:
		
		if url[-3:]=='png':
			r = requests.get(url, timeout=60)
			p2 = os.path.sep.join([args["output"], "{}.png".format(str(total).zfill(8))])
			f2=open(p2,"wb")
			f2.write(r.content)
			f2.close()
			ptxt = os.path.sep.join([args["output"], "{}.txt".format(str(total).zfill(8))])
			ff =open(ptxt,'w') 
			ff.write(url)
			ff.close()
			print("[INFO] downloaded: {}".format(p2))
		elif url[-3:]=='jpg':
			r = requests.get(url, timeout=60)
			p = os.path.sep.join([args["output"], "{}.jpg".format(str(total).zfill(8))])
			f = open(p, "wb")
			f.write(r.content)
			f.close()
			ptxt = os.path.sep.join([args["output"], "{}.txt".format(str(total).zfill(8))])
			ff =open(ptxt,'w') 
			ff.write(url)
			ff.close()
			print("[INFO] downloaded: {}".format(p))
		elif url[-4:]=='jpeg':
			r = requests.get(url, timeout=60)
			p3 = os.path.sep.join([args["output"], "{}.jpeg".format(str(total).zfill(8))])
			f3 = open(p3, "wb")
			f3.write(r.content)
			f3.close()
			ptxt = os.path.sep.join([args["output"], "{}.txt".format(str(total).zfill(8))])
			ff =open(ptxt,'w') 
			ff.write(url)
			ff.close()
			print("[INFO] downloaded: {}".format(p3))			
		# update the counter
		total += 1
		if total == int(args["numbers"])+1:
			break
	# handle if any exceptions are thrown during the download process
	except:
		print("[INFO] error downloading {}...skipping".format(p))


for imagePath in paths.list_images(args["output"]):
	txtpath=imagePath.replace("jpg", "txt")
	# initialize if the image should be deleted or not
	delete = False
	# try to load the image
	try:
		image = cv2.imread(imagePath)
		# if the image is `None` then we could not properly load it
		# from disk, so delete it
		if image is None:
			delete = True
	# if OpenCV cannot load the image then the image is likely
	# corrupt so we should delete it
	except:
		print("Except")
		delete = True
	# check to see if the image should be deleted
	if delete:
		print("[INFO] deleting {}".format(imagePath))
		os.remove(imagePath)
		os.remove(txtpath)




















