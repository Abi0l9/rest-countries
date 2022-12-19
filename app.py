import requests
from flask import Flask, request
from flask_migrate import Migrate

app = Flask(__name__)
migrate = Migrate(app)


if __name__=='__main__':
    app.run(debug=True)