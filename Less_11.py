import cv2
from PIL import Image

image_cat = 'cat.jpeg'
cat_face_cascade = cv2.CascadeClassifier('haarcascade_frontalcatface_extended.xml')
image = cv2.imread(image_cat)
cat_face = cat_face_cascade.detectMultiScale(image)

print(cat_face)

cat = Image.open(image_cat)
glasses = Image.open('glasses.png')
cat = cat.convert('RGBA')
glasses = glasses.convert('RGBA')


for (x,y,w,h) in cat_face:
    glasses = glasses.resize(( w, int(h/3)))
    cat.paste(glasses, (x,int(y+h/4)), glasses)

    cat.save('cat911.png')
    cat911 = cv2.imread('cat911.png')
    cv2.imshow('cat911', cat911)
    cv2.waitKey()

cv2.imshow("cat", image)
cv2.waitKey()


