# Copyright 2020 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

from helloworld.greet.greeting import Greeter


def test_greeter() -> None:
    greeter = Greeter(translations={"hello": {"es": "hola"}})
    assert greeter.greet("test") == "Hola, test!"
