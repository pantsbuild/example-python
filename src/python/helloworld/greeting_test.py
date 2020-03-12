# Copyright 2020 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

from helloworld.greeting import Greeter


def test_greeter():
    greeter = Greeter()
    greeting = greeter.greet("world")
    assert greeting.endswith("world!")
