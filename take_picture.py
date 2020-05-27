import cv2

cpt = 0
maxFrames = 1

try:
    vidStream = cv2.VideoCapture(0)
except:
    print ("problem opening input stream")
    sys.exit(1)

while cpt < maxFrames:
    ret, frame = vidStream.read()
    if not ret:
        sys.exit(0)
    cv2.imshow("test window", frame)
    cv2.imwrite("exemple%04i.jpg" %cpt, frame)
    cpt += 1
