# Copyright 2020 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

pex_binary(
    # name defaults to the name of this directory, i.e., `helloworld`.
    sources=["main.py"],
    entry_point="helloworld.main",
)

# Note: Has sdist dependencies, so must be built on Linux.
python_awslambda(
    name="helloworld-awslambda",
    sources=["awslambda.py"],
    handler="helloworld.awslambda:handler",
    runtime="python3.7",
)

pex_binary(
    name="helloworld_py2",
    sources=["main_py2.py"],
    entry_point="helloworld.main_py2",
    compatibility=">=2.7,<3",
)

python_library(
    name="config",
    sources=["config.py"],
    dependencies=[
        # Pants cannot infer dependencies on resources targets and Protobuf, so we explicitly
        # add them.
        ":config_file",
        "helloworld/util/proto",
    ],
)

resources(
    name="config_file",
    sources=["config.json"],
)
