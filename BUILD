# Copyright 2020 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).


# A macro that turns every entry in this directory's requirements.txt into a target
# with the name of the corresponding dist.
#
# For example, `translate>=3.2.1` expands to:
#
#   python_requirement_library(
#     name='translate',
#     requirements=['translate>=3.2.1']
#   )
#
# We set `module_mapping` for any requirements whose module names differ from the project's name so that dependency
# inference works.
#
# Refer to https://www.pantsbuild.org/docs/python-third-party-dependencies.
python_requirements(
  module_mapping={
    "ansicolors": ["colors"],
    "setuptools": ["pkg_resources"],
  },
)
