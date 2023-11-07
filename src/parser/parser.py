from helpers.helpers import Helpers

import pandas as pd


class Parser:
    def __init__(self, config_file: dict) -> None:
        self._helpers = Helpers()
        self._parser_config = config_file

    def _parse_response(self, json: dict) -> any:
        parse_config = self._helpers.get_parser(
            parser_config=self._parser_config, parser_name="pokeapi"
        )

        # print(parse_config)

        if parse_config["type"] == "api":
            endpoint_config = self._helpers.get_parser_endpoint(
                parser_config=self._parser_config,
                parser_name="pokeapi",
                endpoint_name="pokemon",
            )
            parsed_response = self._helpers.get_introspection(
                json=json, introspection=endpoint_config["introspection"]
            )

            # print(parsed_response)

            if parsed_response != []:
                df = pd.DataFrame(parsed_response)

                return df
            
            return None
