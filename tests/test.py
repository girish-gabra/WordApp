import unittest
import json
import sys,os
sys.path.append(os.path.abspath(os.path.join('..')))

from api import app

class AppTest(unittest.TestCase):
	def setUp(self):	
		self.app = app.test_client()
		self.app.testing = True			

	#test main page
	def test_main_page(self):
		response = self.app.get('/')
		self.assertEqual(response.status_code,200)

	def random_helper(self,wordsList):
		return self.app.post('/random',data = json.dumps(dict(words=wordsList)), content_type='application/json')		

	#test random word API
	def test_random_word(self):
		words = 'king,queen,jack,spade,ace'
		response = self.random_helper(words)
		self.assertEqual(response.status_code,200)
				
	#test for rhyme words api
	def test_rhyming_words(self):
		word = 'climbing'
		data = {'word':word}
		response = self.app.get('/rhyme',query_string=data)
		self.assertEqual(response.status_code,200)

	def test_suggest_words(self):
		word = 'helo'
		data = {'word':word}
		response =self.app.get('/suggest',query_string=data)
		self.assertEqual(response.status_code,200)

if __name__ == "__main__":
	unittest.main()

