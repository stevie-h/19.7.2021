
import json
from flask import Flask, request

app = Flask(__name__)


class Food:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return f'id: {self.id} name: {self.name}'


food_list = [Food(1, "food1"), Food(2, "food2"), Food(3, "food3")]


# get all food in list, post to list
@app.route('/food/', methods=['GET', 'POST'])
def get_tasks():

    if request.method == 'GET':
        json_list = []
        for e in food_list:
            json_list.append(json.dumps(e.__dict__))
        return json.dumps(json_list)

    if request.method == 'POST':
        print(request.json)
        obj = request.json
        e = Food(obj['id'], obj['name'])
        food_list.append(e)

    return 'OK', 201


# get food by id, delete and update (by id)
@app.route('/food/<int:id>', methods=['GET', 'DELETE', 'PUT'])
def get_tasks_by_id(id):

    if request.method == 'GET':
        for e in food_list:
            if e.id == id:
                return json.dumps(e.__dict__)

    if request.method == 'DELETE':
        for e in food_list:
            if e.id == id:
                food_list.remove(e)
                return 'success'

    if request.method == 'PUT':
        for e in food_list:
            if e.id == id:
                food_list.remove(e)
                obj = request.json
                e = Food(obj['id'], obj['name'])
                food_list.append(e)
                return 'success'


app.run()

