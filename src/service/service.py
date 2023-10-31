import requests

from helpers.helpers import Helpers

class Service():
    def __init__(self, config_file: dict) -> None:
        self._helper = Helpers()
        self.service_config = config_file

    def _request(self, source_name, endpoint_name) -> any:
        # Seria interessante deixar essas atribuições aqui nessa função, pensando em requests em múltiplas sources e múltiplos endpoints ou jogar tudo isso para o init?
        source_config = self._helper.get_source(service_config=self.service_config, source_name=source_name)
        endpoint_config = self._helper.get_endpoint(service_config=self.service_config, source_name=source_name, endpoint_name=endpoint_name)
        url_base = source_config["base_url"]
        endpoint = endpoint_config["path"]
        method = endpoint_config["method"]
        params = endpoint_config["params"]

        request = requests.request(url=f'{url_base}{endpoint}', method=method, params=params)

        # Como configurar a paginação com o auxílio do yml?

        # Como configurar a introspecção?

        # Como configurar dependências?

        # if request.status_code == 200:
        #     introspection = self._helper.get_introspection(json=request.json(), introspection=endpoint_config["introspection"])
        #     json_data = request.json()[introspection]


    def _get_next_page(self, params: dict, json: any) -> any:
        pass