from flask import Flask, request
from engine.engine import engine_of_program, get_part_family_tree
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def hello():
    return 'Hello, World!'

@app.route('/', methods=['POST'])
def generateFamilyTree():
    name = request.form['name']
    age = request.form['age']
    state = request.form['state']
    voter_id = request.form['voter_id']
    gender = request.form['gender']
    relation_name = request.form['relation_name']
    res = engine_of_program(name, age, state, voter_id, gender, relation_name)
    return res

@app.route('/getAllPartFamilies', methods=['POST'])
def generatePartFamilyTree():
    name = request.form['name']
    age = request.form['age']
    state = request.form['state']
    voter_id = request.form['voter_id']
    gender = request.form['gender']
    relation_name = request.form['relation_name']
    res = get_part_family_tree(name, age, state, voter_id, gender, relation_name)
    return res
    

if __name__ == '__main__':
    app.run()
