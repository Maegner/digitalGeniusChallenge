from src.domain import model_manager
from src.utils import name_parser
from flask import Flask,abort,request,jsonify

manager = model_manager.Model_Manager()
app = Flask(__name__)

@app.route('/help',methods=['POST'])
def help_request():
    
    help = request.get_json()
    try:
        help_id = help["id"]
        help_request = help["request"]
        
        name = name_parser.get_names(help_request)
        help_model = manager.get_model(help_id)
        
        if help_model == None:
            abort(404)

        response = {"response":help_model.get_response(name)}

        return jsonify(response)
    except KeyError:
        abort(400)

def settup(debug=True):
    
    global manager
    manager
    manager.retrieve_data()

    if manager.is_empty():
        manager.populate()
        manager.store()

    app.run(debug=debug,host='0.0.0.0',port=5000)

if __name__ == '__main__':
    settup()