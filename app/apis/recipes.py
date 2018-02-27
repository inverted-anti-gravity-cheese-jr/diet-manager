from bson import json_util
from bson.objectid import ObjectId
from flask import Blueprint, Response, request
from app.web_config import db

recipe_api = Blueprint('recipes', __name__)

@recipe_api.route("/count", methods=["GET"])
def getRecipeCount():
	return Response(json_util.dumps({"count": db.recipes.count()}), mimetype="application/json")

@recipe_api.route("/", methods=["GET"])
def getRecipes():
	recipes = list(db.recipes.find())
	return Response(json_util.dumps(recipes), mimetype="application/json")

@recipe_api.route("/<recipe>", methods=["GET"])
def getRecipe(recipe):
	recipe = db.recipes.find_one({"_id": ObjectId(recipe)})
	return Response(json_util.dumps(recipe), mimetype="application/json")

@recipe_api.route("/", methods=["POST", "PUT"])
def addOrUpdateRecipe():
	name = request.form.get('name')
	ingredients = request.form.get('ingredients')
	description = request.form.get('description')
	recipe = {"name": name, "ingredients": ingredients, "description": description}
	result = db.recipes.insert_one(recipe)
	return json_util.dumps(result.inserted_id)