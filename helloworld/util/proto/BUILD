# Copyright 2020 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

# `name` defaults to the name of this directory, i.e., `proto`.
# `sources` defaults to ["*.proto"].
protobuf_library(dependencies=[":init"])


# Note that we need an `__init__.py` file for MyPy to recognize our generated code as a valid
# module. We include this in the dependencies for the `protobuf_library` to ensure the
# `__init__.py` is always used.
#
# Often, you won't want to put `__init__.py` files in your Protobuf directories; see
# https://www.pantsbuild.org/docs/protobuf#protobuf-and-source-roots for how to change where the
# protobuf code is generated.
python_library(name="init")
