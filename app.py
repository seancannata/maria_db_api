# import the necessary packages
import flask
import json
import mariadb
import os
import logging

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

config = {
    'host': str(os.environ['HOST']),
    'port': int(os.environ['PORT']),
    'user': str(os.environ['USER']),
    'password': str(os.environ['PASSWORD']),
    'database': str(os.environ['DATABASE'])
}
'''


def create_config():
  config = {
    'host': str(os.environ['HOST']),
    'port': int(os.environ['PORT']),
    'user': str(os.environ['USER']),
    'password': str(os.environ['PASSWORD']),
    'database': str(os.environ['DATABASE'])
  }

  if (os.environ.get('HOST') == None):
    config['host'] = '127.0.0.1'
  if (os.environ.get('PORT') == None):
    config['port'] = 3306
  if (os.environ.get('USER') == None):
    config['user'] = 'root'
  if (os.environ.get('PASSWORD') == None):
    config['password'] = "Password123!"
  if (os.environ.get('DATABASE') == None):
    config['database'] = 'demo'

  return config


# route to return hello.
@app.route('/', methods=['GET'])
def default():
  return 'Goodbye!'


# route to return all people
@app.route('/api/books', methods=['GET'])
def index():
  conn = mariadb.connect(user=config['user'],
    password=config['password'],
    host=config['host'],
    port=config['port'],
    database='test')
  cur = conn.cursor()
  cur.execute("select * from books")
  row_headers=[x[0] for x in cur.description]
  rv = cur.fetchall()
  json_data=[]
  for result in rv:
    json_data.append(dict(zip(row_headers,result)))
  return json.dumps(json_data)


# MAIN
if __name__ == '__main__':
  config = create_config()
  app.run()
