from helpers.helpers import Helpers
from service.service import Service
from parser.parser import Parser

class Handler():
    def __init__(self) -> None:
        print("Process started!\n")
        self.helper = Helpers()

    def run(self) -> None:
        config_file = self.helper.get_config()

        service = Service(config_file)

        service._request(source_name="pokeapi", endpoint_name="pokemon")

        # print(config_file)

        # poke_source = self.helper._get_source(config_file, "pokeapi")

        # print(poke_source)

        # pokemon_endpoint = self.helper._get_endpoint(config_file, "pokeapi", "pokemon")

        # print(pokemon_endpoint)

