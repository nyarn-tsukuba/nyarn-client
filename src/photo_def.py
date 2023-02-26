import torch
import time

def detect_face(jpg):
    model = torch.hub.load("ultralytics/yolov5", "yolov5s", pretrained=True) 
    result = model(jpg)
    obj = result.pandas().xyxy[0]
    for i in range(len(obj)):
        if obj.name[i] == 'person' and obj.confidence[i] >= 0.75:
            print('OK')
            return jpg
            time.sleep(5)
        else:
            pass