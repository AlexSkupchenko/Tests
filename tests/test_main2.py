import pytest
from main2 import yandex_request_put_folder, token, yandex_request_get_disk, folder, path_in_root, folder_of_putting

token_ya = token
headers = {'Content-Type': 'application/json',
           'Accept': 'application/json',
           'Authorization': f'OAuth {token}'
           }


class TestSomething:
    def setup(self):
        pass
        # print("method setup")

    def teardown(self):
        pass
        # print("method teardown")

    def test_yandex_request_get_disk_res200(self):
        assert yandex_request_get_disk(folder, token, headers) == 200

    def test_yandex_request_put_folder_res201(self):
        assert yandex_request_put_folder(path_in_root, folder_of_putting, headers) == 201

    def test_yandex_request_put_folder_res409(self):
        assert yandex_request_put_folder(path_in_root, folder_of_putting, headers) == 409
