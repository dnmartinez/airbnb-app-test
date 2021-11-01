from flask import Flask, request, render_template, jsonify
import pymysql
import os

db_username = "admin"
db_password = "yokocat22"
db_name = "listings"
db_endpoint = "naomi-airbnb-db.chjxclsv9tv3.us-east-2.rds.amazonaws.com"
app = Flask(__name__)
#api = Api(app) # wrap our app in an API. Initializes fact that we are using restful api

@app.route("/")
def index():
    #return 'hello from Naomi'
    return render_template("index.html")

@app.route("/affordable", methods=['GET'])
def affordabe():
    connection= pymysql.connect(host=db_endpoint, user=db_username, passwd=db_password, db=db_name)
    with connection:

        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT * FROM nl_listing WHERE price <= 80"
            cursor.execute(sql)
            result = jsonify(cursor.fetchall())
    return result
        
        #return render_template("affordable.html", name=result)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')