import pytest

from src.utils.treeview import JSONTreeView


def example_data():
    simple_1 = dict(a=1, b=2)
    simple_2 = dict(b=1, c=2)
    complex_1 = dict(aa=simple_1, bb=simple_2)
    complex_2 = dict(ab=simple_1, ba=simple_2)
    yield [simple_1, simple_1]
    yield [dict(a=simple_1, b=simple_2)]
    yield [complex_1, complex_1, complex_2]


@pytest.mark.parametrize("d", example_data())
def test_simple(d, file_regression):
    t = JSONTreeView()
    out = t.show(d)
    file_regression.check(out)
