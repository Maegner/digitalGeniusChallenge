import pickle
from src.domain import model

class Model_Manager:
    current_models = {}
    
    def __init__(self,models={}):
        self.current_models = models

    def store(self):
        with open('model_manager','wb') as f:
            pickle.dump(self.current_models,f)
    
    def add_model(self,new_model):
        self.current_models[new_model.get_id()] = new_model
    
    def get_model(self,model_id):
        try:
            result = self.current_models[model_id]
        except KeyError:
            result = None
        return result

    def is_empty(self):
        return len(self.current_models) == 0
    
    def populate(self):
        
        id_1 = "26444047-56f8-43e5-8e25-b70b8e5367f1"
        response_1 = "Thanks for getting in touch {}! I will try my best to help."
        model_1 = model.Model(id_1,response_1)
        self.add_model(model_1)

        id_2 = "f59da1c7-c060-4aec-b3a0-dd7453a4c541"
        response_2 = "Hello {}! How can I help you?"
        model_2 = model.Model(id_2,response_2)
        self.add_model(model_2)

    
    def retrieve_data(self):
        try:
            with open('model_manager','rb') as f:
                self.current_models = pickle.load(f)
                return True
        except FileNotFoundError:
            return False