import pytest

from src.utils.string_func import string_to_ascii


def strings():
    """Erstellt Testcases für die String-Manip Funktionen,
        NFKD Version ist immer an erster Stelle der Liste"""
    yield "Lukas Erhard", ["Lukas Erhard"]
    yield "Müller", ["Muller", "Mueller"]
    yield "Jérôme", ["Jerome"]
    yield "Eva Hummers-Pradier", ["Eva Hummers-Pradier", "Eva HummersPradier", "Eva Hummers- Pradier"]
    yield "müller, L", ["muller, L", "mueller, L"]
    yield "ellenbürger", ["ellenburger", "ellenbuerger"]
    yield "ellenbürger", ["ellenburger", "ellenbuerger"]
    yield "", [""]
    yield "straße", ["strae", "strasse"]
    yield "meier-landrut", ["meier-landrut", "meierlandrut", "meier- landrut"]
    yield "A' Chung", ["A Chung"]


@pytest.mark.parametrize("name_tuple", strings())
def test_string_to_ascii(name_tuple):
    question, answer = name_tuple[0], name_tuple[1].pop(0)
    assert string_to_ascii(question) == answer


def test_string_to_ascii_none():
    with pytest.raises(TypeError):
        string_to_ascii(None)
