import cv2
from cv2 import waitKey

img = cv2.imread("img/lena.png")

print(type(img))

print('Shape: ', img.shape)
print('Size: ', img.size)
print('DType: ', img.dtype)

b, g, r = cv2.split(img)

# print('R: ', r)
# print('G: ', g)
# print('B: ', b)

cv2.imshow('Lena', img)
cv2.imshow('Red', r)
cv2.imshow('Green', g)
cv2.imshow('Blue', b)
# waitKey(0)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

h, s, v = cv2.split(hsv)

print('H: ', h)
print('S: ', s)
print('V: ', v)

cv2.imshow('Hue', h)
cv2.imshow('Saturation', s)
cv2.imshow('Value', v)

waitKey(0)