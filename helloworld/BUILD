# Copyright 2020 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).


python_binary(
    # name defaults to the name of this directory, i.e., `helloworld`.
    sources = ["main.py"],
    entry_point = "helloworld.main",
    dependencies = [
        "//:ansicolors",
        "helloworld/greet",
    ]
)


python_binary(
    name = "helloworld_py2",
    sources = ["main_py2.py"],
    entry_point = "helloworld.main_py2",
    compatibility = ">=2.7,<3",
    dependencies = [
        "//:ansicolors",
        "helloworld/greet_py2",
    ]
)
