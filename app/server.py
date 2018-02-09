from flask import Flask, request, json, jsonify
app = Flask(__name__)

@app.route("/")
def hello():
    return "Welcome to chart-app"

@app.route('/items')
def read_json():
    data_json = open('app/data.json')
    stored_json = json.load(data_json)
    print('*** read cart ***')
    return jsonify(stored_json)

@app.route('/add_item', methods=['POST'])
def add_json():
    data_json = open('app/data.json', mode='r')
    stored_json = json.load(data_json)
    data_json.close()
    new_data = request.json
    
    name_list = list(x["name"] for x in stored_json)
    if new_data["name"] not in name_list:
        stored_json.append(new_data)
    else:
        for i in stored_json:
            if new_data["name"] == i["name"]:
                i["qty"] += new_data["qty"]

    data_json = open('app/data.json', mode='w')
    json.dump(stored_json, data_json)
    data_json.close()
    print('*** insert *** %s' % new_data["name"])
    return 'successfuly inserted:\n\n' + str(new_data)

@app.route('/items/<name>', methods=['DELETE'])
def delete_item(name):
    data_json = open('app/data.json', mode='r')
    stored_json = json.load(data_json)
    data_json.close()
    
    name_list = list(x["name"] for x in stored_json)
    if str(name) not in name_list:
        return "The item is couldn't be deleted because not available."
    else:
        for i in stored_json:
            if str(name) == i["name"]:
                stored_json.remove(i)

    data_json = open('app/data.json', mode='w')
    json.dump(stored_json, data_json)
    data_json.close()
    print('*** delete *** %s' % (name))
    return 'successfuly deleted: ' + str(name)