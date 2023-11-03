"""Test hello_world module."""
from app.hello_world import greet


def test_greet() -> None:
    """Test greet() function."""
    assert greet(name="World") == "Hello World!"
