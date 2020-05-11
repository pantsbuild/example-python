# Copyright 2020 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

from helloworld.protos.config_pb2 import Config
from helloworld.util.config_loader import load_config_from_json


def load_config() -> Config:
    return load_config_from_json(__name__, "config.json")
