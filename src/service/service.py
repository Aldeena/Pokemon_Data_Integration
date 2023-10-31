import requests

from helpers.helpers import Helpers as helper

class Service():
    def __init__(self) -> None:
        pass

    def request(self, source_name, endpoint_name):
        source_config = helper._get_source(source_name=source_name)
        endpoint_config = helper._get_endpoint(source_name=source_name, endpoint_name=endpoint_name)
        url_base = source_config["base_url"]
        endpoint = endpoint_config["path"]
        method = endpoint_config["method"]
        params = endpoint_config["params"]

        request = requests.request(url=f'{url_base}{endpoint}', method=method, params=params)

        print(request.status_code)