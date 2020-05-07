# Copyright 2020 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

import random
from typing import List

from helloworld.util.lang import LanguageTranslator


class Greeter:
    def __init__(self, greetings: List[str], languages: List[str]) -> None:
        self._greetings = greetings
        self._language_translator = LanguageTranslator(languages=languages)

    def translated_greeting(self) -> str:
        random_greeting = random.choice(self._greetings)
        return self._language_translator.translate_to_random_language(random_greeting)

    def greet(self, name: str) -> str:
        greeting = self.translated_greeting()
        return f"{greeting}, {name}!".capitalize()
