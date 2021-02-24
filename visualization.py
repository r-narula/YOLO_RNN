import cv2
img = cv2.imread("/home/mononoke/Desktop/data/images_only/frame0.jpg")
img = cv2.resize(img,(224,224))
img = cv2.rectangle(img,(59,18),(137,205),(255,0,0),2)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()