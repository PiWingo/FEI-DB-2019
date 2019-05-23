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
    subqueryString = 'SELECT \"Id_Prod\" FROM public.\"Produto\" WHERE \"Id_Prod\" BETWEEN 1 AND 250000 AND (CAST(\"Valor_Unit\" AS TEXT) LIKE \'%1%\' OR CAST(\"Valor_Unit\" AS TEXT) LIKE \'%0%\') AND \"Versao\" > 2004'
    cursor.execute(subqueryString)
    print(subqueryString)
    idResult = cursor.fetchall()
    queryString = 'SELECT * FROM public.\"Pedido\" WHERE \"Produto_Id_Prod\" IN (\''+ '\',\''.join(idResult)  +'\') AND \"Quantidade\" BETWEEN 10 AND 75 AND \"Valor_Total\" >= 1554 AND \"Conta_Cnpj\" LIKE \'%1%\' ORDER BY \"Valor_Total\" DESC'
    print(queryString);
    cursor.execute(queryString)
    resultlist = cursor.fetchall()
    f = open('queryPostgres.txt', 'w+')
    for result in resultlist:
        f.write(str(result) + '\n')
    f.close()
    return send_file('queryPostgres.txt', as_attachment=True)

@app.route('/mongo')
def show():
    contas = mongo.db.contas
    produto = mongo.db.produto
    #'SELECT \"Id_Prod\" FROM public.\"Produto\" WHERE \"Id_Prod\" BETWEEN 1 AND 250000 AND (CAST(\"Valor_Unit\" AS TEXT) LIKE \'%1%\' OR CAST(\"Valor_Unit\" AS TEXT) LIKE \'%0%\') AND \"Versao\" > 2004'
    query = [{'$match':{'Quantidade':{'$gte': 1,'$lte': 75}, 'Valor_Total':{'$gte': 1554}, 'Conta_Cnpj': '%o%', 'Id_Prod': produto.find([{'$match': 'Id_Prod': {'$gte': 1,'$lte': 250000}, {'$or': {'Valor_Unit': '%1%', 'Valor_Unit': '%0%'}}, 'Versao': {'$gt': 2004}}])}},{'$sort':{"Valor_Total": 1.0}}, {'$project': {'Id_Ped': 1.0, 'Conta_Cnpj': 1.0, 'Quantidade': 1.0, 'Valor_Total': 1.0,'Produto_Id_Prod': 1.0, 'Forma_Pagamento': 1.0}}]
    f = open('queryMongo.txt', 'w+')
    f.write('melhorou '+ test['teste'] + ' ' + test['teste2'] + ' ' + test['teste3'] + ' '+  test['mostrando'])
    f.close()
    return send_file('queryMongo.txt', as_attachment=True)

@app.route('/')
def main():
    return render_template('main.html')

if __name__ == '__main__':
    app.run(debug=True)
