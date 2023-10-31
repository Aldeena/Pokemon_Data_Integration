import yaml

class Helpers:

    def __init__(self) -> None:
        pass

    def _get_config(self) -> dict:
        with open("src/helpers/config.yml", "r") as file:
            config_file = file.read()
        config_dict = yaml.safe_load(config_file)
        return config_dict

    def _get_source(self, service_config: dict, source_name: str) -> dict:
        return service_config.get("sources", {}).get(source_name)
    
    def _get_endpoint(self, service_config: dict, source_name: str, endpoint_name: str) -> dict:
        return service_config.get("sources",{}).get(source_name, {}).get("endpoints",{}).get(endpoint_name)