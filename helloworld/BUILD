# Copyright 2020 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

# `name` defaults to the name of this directory, i.e., `helloworld`.
pex_binary(
    entry_point="main.py",
)

# A library that owns all Python code in this directory, other that `config.py`: see below!
python_library(
    name="lib",
    sources=["*.py", "!config.py"],
)

# Note: This has sdist dependencies, so it must be built on Linux.
python_awslambda(
    name="helloworld-awslambda",
    dependencies=[":lib"],
    handler="helloworld.awslambda:handler",
    runtime="python3.7",
)

# Pants cannot infer dependencies on resources targets and Protobuf, so we explicitly add them.
python_library(
    name="config",
    sources=["config.py"],
    dependencies=[":config_file", "helloworld/util/proto"],
)

resources(
    name="config_file",
    sources=["config.json"],
)
