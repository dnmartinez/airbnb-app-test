from flask import Flask, request, render_template, jsonify, make_response
import pymysql
import pymysql.cursors

from secrets_manager import get_secret

"""db_username = "admin"
db_password = "yokocat22"
db_name = "listings"
db_endpoint = "naomi-airbnb-db.chjxclsv9tv3.us-east-2.rds.amazonaws.com""""
client = boto3.client('secretsmanager')
response = client.get_secret_value(
    SecretId='naomi-airbnb-db-sm'
)
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
            # Read a single record
            sql = "SELECT * FROM nl_listing WHERE price <= 150 ORDER BY price"
            cursor.execute(sql)
            result = cursor.fetchall()
    return make_response(jsonify({'lisnting': result}))
    #return render_template("affordable.html", data=result)
        
        #return render_template("affordable.html", name=result)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')