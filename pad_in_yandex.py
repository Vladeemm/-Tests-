import time
import logging
import requests
import os

from dotenv import load_dotenv


def status_code(code, file_name):
    """Обрабатывает код статуса полученный от API"""

    if code == 201:
        logging.info(f"Создание папки -- {file_name} -- на Я.Диске")
        time.sleep(2)
        logging.info(f"Папка -- {file_name} -- создана")
    elif code == 409:
        logging.info(f"Папка -- {file_name} -- на Я.Диске уже существует")
        time.sleep(2)


def creating_folder():
    """Создает папку на яндекс диске и возвращает код статуса"""

    logging.basicConfig(level=logging.INFO, format='%(message)s')

    try:
        load_dotenv()
        yd_token = os.getenv('YD_TOKEN')
    except Exception as e:
        print(f"Ошибка при загрузке: {e}")
        yd_token = None

    file_name = input("Ведите название папки: ")
    yd_base = 'https://cloud-api.yandex.net'
    params = {
        'path': file_name
    }
    headers = {
        'Authorization': f'OAuth {yd_token}'
    }

    response = requests.put(f"{yd_base}/v1/disk/resources",
                            headers=headers,
                            params=params)
    status_code(response.status_code, file_name)
    return response.status_code




if __name__ == "__main__":
    result = creating_folder()
    if result:
        print("\nОперация завершена успешно")
    else:
        print("\nОперация завершилась неудачно")
