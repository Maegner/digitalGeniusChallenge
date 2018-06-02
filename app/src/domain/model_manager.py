import pickle
from src.domain import model

class Model_Manager:
    current_models = {}
    
    def __init__(self,models={}):
        self.current_models = models

    def store(self):
        with open("model_manager",'wb') as f:
            pickle.dump(self.current_models,f)
    
    def add_model(self,new_model):
        self.current_models[new_model.get_id()] = new_model
    
    def get_model(self,model_id):
        try:
            result = self.current_models[model_id]
        except KeyError:
            result = None
        return result
