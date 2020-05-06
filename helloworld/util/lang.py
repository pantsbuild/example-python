# Copyright 2020 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

import random

from translate import Translator

from helloworld.util.resources import get_lines


class LanguageTranslator:
    class UnknownLanguage(Exception):
        pass

    def __init__(self):
        self._langs = get_lines(__name__, "langs.txt")

    def translate(self, lang: str, phrase: str) -> str:
        if lang not in self._langs:
            raise self.UnknownLanguage(lang)
        translator = Translator(lang)
        return translator.translate(phrase)

    def translate_to_random_language(self, phrase: str) -> str:
        return self.translate(self._pick_random_language(), phrase)

    def _pick_random_language(self):
        return random.choice(self._langs)
