from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "***postgres uri goes here (add ql to the end of postgres)***"

db = SQLAlchemy(app)
ma = Marshmallow(app)
CORS(app)