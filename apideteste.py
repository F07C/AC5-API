from flask import Flask
import json
import requests


app = Flask(__name__)

@app.route('/api/ac5/v1/', methods=['GET'])
def home():
    api_url = "https://jsonplaceholder.typicode.com/todos/"
    response = requests.get (api_url)
    return response.json()

app.route('/api/ac5/v2/', methods = ['POST'])
def cadastro():
    api_url = "https://jsonplaceholder.typicode.com/todos/"
    envite = {"userId": 1, "title": "Buy milk", "completed": False}
    response = requests.post(api_url, json=envite)
    return response.json()

@app.route('/api/ac5/v3/', methods=["DELETE"])
def home():
    api_url = "https://jsonplaceholder.typicode.com/todos/1"
    response = requests.delete(api_url)
    return response.json()


if __name__ == '__main__':
    app.run()