import tkinter as tk
import json
from PIL import Image as PILImage, ImageTk
import requests

from utilities.center_window import center_window

def Image(root, client, animal):
    tests_in_window = tk.Toplevel(root)
    tests_in_window.title(animal)
    center_window(tests_in_window, 400, 400)

    json_output = json.dumps({
        "data": "",
        "action": animal
    })
    client.send(json_output.encode())

    response = json.loads(client.recv(8192).decode())
    url = response["url"]
    width = response["width"]
    height = response["height"]

    try:
        center_window(tests_in_window, width, height)
        img_response = requests.get(url, stream=True)
        img_response.raise_for_status()
        pil_image = PILImage.open(img_response.raw)
        # pil_image = pil_image.resize((width, height))
        photo = ImageTk.PhotoImage(pil_image)

        label = tk.Label(tests_in_window, image=photo)
        label.image = photo
        label.pack(pady=10)

    except Exception as e:
        tk.Label(tests_in_window, text=f"Ошибка загрузки изображения: {e}").pack(pady=10)