import cv2
from pprint import pprint
#pprint(cv2)
#img=cv2.imread("gpay.png")
img = cv2.imread("day10/gpay.png")
cv2.imshow("Image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cap=cv2.VideoCapture(0)
#pprint(cap)
while True:
    ret,frame=cap.read()
    if not ret:
        break
    cv2.imshow("LiveCamera", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break