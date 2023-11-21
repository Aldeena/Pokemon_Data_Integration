from helpers.helpers import Helpers
from service.service import Service
from parser.parser import Parser
from loader.loader import Loader

import pandas as pd


class Handler:
    def __init__(self) -> None:
        print("Process started!\n")
        self._helper = Helpers()
        self._helper.del_last_execution_traces()
        config_file = self._helper.get_config()

        self._service = Service(config_file)
        self._parser = Parser(config_file)
        self._loader = Loader()

    def run(self) -> None:
        dependencies_list = self._helper.get_dependencies(source_name="pokeapi")
        self.dependency_attribute = []

        print(dependencies_list)

        request_count = 0

        while True:
            data = self._service._request(
                source_name="pokeapi",
                endpoint_name="pokemon",
                request_count=request_count,
            )

            parsed_response = self._parser._parse_response(json=data)

            if parsed_response is not None and self._helper.is_paginated(parser_name="pokeapi", endpoint_name="pokemon"):
                request_count += 1
            else:
                request_count = 0
                break

            for dictionary in dependencies_list:
                if "pokemon" in dictionary:
                    self._helper.save_dependency(endpoint="pokemon", dependency_list=parsed_response[dictionary["pokemon"]].tolist())


