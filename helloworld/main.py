# Copyright 2020 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

from colors import green

from helloworld.greet.greeting import Greeter
from helloworld.util.config_loader import Config


def say_hello(config: Config) -> None:
    greeter = Greeter(languages=config.languages, greetings=config.greetings)
    sentence = greeter.greet("world")
    print(green(sentence))


if __name__ == "__main__":
    config = Config.load_from_json("helloworld", "config.json")
    say_hello(config)
