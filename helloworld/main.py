# Copyright 2020 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

from colors import green

from helloworld.greet.greeting import Greeter
from helloworld.util.config import Config


def say_hello() -> None:
    config = Config.load_from_json_resource(__name__, "config.json")
    greeter = Greeter(languages=config.languages, greetings=config.greetings)
    sentence = greeter.greet("world")
    print(green(sentence))


if __name__ == "__main__":
    say_hello()
