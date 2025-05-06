import requests
import json
import random
def get_dog(conn):
    url = "https://dog.ceo/api/breeds/image/random"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        image_url = data["message"]
        # img = requests.get(image_url)


        print(image_url)

        json_output_from_server = json.dumps({"url": image_url,
                                              "width": 720,
                                              "height": 480})
        conn.send(json_output_from_server.encode())
    else:
        result_str = f"Ошибка при запросе: {response.status_code}"
        print(result_str)
        conn.send(result_str.encode())