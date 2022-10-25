# Copyright 2020 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

# A macro that turns every entry in this directory's requirements.txt into a
# `python_requirement_library` target. Refer to
# https://www.pantsbuild.org/docs/python-third-party-dependencies.
python_requirements(name="reqs")

python_distribution(
    name="my-wheel",
    dependencies=["helloworld:lib"],
    wheel=True,
    sdist=False,
    provides=setup_py(
        name="helloworld",
        version="0.0.1",
        description="A language translator.",
    ),
)
