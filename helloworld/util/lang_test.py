# Copyright 2020 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

import pytest

from helloworld.util.lang import LanguageTranslator


def test_language_translator():
    language_translator = LanguageTranslator()
    assert "hola" == language_translator.translate("es", "hello")


def test_unknown_language():
    with pytest.raises(LanguageTranslator.UnknownLanguage):
        LanguageTranslator().translate("xx", "hello")
