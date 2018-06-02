import src.domain
from src.domain import model_manager,model

def test_constructor_empty():
    manager = model_manager.Model_Manager()
    assert manager.get_model("id") == None

def test_constructor_not_empty():
    mod = model.Model("id","response: {}")
    models = {mod.get_id(): mod}
    manager = model_manager.Model_Manager(models)
    
    result = manager.get_model(mod.get_id())
    assert result.get_id() == mod.get_id()

def test_add_model():
    mod = model.Model("id","response: {}")
    manager = model_manager.Model_Manager()
    manager.add_model(mod)

    result = manager.get_model(mod.get_id())
    assert result.get_id() == mod.get_id()