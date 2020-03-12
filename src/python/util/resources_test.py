# Copyright 2020 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

from util.resources import get_lines


def test_get_lines():
    assert ["banana", "apple", "orange", "pear"] == get_lines(
        __name__, "resources_test.txt"
    )
