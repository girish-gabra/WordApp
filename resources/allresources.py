from flask import request
from flask_restful import Resource
from random import randint
import random
import pronouncing
import enchant

# this can be considered as a home page having welcome message
class Welcome(Resource):
	def get(self):
		return {'message':'welcome'}

#this resource returns random word when user passes two or more words
class RandomWord(Resource):
	def get(self):
		pass

	def post(self):
		#words = request.form['words']
		try:
			json_data = request.get_json(force=True)
		except:
			return {"error":"Input should have JSON data format"} 
		wordList = json_data['words']		
		wordList = wordList.split(",")  # split comma separated string into list of words
		if len(wordList) <= 1:
			return {"error":"Please enter atleast two words"}
		numWords = len(wordList)		
		randomIndex = randint(0,numWords-1)	# generates a random index so that random word can be returned
		return {'random': wordList[randomIndex]}

# this resource will return all the rhyming words according to the input word
class RhymeForWord(Resource):
	def get(self):
		args=request.args
		if(len(args)>1):
			return {"error":"Only one parameter 'word' allowed"}
		if('word' not in args.keys()):
			return {"error":"Parameter 'word' is missing"}
		
		word = args['word'].strip()	# remove trailing and leading spaces  
 
		if len(word)==0:
			return {"error":"Word cannot be empty"}		
		
		rhymeList = pronouncing.rhymes(word)	# Fetch list of rhyming words with the input word
		rhymeList = ",".join(rhymeList)			# form a string of all rhyming words separated by ','
		return {'rhymes':rhymeList}				# return json

#this resource will suggest list of 10 words that are close to the input word
class SuggestWord(Resource):
	def get(self):
		args=request.args
		if(len(args)>1):
			return {"error":"Only one parameter 'word' allowed"}
		if('word' not in args.keys()):
			return {"error":"Parameter 'word' is missing"}
		
		d=enchant.Dict("en_US")
		word = args['word'].strip()
		if len(word)==0:
			return {"error":"Word cannot be empty"}	
	
		suggestList = list(d.suggest(word))[:10]
		suggestList = ",".join(suggestList)
		return {'suggestions': suggestList}
		
		
