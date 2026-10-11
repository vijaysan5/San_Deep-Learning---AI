import cv2
import numpy as num

#   1_____Read Image :
Rose = cv2.imread("San's  DataScience Folder/Deep Learning Folder/Logo Images.png")

#   2_____Resize Image :
Resz = cv2.resize(Rose, (600, 400))

#   3_____Change Color >>> Orginal into Gray :
Gray = cv2.cvtColor(Rose, cv2.COLOR_BGR2GRAY)

#   4_____Blur Image :
Blur = cv2.GaussianBlur(Gray, (3, 3), 0)

#   5_____Canny Edge Detecation :
Edge = cv2.Canny(Blur, 100, 200)

#   6_____Threshold :
_, Thresh = cv2.threshold(Gray, 127, 255, cv2.THRESH_BINARY)

#   7_____Flip :
Flip = cv2.flip(Rose, 1)

#   8_____Rotate :
Rotate = cv2.rotate(Rose, cv2.ROTATE_90_CLOCKWISE)

#   9_____Draw a Circle :
Circle = Rose.copy()
cv2.circle(Circle, (150, 250), 60, (290, 0, 0), 2)

#  10_____Draw a Rectangle :
Rect = Rose.copy()
cv2.rectangle(Rect, (100, 100), (300,250), (0, 290, 0), 2)

#  11_____Draw a Line :
Line = Rose.copy()
cv2.line(Line, (0, 0), (200, 300), (0, 0, 290), 2)

#   12_____Add a Text :
Text = Rose.copy()
cv2.putText(Text, "ORANGE_ROSE", (20, 70),
           cv2.FONT_HERSHEY_SIMPLEX,
           1, (290, 290, 290), 2)

#  13_____Find Contours :
Contours, Hierarchy = cv2.findContours(
    Thresh,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)

#  14_____Draw Contour :
Cont = Rose.copy()
cv2.drawContours(Cont, Contours, -2, (0, 290,  290), 2)


#  Show Output :
cv2.imshow("1. Orginal Image", Rose)
cv2.imshow("2. Resize Image", Resz)
cv2.imshow("3. Convert Color", Gray)
cv2.imshow("4. Blur Image", Blur)
cv2.imshow("5. Edge Canny", Edge)
cv2.imshow("6. Threshold", Thresh)
cv2.imshow("7. Flip Image", Flip)
cv2.imshow("8. Rotate Image :", Rotate)
cv2.imshow("9. Draw Circle", Circle)
cv2.imshow("10. Draw Rectangle", Rect)
cv2.imshow("11. Draw Line", Line)
cv2.imshow("12. Add Text", Text)
cv2.imshow("13. Contours", Cont)


cv2.waitKey(0)
cv2.destroyAllWindows()