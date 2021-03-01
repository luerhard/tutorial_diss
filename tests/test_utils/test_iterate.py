from src.utils.iterate import chunks


def test_simple_chunks():
    result = list(chunks([1, 2, 3, 4, 5], chunksize=2))
    assert result == [[1, 2], [3, 4], [5]]
