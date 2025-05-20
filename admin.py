import json
import socket
import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox
from utilities.center_window import center_window

IP = '127.0.0.1'
PORT = 4000
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((IP, PORT))
client.settimeout(3)

root = tk.Tk()
root.title("Admin-panel")
center_window(root, 500, 550)


text_response = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=25)
text_response.pack(pady=10, padx=10)
text_response.config(state=tk.DISABLED)


def admin():
    json_output = json.dumps({"data": '', "action": "ADMIN"})
    client.send(json_output.encode())
    response = client.recv(8192).decode()

    text_response.config(state=tk.NORMAL)
    text_response.delete(1.0, tk.END)
    text_response.insert(tk.END, response)
    text_response.config(state=tk.DISABLED)

def exit_app():
    json_output = json.dumps({"data": "", "action": "BYE"})
    client.send(json_output.encode())
    client.close()
    root.destroy()

tk.Button(root, text="Смотреть логи", command = admin).pack(pady=5)
tk.Button(root, text="Выход", command=exit_app).pack(pady=5)

root.mainloop()
