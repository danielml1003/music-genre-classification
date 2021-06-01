import tkinter as tk
from tkinter.filedialog import askopenfile
import socket
import wave
import numpy as np
import matplotlib.pyplot as plt
import os
import threading


IP = "127.0.0.1"
PORT = 10000
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((IP, PORT))
file_dir = []


def handler(sock_a):
    while True:
        data = sock_a.recv(1024)
        if data:
            return data


thread = threading.Thread(target=handler, args=(client_socket, ))
thread.daemon = True
thread.start()


root = tk.Tk()

# app size
canvas = tk.Canvas(root, width=600, height=300)
canvas.grid(columnspan=3, rowspan=3)

# instructions
instructions = tk.Label(root, text="Select a WAV file on your computer")
instructions.grid(columnspan=3, column=0, row=0)


def open_file():
    browse_text.set("loading...")
    file = askopenfile(parent=root, mode='rb', title="choose a file", filetype=[("WAV file", "*.wav")])
    if file:
        # wav = wave.open(file.name, "r")
        chunk = file.read(65536)
        client_socket.sendall(chunk)

        # print(wav.readframes(-1))
        browse_text.set("browse")
        page_content = os.path.basename(file.name)
        # text box
        text_box = tk.Text(root, height=10, width=50)
        text_box.insert(1.0, page_content)
        text_box.grid(column=2, row=1)


# browse button
browse_text = tk.StringVar()
browse_btn = tk.Button(root, textvariable=browse_text, command=lambda: open_file())
browse_text.set("Browse")
browse_btn.grid(column=0, row=1)

# send button
btn_text = tk.StringVar()
send_btn = tk.Button(root, textvariable=btn_text, command=lambda :send_file())
btn_text.set("...")
send_btn.grid(column=1, row=2)


def send_file():
    return "hello"


# answer from server text


def on_change_text():
    return "...."


text = on_change_text()
answer_text = tk.Text(root, height=5, width=35)
answer_text.insert(1.0, text)
answer_text.grid(column=1, row=4)

# redraw canvas
canvas = tk.Canvas(root, width=600, height=250)
canvas.grid(columnspan=3)

root.mainloop()

