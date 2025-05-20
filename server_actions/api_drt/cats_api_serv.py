import random
import requests
import json

from server_actions.api_drt.accsess_keys import accsess_key_cat

def get_cat(conn):
    accsess_key = accsess_key_cat
    url = f"https://pixabay.com/api/?key={accsess_key}&q=cats&image_type=photo"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        # image_url = random.choice(data["hits"][0]["webformatURL"])
        # width = data["hits"][0]["webformatWidth"]
        # height = data["hits"][0]["webformatHeight"]
        random_hit = random.choice(data["hits"])
        image_url = random_hit["webformatURL"]
        width = random_hit["webformatWidth"]
        height = random_hit["webformatHeight"]
        # img = requests.get(image_url)
        json_output_from_server = json.dumps({"url": image_url,
                                              "width": width,
                                              "height": height})
        conn.send(json_output_from_server.encode())
        print(f"Вот тебе котик: {image_url}")
    else:
        result_str = f"Ошибка при запросе: {response.status_code}"
        print(result_str)
        conn.send(result_str.encode())