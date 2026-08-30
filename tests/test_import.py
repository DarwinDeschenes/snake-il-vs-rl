import snake
import pytest
import importlib

def version():
    return importlib.metadata.version("snake-il-vs-rl")

def test_trivial():
    importlib.metadata.version("snake-il-vs-rl")
    assert version() == "0.1.0"
