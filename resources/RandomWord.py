from flask_restful import Resource

class RandomWord(Resource):
	def post(self):
		words = request.form['words']
		wordList = words.split(",")
		return {'random': wordList[0]}
