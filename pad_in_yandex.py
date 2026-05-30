import time
import logging
import requests
import os

from dotenv import load_dotenv


def status_code(code, file_name):
    """Обрабатывает код статуса полученный от API"""

    if code == 200:
        print(f"Подтверждаю наличие папки -- {file_name} -- на Я.Диске")
        time.sleep(2)
    elif code == 201:
        print(f"Создание папки -- {file_name} -- на Я.Диске")
        time.sleep(2)
        print(f"Папка -- {file_name} -- создана")
        time.sleep(2)
    elif code == 404:
        print(f"Папка -- {file_name} -- на Я.Диске не создана")
        time.sleep(2)
    elif code == 409:
        print(f"Папка -- {file_name} -- на Я.Диске уже существует")
        time.sleep(2)


def creating_folder(yd_token):
    """Создает папку на яндекс диске и возвращает код статуса"""

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


def checking_folder(yd_token):
    """Проверяет наличие папки на яндекс диске и возвращает код статуса"""

    file_name = input("Ведите название папки: ")
    yd_base = 'https://cloud-api.yandex.net'
    params = {
        'path': file_name
    }
    headers = {
        'Authorization': f'OAuth {yd_token}'
    }
    response = requests.get(f"{yd_base}/v1/disk/resources",
                            headers=headers,
                            params=params)
    status_code(response.status_code, file_name)
    return response.status_code


def folder_creation_manager_on_YD():
    """
    cr - "creating a folder" -- Команда создания папки на Яндекс Диске
    ch - "checking for a folder" -- Команда проверки наличия папки на Яндекс Диске
    e - "exit" -- Команда выхода из менеджера
    """
    print("Добро пожаловать в менеджер папок Яндекс Диска.\n"
          "Введите help, для просмотра списка поддерживаемых команд)\n")

    try:
        load_dotenv()
        yd_token = os.getenv('YD_TOKEN')
    except Exception as e:
        print(f"Ошибка при загрузке: {e}")
        yd_token = None

    while True:
        command = input("Введите команду: ")
        if command == "cr":
            result = creating_folder(yd_token)
            if result:
                print("Операция завершена")
            else:
                print("Операция завершилась неудачно")
        elif command == "ch":
            checking_folder(yd_token)
        elif command == "help":
            print(folder_creation_manager_on_YD.__doc__)
        elif command == 'exit':
            break



if __name__ == "__main__":
    folder_creation_manager_on_YD()
