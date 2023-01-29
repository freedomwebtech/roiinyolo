import torch
import cv2
import numpy as np

def POINTS(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE :  
        colorsBGR = [x, y]
        print(colorsBGR)
        

cv2.namedWindow('ROI')
cv2.setMouseCallback('ROI', POINTS)



model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
count=0
while True:
    frame=stream.read()
#    count += 1
#    if count % 3 != 0:
#        continue
    
    frame=cv2.resize(frame,(1020,500))
    results = model(roi)
    for index, row in results.pandas().xyxy[0].iterrows():
        x1 = int(row['xmin'])
        y1 = int(row['ymin'])
        x2 = int(row['xmax'])
        y2 = int(row['ymax'])
        d=(row['name'])
        print(d)
    cv2.imshow("ROI",frame)
    if cv2.waitKey(1)&0xFF==27:
        break
stream.release()
cv2.destroyAllWindows()