import yaml


class Helpers:
    def __init__(self) -> None:
        pass

    def get_config(self) -> dict:
        with open("src/helpers/config.yml", "r") as file:
            config_file = file.read()
        self.config_dict = yaml.safe_load(config_file)
        return self.config_dict

    def get_source(self, service_config: dict, source_name: str) -> dict:
        return service_config.get("sources", {}).get(source_name)

    def get_source_endpoint(
        self, service_config: dict, source_name: str, endpoint_name: str
    ) -> dict:
        return (
            service_config.get("sources", {})
            .get(source_name, {})
            .get("endpoints", {})
            .get(endpoint_name)
        )

    def get_parser(self, parser_config: dict, parser_name: str) -> dict:
        return parser_config.get("parser", {}).get(parser_name, {})

    def get_parser_endpoint(
        self, parser_config: dict, parser_name: str, endpoint_name: str
    ) -> dict:
        return (
            parser_config.get("parser", {})
            .get(parser_name, {})
            .get("endpoints", {})
            .get(endpoint_name)
        )

    def get_introspection(self, json: dict or list, introspection: dict) -> any:
        if not json:
            return None

        if introspection.get("introspection"):
            return self.get_introspection(
                json=json[introspection["value"]],
                introspection=introspection["introspection"],
            )

        else:
            return json[introspection["value"]]

    def is_paginated(
        self, parser_name: str, endpoint_name: str
    ) -> bool:
        
        print(self.config_dict.get("parser", {})
            .get(parser_name, {})
            .get("endpoints", {})
            .get(endpoint_name, {})
            .get("pagination",{})
            .get("enabled"))

        return (
            self.config_dict.get("parser", {})
            .get(parser_name, {})
            .get("endpoints", {})
            .get(endpoint_name, {})
            .get("pagination",{})
            .get("enabled")
        )

    def get_dependencies(self, source_name) -> any:
        endpoint_list = self.config_dict["sources"].get(source_name, {}).get("endpoints")
        dependencies_dict = {}

        for key, value in endpoint_list.items():
            dependencies_dict[key] = value.get("dependencies", {})

        return dependencies_dict
