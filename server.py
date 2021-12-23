from flask import Flask, url_for, request, redirect, abort, jsonify
from carsDAO import carsDAO

app = Flask(__name__, static_url_path='', static_folder='staticpages')



@app.route('/')
def index():
    return "hello"
#get all
@app.route('/cars')
def getAll():
    return jsonify(carsDAO.getAll())
# find By id
@app.route('/cars/<int:plate>')
def findById(plate):
    return jsonify(carsDAO.findByID(plate))

# create
# curl -X POST -d "{\"plate\":\"123\", \"model\":\"Ford\", \"year\":123, \"fuel\":\"test\"}" -H Content-Type:application/json http://127.0.0.1:5000/cars
@app.route('/cars', methods=['POST'])
def create():
    
    if not request.json:
        abort(400)
    
    car = {
        "plate": request.json["plate"],
        "model": request.json["model"],
        "year": request.json["year"],
        "fuel": request.json["fuel"]
    }
    
    return jsonify(carsDAO.create(car))


    return "served by Create "

#update
# curl -X PUT -d "{\"model\":\"new model\", \"fuel\":"Petrol"}" -H "content-type:application/json" http://127.0.0.1:5000/cars/1
@app.route('/cars/<int:plate>', methods=['PUT'])
def update(plate):
    foundcars = carsDAO.findByID(plate)
    print(foundcars)
    if len(foundcars) == {}:
        return jsonify({}), 404
    currentCar = foundcars[0]
    if 'model' in request.json:
        currentCar['model'] = request.json['model']
    if 'year' in request.json:
        currentCar['year'] = request.json['year']
    if 'fuel' in request.json:
        currentCar['fuel'] = request.json['fuel']
    carsDAO.update(currentCar)
    return jsonify(currentCar)

#delete
# curl -X DELETE http://127.0.0.1:5000/books/1
@app.route('/cars/<int:plate>', methods=['DELETE'])
def delete(plate):
    carsDAO.delete(plate)
    return jsonify({"done":True})


if __name__ == "__main__":
    app.run(debug=True)