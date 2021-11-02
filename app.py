from flask import Flask, request, render_template, jsonify, make_response
from secrets_manager import get_secret
import pymysql
import pymysql.cursors
import boto3



app = Flask(__name__)
db_config = get_secret()


@app.route("/")
def index():
    #return 'hello from Naomi'
    return render_template("index.html")

@app.route("/affordable", methods=['GET'])
def affordabe():
    connection= pymysql.connect(host=db_config["host"], user=db_config["username"], passwd=db_config["password"], db=db_config["db_name"], cursorclass=pymysql.cursors.DictCursor)
    with connection:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM nl_listing WHERE price <= 150 ORDER BY price"
            cursor.execute(sql)
            result = cursor.fetchall()
    return make_response(jsonify({'lisnting': result}))
    
    #return render_template("affordable.html", data=result)
        
        #return render_template("affordable.html", name=result)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')