import tkinter as tk
from tkinter import messagebox
import pyautogui
import threading
import time

# プログラムが実行中かどうかを追跡するフラグ
is_running = False

def start_clicking(x, y, interval):
    global is_running
    while is_running:
        pyautogui.click(x=x, y=y)
        time.sleep(interval)

def start():
    global is_running
    if not is_running:
        is_running = True
        x = int(x_entry.get())
        y = int(y_entry.get())
        interval = int(interval_entry.get())
        t = threading.Thread(target=start_clicking, args=(x, y, interval))
        t.start()
    else:
        messagebox.showinfo('Info', 'プログラムは既に実行中です。')

def stop():
    global is_running
    if is_running:
        is_running = False
    else:
        messagebox.showinfo('Info', 'プログラムは実行されていません。')

root = tk.Tk()
root.title("自動クリッカー")

# X座標の入力
x_label = tk.Label(root, text="X座標:")
x_label.pack()
x_entry = tk.Entry(root)
x_entry.pack()

# Y座標の入力
y_label = tk.Label(root, text="Y座標:")
y_label.pack()
y_entry = tk.Entry(root)
y_entry.pack()

# クリック間隔の入力
interval_label = tk.Label(root, text="クリック間隔（秒）:")
interval_label.pack()
interval_entry = tk.Entry(root)
interval_entry.pack()

# プログラム開始ボタン
start_button = tk.Button(root, text="開始", command=start)
start_button.pack()

# プログラム終了ボタン
stop_button = tk.Button(root, text="終了", command=stop)
stop_button.pack()

root.mainloop()
