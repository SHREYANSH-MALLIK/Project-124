from flask import Flask,jsonify, request

app = Flask(__name__)

contacts = [
    {
        'id' : 1,
        'name' : "Raju",
        'contact' : "9987644456",
        'done' : False
    },{
        'id' : 2,
        'name' : "Raju",
        'contact' : "9987644456",
        'done' : False
    }
]

@app.route("/")
def hello_world():
    return "Hello World!"

@app.route("/add-data", methods=["POST"])
def add_contact():
    if not request.json:
        return jsonify({
            "status":"error",
            "message": "Please provide the data!"
        },400)

    contact = {
        'id': contacts[-1]['id'] + 1,
        'name': request.json['title'],
        'contact': request.json.get('description', ""),
        'done': False
    }
    contacts.append(contact)
    return jsonify({
        "status":"success",
        "message": "Contact added succesfully!"
    })
    

@app.route("/get-data")
def get_task():
    return jsonify({
        "data" : contacts
    }) 

if (__name__ == "__main__"):
    app.run(debug=True)