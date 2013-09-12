import cv2


cv2.namedWindow("preview")
cv2.namedWindow("average")
vc = cv2.VideoCapture(0)

vc.set(3,360)
vc.set(4,240)
vc.set(15, 0.05)

key = cv2.waitKey(2000)
frame = None
lastframe = None
diff = None
average = None
if vc.isOpened(): # try to get the first frame
    print "camera open"
    rval, frame = vc.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    rval, lastframe = vc.read()
    lastframe = cv2.cvtColor(lastframe, cv2.COLOR_BGR2GRAY)
    rval,diff = vc.read()
    diff = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    rval, average = vc.read()
    average = cv2.cvtColor(average, cv2.COLOR_BGR2GRAY)
else:
    rval = False


while rval:
    #print "frame", frame
    for line,x in enumerate(frame):
        #print "line",line
        for pixel,y in enumerate(frame[line]):
            #print "pixel",pixel
            average[line][pixel] = (average[line][pixel]*8.0 +  frame[line][pixel]*2.0)/10.0

    #diff = lastframe - frame
    #diff = diffImg(lastframe,frame)
    cv2.imshow("average", average)
    cv2.imshow("preview", frame)
    lastframe = frame
    for i in range(0,30):
        rval, frame = vc.read()
    rval, frame = vc.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    key = cv2.waitKey(10)
    if key == 27: # exit on ESC
        break