from flask import Flask
from flask_restful import Api, Resource
from resources.allresources import RandomWord
#from flask import request


app = Flask(__name__)

api = Api(app)

class HelloWorld(Resource):
	def get(self):
		return {'hello':'world'}




'''class RandomWord(Resource):
	def get(self):
		pass

	def post(self):
		words = request.form['words']
		#wordList = words.split(",")
		#return wordList[0]
		return words'''

api.add_resource(RandomWord,'/random')
api.add_resource(HelloWorld, '/');

