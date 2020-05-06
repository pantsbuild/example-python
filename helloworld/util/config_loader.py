# Copyright 2020 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import List

import pkg_resources


@dataclass
class Config:
    languages: List[str]
    greetings: List[str]

    @classmethod
    def load_from_json(cls, pkg_name: str, resource_name: str) -> Config:
        resource_content = pkg_resources.resource_string(pkg_name, resource_name)
        parsed = json.loads(resource_content)
        return cls(languages=parsed["languages"], greetings=parsed["greetings"])
