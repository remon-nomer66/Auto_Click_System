import tkinter as tk
from tkinter import messagebox
import pyautogui
import threading
import time
import pytesseract
from PIL import ImageGrab
import re

stop_flag = threading.Event()
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\clemo\OneDrive\デスクトップ\data\tesseract.exe'

def decision():
    input_seconds = entry.get()
    seconds = int(input_seconds)
    print(seconds)

def coord():
    input_x = entry_x.get()
    input_y = entry_y.get()
    x = int(input_x)
    y = int(input_y)
    print(x , y)

def coord_play():
    input_play_x = entry_play_x.get()
    input_play_y = entry_play_y.get()
    play_x = int(input_play_x)
    play_y = int(input_play_y)
    print(play_x , play_y)

def get_timer():
    x1 = int(timer_x1.get())
    y1 = int(timer_y1.get())
    x2 = int(timer_x2.get())
    y2 = int(timer_y2.get())
    print(x1, y1, x2, y2)


def start():
    def click_loop():
        while not stop_flag.is_set():
            play_x = int(entry_play_x.get())
            play_y = int(entry_play_y.get())
            click_x = int(entry_x.get())
            click_y = int(entry_y.get())
            seconds = int(entry.get())

            # Playボタンをクリック
            pyautogui.click(x=play_x, y=play_y)
            # 2秒間待つ
            time.sleep(2)
            # 画面キャプチャ
            img = ImageGrab.grab(bbox=(int(timer_x1.get()), int(timer_y1.get()), int(timer_x2.get()), int(timer_y2.get())))
            #imgを保存する
            img.save("img.png")
            pre_text = pytesseract.image_to_string(img)
            print(pre_text)
            pre_number = re.sub('\D', '', pre_text)
            print(pre_number)

            if len(pre_number) == 4:
                seconds = int(pre_number[:2]) * 60 + int(pre_number[2:])
            if len(pre_number) == 3:
                seconds = int(pre_number[:1]) * 60 + int(pre_number[1:])
            print(seconds)

            if len(pre_number) not in [3, 4]:
                seconds = 900
                print("OCRがうまくいかなかったので15分待ちます")
                print(seconds)

            # 指定時間待つ
            time.sleep(seconds)
            # 指定した座標をクリック
            pyautogui.click(x=click_x, y=click_y)
            # 10秒間待つ
            time.sleep(5)

    threading.Thread(target=click_loop).start()

def stop():
    stop_flag.set()

root = tk.Tk()
root.title("自動クリッカー")

# 秒数の入力
timer_label = tk.Label(root, text="クリック間隔(s)")
timer_label.grid(row=0, column=0)
entry = tk.Entry(root,fg="blue", bg="light gray", bd=5)
entry.insert(0, "900")
entry.grid(row=0, column=1)

# 秒数決定ボタン
decision_button = tk.Button(root, text="決定", command=decision)
decision_button.grid(row=0, column=2)

# 次の動画ラベル
next_label = tk.Label(root, text="次の動画座標")
next_label.grid(row=1, column=0)

# X座標の入力
entry_x = tk.Entry(root,fg="blue", bg="light gray", bd=5)
entry_x.insert(0, "1680")
entry_x.grid(row=2, column=0)

# Y座標の入力
entry_y = tk.Entry(root,fg="blue", bg="light gray", bd=5)
entry_y.insert(0, "950")
entry_y.grid(row=2, column=1)

# 座標決定ボタン
coord_button = tk.Button(root, text="座標決定", command=coord)
coord_button.grid(row=2, column=2)

# Playボタンラベル
play_label = tk.Label(root, text="Playボタン座標")
play_label.grid(row=3, column=0)

# X座標の入力_play
entry_play_x = tk.Entry(root,fg="blue", bg="light gray", bd=5)
entry_play_x.insert(0, "940")
entry_play_x.grid(row=4, column=0)

# Y座標の入力_play
entry_play_y = tk.Entry(root,fg="blue", bg="light gray", bd=5)
entry_play_y.insert(0, "660")
entry_play_y.grid(row=4, column=1)

# 座標決定ボタン_play
coord_button_play = tk.Button(root, text="PLAYボタン座標", command=coord_play)
coord_button_play.grid(row=4, column=2)

#スクリーンショットラベル
shot_label = tk.Label(root, text="スクリーンショット範囲")
shot_label.grid(row=5, column=0)

#スクリーンショットラベルx1y1
shot_label_x1y1 = tk.Label(root, text="x1,y1")
shot_label_x1y1.grid(row=6, column=0)

#スクリーンショットラベルx2y2
shot_label_x1y1 = tk.Label(root, text="x2,y2")
shot_label_x1y1.grid(row=7, column=0)

# スクリーンショット範囲
timer_x1 = tk.Entry(root,fg="blue", bg="light gray", bd=5)
timer_x1.insert(0, "1228")
timer_x1.grid(row=6, column=1)

timer_y1 = tk.Entry(root,fg="blue", bg="light gray", bd=5)
timer_y1.insert(0, "843")
timer_y1.grid(row=6, column=2)

timer_x2 = tk.Entry(root,fg="blue", bg="light gray", bd=5)
timer_x2.insert(0, "1276")
timer_x2.grid(row=7, column=1)

timer_y2 = tk.Entry(root,fg="blue", bg="light gray", bd=5)
timer_y2.insert(0, "865")
timer_y2.grid(row=7, column=2)

# スクリーンショット範囲ボタン決定
timer_button = tk.Button(root, text="スクリーンショット範囲", command=get_timer)
timer_button.grid(row=8, column=2)

#区切り
for i in range(3):
    kugiri_label = tk.Label(root, text="----------------------------------------")
    kugiri_label.grid(row=9, column=i)

# プログラム開始ボタン
start_button = tk.Button(root, text="開始", command=start)
start_button.grid(row=10, column=0)

# プログラム終了ボタン
stop_button = tk.Button(root, text="終了", command=stop)
stop_button.grid(row=10, column=1)

root.mainloop()