from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient("mongodb://localhost:27017/")
db = client.diets

from app.apis.recipes import recipe_api
app.register_blueprint(recipe_api, url_prefix = "/recipe")

