import src.utils
from src.utils import name_parser
import pytest

def test_format_1():
    requestString = "Hi Seydou Abioye here,can you help me?"
    assert name_parser.get_names(requestString) == "Seydou Abioye"

def test_format_2():
    requestString = "Hello my name is Francisco, can you help me?"
    assert name_parser.get_names(requestString) == "Francisco"

def test_no_name():
    requestString = "Hello there, can you help me?"
    assert name_parser.get_names(requestString) == ""