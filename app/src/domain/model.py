
class Model:
    model_id = ""
    model_response = ""

    def __init__(self,id,response):
        self.model_id = id
        self.model_response = response
    
    def get_id(self):
        return self.model_id

    def get_response(self,name):
        return self.model_response.format(name)