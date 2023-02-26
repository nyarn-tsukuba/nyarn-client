import cv2
import torch
import time
import src.feature as Feature
import psycopg2
# データベースに接続するための情報を指定
host = "nyarnnyan.postgres.database.azure.com"
dbname = "postgres"
user = "nyarnadmin"
password = "OEk945I-mkLTslP53"
sslmode = "require"
conn_string = "host={0} user={1} dbname={2} password={3} sslmode={4}".format(host, user, dbname, password, sslmode)
conn = psycopg2.connect(conn_string)
print("Connection established")
cursor = conn.cursor()


# 人物認識
model = torch.hub.load("ultralytics/yolov5", "yolov5s", pretrained=True)
cap = cv2.VideoCapture(0)
count = 0
while True:
    ret, frame = cap.read()
    cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    result = model(frame)
    #推論結果を取得
    obj = result.pandas().xyxy[0]
    #バウンディングボックスの情報を取得
    for i in range(len(obj)):
        if obj.name[i] == 'person' and obj.confidence[i] >= 0.75:
            cv2.imwrite('./image/image_1.jpg', frame)
            count += 1
            print('OK')

            # conn = psycopg2.connect(conn_string)
            # print("Connection established")
            # cursor = conn.cursor()

            try:
                person = Feature.feature("./image/image_1.jpg")
                querya =  f"INSERT INTO nyantable (time,age,sex,emotion) VALUES ('{person[0]}',{person[1]},'{person[2]}','{person[3]}');"
                cursor.execute(querya)
                conn.commit()
                #cursor.close()
                #conn.close()
            except ValueError:
                print('マスクを外してください')
            
            time.sleep(5)
            print('restart')
        else:
            print('wait...')
cursor.close()
conn.close()
cv2.destroyAllWindows()