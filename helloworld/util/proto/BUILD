# Copyright 2020 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

# This target sets the metadata for all the `.proto` files in this directory.
#  See https://www.pantsbuild.org/docs/protobuf.
#
# * `name` defaults to the name of this directory, i.e., `proto`.
# * `sources` defaults to ["*.proto"].
protobuf_library()

# Note that we have an empty `__init__.py` file in this folder. Pants will generate
# `helloworld/util/proto/config_pb2.py`, and we need an `__init__.py` file in the folder for that file to be properly
# recognized. Pants will automatically use this `__init__.py` file if it exists, even though we don't have a
# `python_library` target here.
