import pytest

from main import foo


@pytest.mark.parametrize("input_value, expected", [(2, 3), (100, 101)])
def test_foo(input_value, expected):
    assert foo(input_value == expected)
