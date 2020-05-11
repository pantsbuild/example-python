# Copyright 2020 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

from helloworld.config import load_config
from helloworld.greet.greeting import Greeter


def handler(event, context):
    config = load_config()
    greeter = Greeter(languages=config.languages, greetings=config.greetings)
    print(greeter.greet("world"))
