
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

countries = [
    {"id": 1, "name": "Thailand", "capital": "Bangkok", "area": 513120},
    {"id": 2, "name": "Australia", "capital": "Canberra", "area": 7617930},
    {"id": 3, "name": "Egypt", "capital": "Cairo", "area": 1010408},
]

def _find_next_id():
    return max(country["id"] for country in countries) + 1

@app.route("/countries",methods=['GET'])
def get_countries():
    return jsonify(countries)

@app.route("/countries",methods=['POST'])
def add_country():
    if request.is_json:
        country = request.get_json()
        country["id"] = _find_next_id()
        countries.append(country)
        return country, 201
    return {"error": "Request must be JSON"}, 415

@app.route("/countries/<int:id>", methods=['PUT'])
def update(id):
    if request.is_json:
        i=0
        for data in countries:
            if data['id'] == int(id):
                countries[i] = request.get_json()
            i+=1
        return jsonify(countries)
    return {"error": "Request must be JSON"}, 415

@app.route("/countries/<int:id>", methods=['GET'])
def get_id(id):
    for data in countries:
        if data['id'] == int(id):
            return jsonify(data)
    return{"error": "Id not founded"}, 404

@app.route("/countries/<int:id>", methods=['DELETE'])
def delete(id):

    for data in countries:
        if data['id'] == id:
            countries.remove(data)
            return jsonify({}), 204
    return {"error": "Id not founded"}, 404

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0", port=8090)