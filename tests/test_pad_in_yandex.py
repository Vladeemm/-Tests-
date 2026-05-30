import os
from dotenv import load_dotenv
from pad_in_yandex import creating_folder, checking_folder


try:
    load_dotenv()
    yd_token = os.getenv('YD_TOKEN')
except Exception as e:
    print(f"Ошибка при загрузке: {e}")
    yd_token = None

def test_get_code_201(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '146')
    assert creating_folder(yd_token) == 201

def test_get_code_200(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '146')
    assert checking_folder(yd_token) == 200

def test_get_code_409(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '146')
    assert creating_folder(yd_token) == 409

