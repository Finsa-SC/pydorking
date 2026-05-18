from dataclasses import dataclass

@dataclass(frozen=True)
class DorkingConfig:
    subdomain: str
    categories: str = None

_config = DorkingConfig()

def set_config(config: DorkingConfig):
    global _config
    _config = config

def get_config():
    return _config