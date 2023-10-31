from flask import Flask, request

app = Flask(__name__)

@app.route("/hello", methods=["GET", "POST"])
def hello():
    if request.method == "GET":
        return {
            "Message": "Hello world!"
        }
    elif request.method == "POST":
        data = request.json
        for key, value in data.items():
            print(f"{key}: {value}")
        return "Confirmation"

app.run()

