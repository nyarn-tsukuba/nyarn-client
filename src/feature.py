from deepface import DeepFace
import datetime
import cv2


def feature(img_file):
    now = datetime.datetime.now()
    img = cv2.imread(img_file)
    objs = DeepFace.analyze(
            img_path = img,
            actions = ['age', 'gender', 'emotion']
    )
    list_date = []
    list_date.append(now.strftime("%Y/%m%d/%H%M"))
    list_date.append(objs[0]['age'])
    list_date.append(objs[0]['dominant_gender'])
    list_date.append(objs[0]['dominant_emotion'])

    print(list_date)

#feature("test2.jpg")