# Copyright 2020 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

# This target sets the metadata for all the Python non-test files in this directory.
python_sources(
    name="lib",
    resolve=parametrize("python-default", "service-main2")
)

# This target sets the metadata for all the Python test files in this directory.
python_tests(
    name="tests",
    resolve=parametrize("python-default", "service-main2")
)

# This target allows us to build a `.whl` bdist and a `.tar.gz` sdist by auto-generating
#  `setup.py`. See https://www.pantsbuild.org/docs/python-distributions.
#
# Because this target has no source code, Pants cannot infer dependencies. We depend on `:lib`,
#  which means we'll include all the non-test Python files in this directory, and any of
#  their dependencies.
python_distribution(
    name="dist",
    dependencies=[":lib@resolve=python-default"],
    wheel=True,
    sdist=True,
    provides=setup_py(
        name="helloworld.translator",
        version="0.0.1",
        description="A language translator.",
    )
)
