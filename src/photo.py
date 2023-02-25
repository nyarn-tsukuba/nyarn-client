import cv2
import torch
import time

model = torch.hub.load("ultralytics/yolov5", "yolov5s", pretrained=True) 
# img = cv2.imread('./data/images/bus.jpg')
img = './data/images/image_1.jpeg'
cap = cv2.VideoCapture(0)
count = 0
while True:
    ret, frame = cap.read()
    result = model(frame)
    #推論結果を取得
    obj = result.pandas().xyxy[0]
    #バウンディングボックスの情報を取得
    for i in range(len(obj)):
        if obj.name[i] == 'person' and obj.confidence[i] >= 0.75:
            cv2.imwrite(f'./image/image_{count}.jpg', frame)
            count += 1
            print('OK')
            time.sleep(5)
            print('restart')
        else:
            print('wait...')