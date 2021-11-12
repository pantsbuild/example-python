# Copyright 2020 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

from __future__ import annotations

import random
from dataclasses import dataclass


class UnknownLanguage(Exception):
    pass


class UnknownPhrase(Exception):
    pass


@dataclass
class LanguageTranslator:
    """A mapping of phrases (in English) to ISO 639 language codes (like `es`,
    `fr`) and their translation.

    Assumes that every phrase is translated into the same languages.
    """

    phrases_to_translations: dict[str, dict[str, str]]

    @property
    def all_languages(self) -> set[str]:
        return {
            lang
            for translations in self.phrases_to_translations.values()
            for lang in translations.keys()
        }

    def translate(self, lang: str, phrase: str) -> str:
        if phrase not in self.phrases_to_translations:
            raise UnknownPhrase(phrase)
        translations = self.phrases_to_translations[phrase]
        if lang not in translations:
            raise UnknownLanguage(lang)
        return translations[lang]

    def translate_to_random_language(self, phrase: str) -> str:
        lang = random.choice(sorted(self.all_languages))
        return self.translate(lang, phrase)
