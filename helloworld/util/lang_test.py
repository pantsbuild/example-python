# Copyright 2020 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

import pytest

from helloworld.util.lang import LanguageTranslator


def test_language_translator() -> None:
    language_translator = LanguageTranslator(languages=["es"])
    assert "hola" == language_translator.translate("es", "hello")


def test_unknown_language() -> None:
    language_translator = LanguageTranslator(languages=[])
    with pytest.raises(LanguageTranslator.UnknownLanguage):
        language_translator.translate("xx", "hello")
