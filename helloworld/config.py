# Copyright 2020 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

from helloworld.util.config_loader import load_config_from_json
from helloworld.util.proto.config_pb2 import Config


def load_config() -> Config:
    return load_config_from_json(__name__, "config.json")
