from flask import Flask, request, render_template, send_file
from flask_pymongo import PyMongo
import psycopg2

app = Flask(__name__)

app.config["MONGO_DBNAME"] = "FEI_DB"
app.config["MONGO_URI"] = "mongodb://127.0.0.1:27017/FEI_DB"

connection = psycopg2.connect("dbname=postgres user=postgres password=feidb")
cursor = connection.cursor()

mongo = PyMongo(app)

@app.route('/postgres')
def insert():
    cursor.execute("SELECT * FROM conta;")
    resultlist = cursor.fetchall()
    f = open('queryPostgres.txt', 'w+')
    for result in resultlist:
        f.write(str(result) + '\n')
    f.close()
    return send_file('queryPostgres.txt', as_attachment=True)

@app.route('/mongo')
def show():
    contas = mongo.db.contas
    test = contas.find_one({'teste': 'teste'})
    f = open('queryMongo.txt', 'w+')
    f.write('melhorou '+ test['teste'] + ' ' + test['teste2'] + ' ' + test['teste3'] + ' '+  test['mostrando'])
    f.close()
    return send_file('queryMongo.txt', as_attachment=True)

@app.route('/')
def main():
    return render_template('main.html')

if __name__ == '__main__':
    app.run(debug=True)
