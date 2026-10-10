import cv2

# BGR Image
img = cv2.imread('../1_Intro_to_images/img1.JPG')
img = cv2.resize(img, (500, 600))

# Convert to GrayScale Image
img_canny = cv2.Canny(img, 170, 170, apertureSize=3, L2gradient=True)
img_canny = cv2.resize(img_canny, (500, 600))

cv2.imshow('Image', img)
cv2.imshow('Canny Image', img_canny)
cv2.waitKey(0)
cv2.destroyAllWindows()