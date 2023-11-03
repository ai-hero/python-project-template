""" A simple hello world script. """


def greet(name: str) -> str:
    """Greet someone."""
    greeting = f"Hello {name}!"
    print(greeting)
    return greeting


if __name__ == "__main__":
    greet(name="World")
