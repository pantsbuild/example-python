# Copyright 2020 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

import colors
from colors import green

from helloworld.greet.greeting import Greeter


def say_hello() -> None:
    greeting = Greeter().greet("Pantsbuild")
    greeting = f"main2.py: {greeting} with colors.__version__ = {colors.__version__}"
    print(green(greeting))


if __name__ == "__main__":
    say_hello()
