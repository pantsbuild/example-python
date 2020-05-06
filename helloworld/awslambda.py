# Copyright 2020 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

from helloworld.greet.greeting import Greeter
from helloworld.util.config_loader import load_config_from_json


def handler(event, context):
    config = load_config_from_json("helloworld", "config.json")
    greeter = Greeter(greetings=config.greetings, languages=config.languages)
    print(greeter.greet("world"))
