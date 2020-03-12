# Copyright 2020 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

import random

from util.lang import LanguageTranslator
from util.resources import get_lines


class Greeter:
    def __init__(self):
        self._greeting_selector = GreetingSelector()
        self._language_translator = LanguageTranslator()

    def translated_greeting(self) -> str:
        return self._language_translator.translate_to_random_language(
            self._greeting_selector.pick_greeting()
        )

    def greet(self, name: str) -> str:
        greeting = self.translated_greeting()
        return f"{greeting}, {name}!"


class GreetingSelector:
    def __init__(self):
        self._greetings = get_lines(__name__, "greetings.txt")

    def pick_greeting(self):
        return random.choice(self._greetings)
