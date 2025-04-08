"""Unit testing my dictionary functions"""

__author__: str = "730655988"

from exercises.ex03.dictionary import invert, favorite_color, count, bin_len
import pytest


def test_invert_use_case_1():
    """Test invert with standard key-value pairs."""
    assert invert({"a": "z", "b": "y", "c": "x"}) == {"z": "a", "y": "b", "x": "c"}


def test_invert_use_case_2():
    """Test invert with a single key-value pair."""
    assert invert({"apple": "cat"}) == {"cat": "apple"}


def test_invert_edge_case():
    """Test invert with duplicate values causing KeyError."""
    with pytest.raises(KeyError):
        invert({"kris": "jordan", "michael": "jordan"})


def test_count_use_case_1():
    """Test count with multiple occurrences of words."""
    assert count(["apple", "banana", "apple", "orange", "banana", "banana"]) == {
        "apple": 2,
        "banana": 3,
        "orange": 1,
    }


def test_count_use_case_2():
    """Test count with unique words."""
    assert count(["dog", "cat", "mouse"]) == {"dog": 1, "cat": 1, "mouse": 1}


def test_count_edge_case():
    """Test count with an empty list."""
    assert count([]) == {}


def test_favorite_color_use_case_1():
    """Test favorite_color with a clear winner."""
    assert (
        favorite_color(
            {"Alice": "blue", "Bob": "green", "Charlie": "blue", "David": "red"}
        )
        == "blue"
    )


def test_favorite_color_use_case_2():
    """Test favorite_color with another clear winner."""
    assert (
        favorite_color(
            {"Eve": "yellow", "Frank": "yellow", "Grace": "purple", "Hank": "purple"}
        )
        == "yellow"
    )


def test_favorite_color_edge_case():
    """Test favorite_color with an empty dictionary."""
    assert favorite_color({}) == ""


def test_bin_len_use_case_1():
    """Test bin_len with standard input."""
    assert bin_len(["the", "quick", "fox"]) == {3: {"the", "fox"}, 5: {"quick"}}


def test_bin_len_use_case_2():
    """Test bin_len with duplicate words."""
    assert bin_len(["the", "the", "fox"]) == {3: {"the", "fox"}}


def test_bin_len_edge_case():
    """Test bin_len with an empty list."""
    assert bin_len([]) == {}


if __name__ == "__main__":
    pytest.main()
