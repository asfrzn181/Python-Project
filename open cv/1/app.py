import cv2 as cv
import sys

img = cv.imread(cv.samples.findFile("gambar.jpg"))

if img is None:
	sys.exit("Tidak dapat membaca gambar")

cv.imshow("Display window",img)
k = cv.waitKey(0)

if k == ord("s"):
	cv.imwrite("gambar.jpg",img)