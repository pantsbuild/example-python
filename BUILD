# Copyright 2020 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).


# A macro that turns every entry in this directory's requirements.txt into a target
# with the name of the corresponding dist.
#
# For example, `translate>=3.2.1` expands to:
#   python_requirement_library(
#     name='translate',
#     requirements=[
#       python_requirement('translate>=3.2.1')
#     ]
#   )

python_requirements()
