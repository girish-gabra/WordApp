from flask import request
from flask_restful import Resource
from random import randint

#this API returns random word when user passes two or more words
class RandomWord(Resource):
	def get(self):
		pass

	def post(self):
		#words = request.form['words']
		json_data = request.get_json(force=True)
		wordList = json_data['words']		
		wordList = wordList.split(",")  # split comma separated string into list of words
		numWords = len(wordList)		
		randomIndex = randint(0,numWords-1)	# generates a random index so that random word can be returned
		return {'random': wordList[randomIndex]}
