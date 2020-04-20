# Copyright 2020 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

from helloworld.greet.greeting import Greeter


def handler(event, context):
    print(Greeter().greet("world"))
