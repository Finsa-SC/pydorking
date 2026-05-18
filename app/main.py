import argparse

from config import DorkingConfig, set_config

parser = argparse.ArgumentParser()

parser.add_argument("-d", "--domain", type=str, help="domains you want to dork")

args = parser.parse_args()

config = DorkingConfig(
    subdomain=args.domain
)

set_config(config)