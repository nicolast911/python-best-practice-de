from recipes import One, Many
import pytest

@pytest.fixture
def one1():
    return One(
        "My Recipe",
        ["ingredient 1", "my ingredient 2"],
        "Instructions\n...",
        4
    )

@pytest.fixture
def one2():
    return One(
        "Your Recipe",
        ["ingredient 1", "your ingredient 2"],
        "Instructions\n...",
        5
    )

@pytest.fixture
def many(one1, one2):
    return Many(
        [one1, one2],
    )

def test_many_get_thing(one1, one2, many):
    assert many.get_thing("My Recipe") == one1
    assert many.get_thing("Your Recipe") == one2

    with pytest.raises(KeyError):
        many.get_thing("nonexistent")

def test_many_get_things_1(one1, one2, many):
    assert many.get_things_1("ingredient 1") == [one1, one2]
    assert many.get_things_1("my ingredient 2") == [one1]
    assert many.get_things_1("nonexistent") == []

def test_many_get_things_2(one1, one2, many):
    assert many.get_things_2(4) == [one1]
    assert many.get_things_2(5) == [one2]
    assert many.get_things_2(3) == []

def test_many_get_things_3(one1, one2, many):
    assert many.get_things_3(3) == [one1, one2]
    assert many.get_things_3(4) == [one1, one2]
    assert many.get_things_3(5) == [one2]
    assert many.get_things_3(6) == []