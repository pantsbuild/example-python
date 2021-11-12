# Copyright 2020 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

# This target sets the metadata for all the Python non-test files in this directory.
#
# * Pants cannot infer dependencies on `resources` targets, so we explicitly add the dep.
python_library(
    name="lib",
    dependencies=[":translations"],
)

# This target sets the metadata for all the Python test files in this directory.
python_tests(
    name="tests",
)

# This target teaches Pants about our JSON file, which allows for other targets to depend on it.
resources(
    name="translations",
    sources=["translations.json"],
)
