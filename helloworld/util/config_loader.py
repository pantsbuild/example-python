# Copyright 2020 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

import pkg_resources
from google.protobuf.json_format import Parse as parse_json

from helloworld.util.proto.config_pb2 import Config


def load_config_from_json(pkg_name: str, resource_name: str) -> Config:
    resource_content = pkg_resources.resource_string(pkg_name, resource_name).decode()
    return parse_json(resource_content, Config())
