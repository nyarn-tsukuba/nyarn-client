import tkinter as tk
import tkinter.ttk as ttk

def search():
    text.set("Finish")


# 感情推定
from deepface import DeepFace

def feture(img_file):
    objs = DeepFace.analyze(
            img_path = img_file,
            actions = ['age', 'gender', 'emotion']
    )
    list = []
    list.append(objs[0]['age'])
    list.append(objs[0]['dominant_gender'])
    list.append(objs[0]['dominant_emotion'])

    print(list)




# rootメインウィンドウの設定
root = tk.Tk()
root.title("にゃーん")
root.geometry("200x100")

# メインフレームの作成と設置
frame = ttk.Frame(root)
frame.pack(fill = tk.BOTH, padx=20,pady=10)

# StringVarのインスタンスを格納する変数textの設定
text = tk.StringVar(frame)
text.set("Search")

# 各種ウィジェットの作成
button = tk.Button(frame, textvariable=text, command=search)

# 各種ウィジェットの設置
button.pack()

#print("debug")

root.mainloop()