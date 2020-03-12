# Copyright 2020 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

python_library(
    dependencies = [
        "//:ansicolors",
        "helloworld/greet",
    ]
)

python_binary(
    name = "main",
    entry_point = "helloworld.main",
    dependencies = [
        ":helloworld",
    ]
)
