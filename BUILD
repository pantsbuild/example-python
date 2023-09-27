# Copyright 2020 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

# A macro that turns every entry in this directory's requirements.txt into a
# `python_requirement_library` target. Refer to
# https://www.pantsbuild.org/docs/python-third-party-dependencies.
python_requirements(name="reqs", resolve=parametrize("python-default", "service-main2"))

python_requirement(
    name="colors-1.1.8",
    requirements=["ansicolors==1.1.8"],
    resolve="python-default"
)

python_requirement(
    name="colors-1.1.6",
    requirements=["ansicolors==1.1.6"],
    resolve="service-main2"
)