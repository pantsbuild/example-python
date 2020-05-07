# Copyright 2020 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

from helloworld.greet.greeting import Greeter
from helloworld.util.config_loader import Config


def handler(event, context):
    config = Config.load_from_json("helloworld", "config.json")
    greeter = Greeter(languages=config.languages, greetings=config.greetings)
    print(greeter.greet("world"))
