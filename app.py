import cv2
import torch
import time
import src.feature

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
            cv2.imwrite(f'./image/image_1.jpg', frame)
            count += 1
            print('OK')
            time.sleep(5)
            print('restart')
        else:
            print('wait...')













# import tkinter as tk
# import tkinter.ttk as ttk

# def search():
#     text.set("Finish")


# # 感情推定
# from deepface import DeepFace

# def feture(img_file):
#     objs = DeepFace.analyze(
#             img_path = img_file,
#             actions = ['age', 'gender', 'emotion']
#     )
#     list = []
#     list.append(objs[0]['age'])
#     list.append(objs[0]['dominant_gender'])
#     list.append(objs[0]['dominant_emotion'])

#     print(list)




# # rootメインウィンドウの設定
# root = tk.Tk()
# root.title("にゃーん")
# root.geometry("200x100")

# # メインフレームの作成と設置
# frame = ttk.Frame(root)
# frame.pack(fill = tk.BOTH, padx=20,pady=10)

# # StringVarのインスタンスを格納する変数textの設定
# text = tk.StringVar(frame)
# text.set("Search")

# # 各種ウィジェットの作成
# button = tk.Button(frame, textvariable=text, command=search)

# # 各種ウィジェットの設置
# button.pack()

# #print("debug")

# root.mainloop()