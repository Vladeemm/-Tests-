import os
import responses
import unittest
from unittest import mock
from dotenv import load_dotenv
from pad_in_yandex import checking_folder, creating_folder

load_dotenv()
yd_token = os.getenv('YD_TOKEN')

class TestWithResponses(unittest.TestCase):
    @responses.activate
    def test_checking_folder_response_200(self):
        with mock.patch('builtins.input', return_value='146'):
            responses.add(
                responses.GET,
                'https://cloud-api.yandex.net/v1/disk/resources',
                status=200,
            )
            result = checking_folder(yd_token)
        self.assertEqual(result, 200)

    @responses.activate
    def test_creating_folder_response_201(self):
        with mock.patch('builtins.input', return_value='146'):
            responses.add(
                responses.PUT,
                'https://cloud-api.yandex.net/v1/disk/resources',
                status=201,
            )
            result = creating_folder(yd_token)
        self.assertEqual(result, 201)

    @responses.activate
    def test_checking_folder_response_404(self):
        with mock.patch('builtins.input', return_value='146'):
            responses.add(
                responses.GET,
                'https://cloud-api.yandex.net/v1/disk/resources',
                status=404,
            )
            result = checking_folder(yd_token)
        self.assertEqual(result, 404)

    @responses.activate
    def test_creating_folder_response_409(self):
        with mock.patch('builtins.input', return_value='146'):
            responses.add(
                responses.PUT,
                'https://cloud-api.yandex.net/v1/disk/resources',
                status=409,
            )
            result = creating_folder(yd_token)
        self.assertEqual(result, 409)