import cv2 as cv

image = cv.imread("C:/Users/Nima Rezaei/PycharmProjects/OpenCV/images/git.png", cv.IMREAD_COLOR)

cv.rectangle(image, (275, 265), (600, 340), (0, 255, 0), 2)
cv.ellipse(image, (465, 280), (300, 210), 90, 0, 360, (0, 0, 255), 2)
# eyes/rectangle
cv.putText(image, 'Eyes', (275, 258), cv.FONT_HERSHEY_SIMPLEX, 1,
           (100, 255, 50), 1, cv.LINE_AA)
# face/ellipse
cv.putText(image, 'Face', (680, 280), cv.FONT_HERSHEY_SIMPLEX, 1,
           (100, 0, 255), 1, cv.LINE_AA)

cv.imshow('colored image', image)
cv.waitKey(0)
cv.destroyAllWindows()
