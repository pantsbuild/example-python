# Copyright 2020 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

from helloworld.util.config import Config


def test_load_config_from_json() -> None:
    config = Config.load_from_json_resource(__name__, "config_test_data.json")
    assert config.languages == ["af", "zh"]
    assert config.greetings == ["hi", "hey"]