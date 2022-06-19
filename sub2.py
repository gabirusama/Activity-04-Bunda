import cv2

print("Printing Arcana Xerath...")

filePath = 'red.jpg'
img = cv2.imread(filePath, 1)
cv2.imshow("red", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
