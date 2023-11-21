from helpers.helpers import Helpers

import pandas as pd
from minio import Minio
from io import BytesIO


class Loader():
    def __init__(self, endpoint, access_key, secret_key) -> None:
        self._helper = Helpers()
        print("Starting loader\n")

        self.minioClient = Minio(
            endpoint, access_key=access_key, secret_key=secret_key, secure=False
        )