import requests
import random
import json

from pages.InAccount.img_pages.accsess_keys import accsess_key_bird

def get_bird(conn):
    accsess_key = accsess_key_bird
    url = f"https://api.unsplash.com/search/photos?query=birds&client_id={accsess_key}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        results = data["results"]
        random_photo = random.choice(results)
        image_url = random_photo["urls"]["small"]

        width = 400
        height = 300

        json_output_from_server = json.dumps({"url": image_url,
                                              "width": width,
                                              "height": height})
        conn.send(json_output_from_server.encode())
        # img = requests.get(image_url)

        print(f"Вот тебе птичка: {image_url}")

    else:
        result_str = f"Ошибка при запросе: {response.status_code}"
        print(result_str)
        conn.send(result_str.encode())