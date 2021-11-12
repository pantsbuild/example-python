# Copyright 2020 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

import pytest

from helloworld.translator.translator import (
    LanguageTranslator,
    UnknownLanguage,
    UnknownPhrase,
)


def test_language_translator() -> None:
    translator = LanguageTranslator(
        {
            "hello": {"es": "hola", "ar": "مرحبًا"},
            "computer": {"es": "computadora", "ar": "حاسوب"},
        }
    )
    assert translator.translate("es", "hello") == "hola"
    assert translator.translate("ar", "hello") == "مرحبًا"
    assert translator.translate("es", "computer") == "computadora"


def test_unknown_phrase() -> None:
    translator = LanguageTranslator({"hello": {"es": "hola"}})
    with pytest.raises(UnknownPhrase):
        translator.translate("es", "good morning")


def test_unknown_language() -> None:
    translator = LanguageTranslator({"hello": {"es": "hola"}})
    with pytest.raises(UnknownLanguage):
        translator.translate("ch", "hello")
