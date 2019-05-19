from flask import Flask, request, render_template, send_file
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config["MONGO_DBNAME"] = "FEI_DB"
app.config["MONGO_URI"] = "mongodb://127.0.0.1:27017/FEI_DB"
mongo = PyMongo(app)

@app.route('/insert')
def insert():
    contas = mongo.db.contas
    contas.insert({'teste' : 'teste'})
    return 'inserido'

@app.route('/show')
def show():
    contas = mongo.db.contas
    test = contas.find_one({'teste': 'teste'})
    f = open('query.txt', 'w+')
    f.write('melhorou '+ test['teste'] + ' ' + test['teste2'] + ' ' + test['teste3'] + ' '+  test['mostrando'])
    f.close()
    return send_file('query.txt', as_attachment=True)

@app.route('/')
def main():
    return 'xd'

if __name__ == '__main__':
    app.run(debug=True)
