# import the necessary packages
import flask
import json
import mariadb
import os

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# configuration used to connect to MariaDB
'''
config = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'password': 'Password123!',
    'database': 'demo'
}

export HOST=127.0.0.1
export PORT=3306
export USER=root
export PASSWORD=Password123!
export DATABASE=demo
'''

config = {
    'host': str(os.environ['HOST']),
    'port': int(os.environ['PORT']),
    'user': str(os.environ['USER']),
    'password': str(os.environ['PASSWORD']),
    'database': str(os.environ['DATABASE'])
}

# route to return all people
@app.route('/', methods=['GET'])
def default():
  return 'Hello!'

# route to return all people
@app.route('/api/books', methods=['GET'])
def index():
   # connection for MariaDB
   conn = mariadb.connect(**config)
   # create a connection cursor
   cur = conn.cursor()
   # execute a SQL statement
   cur.execute("select * from books")

   # serialize results into JSON
   row_headers=[x[0] for x in cur.description]
   rv = cur.fetchall()
   json_data=[]
   for result in rv:
        json_data.append(dict(zip(row_headers,result)))

   # return the results!
   return json.dumps(json_data)

app.run()

