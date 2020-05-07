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
        "helloworld/util",
    ]
)

# Note: Has sdist dependencies, so must be built on Linux.
python_awslambda(
    name='helloworld-awslambda',
    sources = ["awslambda.py"],
    dependencies=[
        ":config",
        "helloworld/greet",
        "helloworld/util",
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
    ]
)

resources(
     name = 'config',
     sources = ['config.json'],
)
