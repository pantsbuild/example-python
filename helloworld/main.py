# Copyright 2020 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

from colors import green

from helloworld.greet.greeting import Greeter


def say_hello():
    greeter = Greeter()
    sentence = greeter.greet("world")
    print(green(sentence))


if __name__ == "__main__":
    say_hello()
