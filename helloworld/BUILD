# Copyright 2020 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

# `name` defaults to the name of this directory, i.e., `helloworld`.
pex_binary(
    sources=["main.py"],
    entry_point="helloworld.main",
)

python_library(
  name="awslambda_lib",
  sources=["awslambda.py"],
)

# Note: This has sdist dependencies, so it must be built on Linux.
python_awslambda(
    name="helloworld-awslambda",
    dependencies=[":awslambda_lib"],
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
