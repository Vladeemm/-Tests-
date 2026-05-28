from unittest.mock import patch
from pad_in_yandex import creating_folder


def test_get_code_201():
    with patch('builtins.input', return_value='146'):
        assert creating_folder() == 201


def test_get_code_409():
    with patch('builtins.input', return_value='146'):
        assert creating_folder() == 409