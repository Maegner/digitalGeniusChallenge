import src.domain
from src.domain import model

def test_constructor():
    response = "{}"
    id = "26444047-56f8-43e5-8e25-b70b8e5367f1"
    testSubject = model.Model(id,response)
    assert testSubject.get_id() == id
    assert testSubject.get_response("hello") == "hello"

def test_empty_name_in_response():
    response = "{}"
    id = "26444047-56f8-43e5-8e25-b70b8e5367f1"
    testSubject = model.Model(id,response)
    assert testSubject.get_id() == id
    assert testSubject.get_response("") == ""