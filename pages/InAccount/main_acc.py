import tkinter as tk
from tkinter import ttk

from utilities.center_window import center_window
from pages.InAccount.img_pages.get_img_page import Image

def InAccount(name, root, login_name, client):
    login_in_window = tk.Toplevel(root)
    login_in_window.title(f"Добро пожаловать {name}")
    center_window(login_in_window, 350, 300)

    def Exit():
        login_in_window.destroy()

    button_width = 30
    button_pad_y = 10

    tk.Button(login_in_window,
              text="Показать собаку",
              width=button_width,
              command=lambda: Image(root, client, "DOG").pack(pady=button_pad_y)
              ).pack(pady=button_pad_y)

    tk.Button(login_in_window,
              text="Показать кота",
              width=button_width,
              command=lambda: Image(root, client, "CAT").pack(pady=button_pad_y)
              ).pack(pady=button_pad_y)

    tk.Button(login_in_window,
              text="Показать птицу",
              width=button_width,
              command=lambda: Image(root, client, "BIRD").pack(pady=button_pad_y)
              ).pack(pady=button_pad_y)

    tk.Button(login_in_window,
              text="Выйти",
              width=button_width,
              command=Exit
              ).pack(pady=(button_pad_y, 20))

