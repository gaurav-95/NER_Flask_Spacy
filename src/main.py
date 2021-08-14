from flask import Flask, Response, request
#from flask_restful import Resource, Api
import json
from NamedEntity import *

app = Flask(__name__)

@app.route("/health", methods=['GET'])
def get_status():
    return Response(json.dumps({"status":"UP"}), status=200, mimetype='application/json')

@app.route("/", methods=['GET'])
def get_help():
    return Response(json.dumps(
        {
         "text": "Anisha, who is the daughter of Ahmednagar Member of Parliament Dr Sujay Vikhe Patil and the grandaughter of veteran Maharashtra leader" 
	, 
    "To test sample text NER add to url": "/api/sample_entities"
	,
    "To do NER using POST request (text in body)": "/api/entities",
    "this uses" : "en_core_web_trf model"
    }
    ), status=200, mimetype='application/json')

@app.route("/api/entities", methods=["POST"])
def predict_entity():
    text = request.json["text"]
    entity_dict = NamedEntityService.get_entities(text)
    return Response(json.dumps(entity_dict), status=200, mimetype='application/json')

@app.route("/api/sample_entities", methods=["GET"])
def predict_entity_sm():
    """
            for h2load testing
                    """
    text = "Anisha, who is the daughter of Ahmednagar Member of Parliament Dr Sujay Vikhe Patil and the grandaughter of veteran Maharashtra leader Radhakrishna Vikhe Patil, apparently had been desperate to meet the PM Modi and had been asking her father to take her along. But Patil had to explain to her that what she was asking was a difficult task since the prime minister was a busy man and may not be able to give her an appointment."
    entity_dict = NamedEntityService.get_entities(text)
    return Response(json.dumps(entity_dict), status=200, mimetype='application/json')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port = 8080, debug=True, threaded=True)
