from app import app 
from secret_name import get_secret
import sys
import json
import pymysql
import pymysql.cursors
logger = logging.getLogger()
logger.setLevel(logging.INFO)

try:
    db_config = get_secret()
    connection= pymysql.connect(host=db_config["host"], user=db_config["username"], passwd=db_config["password"], db=db_config["db_name"], cursorclass=pymysql.cursors.DictCursor)
except pymysql.MySQLError as e:
        logger.debug("Connection could not be established  ",e)
        sys.exit()
logger.info("SUCCESS: Connection was established")

@app.route('/affordable_stays/<amount>')
def affordable(amount:int):
    column = 'price'
    with connection:
        with connection.cursor() as cursor:
            # Read a single record
            sql = ''' SELECT * FROM nl_listing WHERE (%s) <= (%s) AND (%s) != 0 ''' %(price, amount)
            cursor.execute(sql)
            result = cursor.fetchall()
    return json.dumps(result)

@app.route('/expensive_stays/<amount>')
def exprensive(amount:int):
    with connection:
        with connection.cursor() as cursor:
            # Read a single record
            sql = ''' SELECT * FROM nl_listing WHERE (%s) => (%s) ''' %(price, amount)
            cursor.execute(sql)
            result = cursor.fetchall()
    return json.dumps(result)


@app.route('/neighborhood/<name>')
def neighborhood(name:str):
    with connection:
        with connection.cursor() as cursor:
            # Read a single record
            sql = ''' SELECT * FROM nl_listing WHERE (%s) LIKE (%s) ''' %(neighbourhood, name)
            cursor.execute(sql)
            result = cursor.fetchall()
    return json.dumps(result)

@app.route('/housing_type/<hosing>')
def housing_type(name:str):
    with connection:
        with connection.cursor() as cursor:
            # Read a single record
            sql = ''' SELECT * FROM nl_listing WHERE (%s) LIKE (%s) ''' %(room_type, hosing)
            cursor.execute(sql)
            result = cursor.fetchall()
    return json.dumps(result)

@app.route('/expensive_neighborhoods/<neighborhood>/<amount>')
def expensive_neighborhoods(name:str, amount:int):
    with connection:
        with connection.cursor() as cursor:
            # Read a single record
            sql = ''' SELECT * FROM nl_listing WHERE (%s) LIKE (%s) AND (%s) >= (%s) ''' %(neighbourhood, name, price, amount)
            cursor.execute(sql)
            result = cursor.fetchall()
    return json.dumps(result)

@app.route('/')
def index():
    #return 'hello from Naomi'
    return '<h1>Index</h1>'