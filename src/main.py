import sys
import os

from handler.handler import Handler

def main() -> None:
    handler = Handler()

    handler.run()


if __name__ == "__main__":
    main()