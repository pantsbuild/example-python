# Copyright 2020 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

from colors import green

from helloworld.config import load_config
from helloworld.greet.greeting import Greeter


def say_hello() -> None:
    config = load_config()
    greeter = Greeter(languages=config.languages, greetings=config.greetings)
    sentence = greeter.greet("world")
    print(green(sentence))


if __name__ == "__main__":
    say_hello()
