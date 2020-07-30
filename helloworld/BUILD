# Copyright 2020 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

python_binary(
    # name defaults to the name of this directory, i.e., `helloworld`.
    sources = ["main.py"],
    entry_point = "helloworld.main",
    dependencies = [
        ":config",
        "//:ansicolors",
        "helloworld/greet",
    ],
)

# Note: Has sdist dependencies, so must be built on Linux.
python_awslambda(
    name='helloworld-awslambda',
    sources = ["awslambda.py"],
    dependencies=[
        ":config",
        "helloworld/greet",
    ],
    handler='helloworld.awslambda:handler',
    runtime='python3.7',
)

python_binary(
    name = "helloworld_py2",
    sources = ["main_py2.py"],
    entry_point = "helloworld.main_py2",
    compatibility = ">=2.7,<3",
    dependencies = [
        "//:ansicolors",
        "helloworld/greet_py2",
    ],
)

python_library(
    name = "config",
    sources = ["config.py"],
    dependencies = [
        ":config_file",
        "helloworld/util",
        "helloworld/util/proto",
    ],
)

resources(
    name = "config_file",
    sources = ["config.json"],
)
