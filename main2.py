import requests

path = 'disk:/nonsense'
token = "..."
headers = {'Content-Type': 'application/json',
           'Accept': 'application/json',
           'Authorization': f'OAuth {token}'
           }
folder = 'nonsense'


def yandex_request_get_disk(folder, token, header):
    url = 'https://cloud-api.yandex.net/v1/disk/resources'
    param = {'path': '/%s' % folder}
    response = requests.get(url, params=param, headers=header)
    res = [response.status_code][0]
    return res


path_in_root = 'nonsense'
folder_of_putting = 'xxx10'


def yandex_request_put_folder(path_in_root, folder_of_putting, headers):
    url = "https://cloud-api.yandex.net/v1/disk/resources"
    params = {'path': "%s/%s" % (path_in_root, folder_of_putting)}
    response = requests.put(url, params=params, headers=headers)
    res = [response.status_code][0]
    return res
