import cv2

img1 = cv2.imread('img/circle1.png')
img2 = cv2.imread('img/circle2.png')

img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

op_and = cv2.bitwise_and(img1, img2)
op_or = cv2.bitwise_or(img1, img2)
op_xor = cv2.bitwise_xor(img1, img2)

with open('op_and.txt', 'w') as f:
    f.write(str(op_and))

with open('op_or.txt', 'w') as f:
    f.write(str(op_or))

with open('op_xor.txt', 'w') as f:
    f.write(str(op_xor))

cv2.imshow('Image 1', img1)
cv2.waitKey(0)
cv2.imshow('Image 2', img2)
cv2.waitKey(0)
cv2.imshow('AND', op_and)
cv2.waitKey(0)
cv2.imshow('OR', op_or)
cv2.waitKey(0)
cv2.imshow('XOR', op_xor)
cv2.waitKey(0)