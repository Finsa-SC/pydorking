from app.utils.loader import dork_generator
from app.config import get_config

config = get_config()

class PyDorking:
    def __init__(self):
        self.subdomain: str = config.subdomain
        self.categories_input: str = config.categories
        self.categories: list[str] | None = None
        self.scan_result: dict = {}

    def execute(self):
        ...

    def executor(self):
        if self.categories_input:
            self.categories = self.categories_input.replace(" ", "").split(",")
        dork_stream = dork_generator(self.categories)

        for base_query in dork_stream:
            final_query = f"site:{self.subdomain} {base_query}"
