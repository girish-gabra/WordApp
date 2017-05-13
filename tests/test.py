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

	# helper function to call random word API
	def random_helper(self,wordsList):
		return self.app.post('/random',data = json.dumps(dict(words=wordsList)), content_type='application/json')		
	
	#test random word API
	def test_random_word(self):
		words = 'king,queen,jack,spade,ace'
		response = self.random_helper(words)
		self.assertEqual(response.status_code,200)		# check the response code
		json_dict=json.loads(response.data.decode("utf-8").rstrip()) # check if random string existed in original string
		self.assertIn(json_dict['random'],words)

	# test json input for Random Word Api
	def test_random_word_for_json(self):
		wordsList = 'king,queen,jack,spade,ace'
		response = self.app.post('/random',data=dict(words=wordsList))
		#print(response.data)
		self.assertIn(b"Input should have JSON data format",response.data)

	# test if input is less than two words
	def test_random_word_less_than_two(self):
		words=""
		response = self.random_helper(words)		
		self.assertIn(b'Please enter atleast two words',response.data)
		words="hello"
		response = self.random_helper(words)		
		self.assertIn(b'Please enter atleast two words',response.data)

	#test for rhyme words api
	def test_rhyming_words(self):
		word = 'climbing'
		data = {'word':word}
		response = self.app.get('/rhyme',query_string=data)
		self.assertEqual(response.status_code,200)

	def test_rhyming_words_parameter(self):
		word = 'climbing'
		data = {'word':word,'abc':word}
		response = self.app.get('/rhyme',query_string=data)		
		self.assertIn(b"Only one parameter 'word' allowed",response.data)
	
	def test_rhyming_words_parameter1(self):
		word = 'climbing'
		data = {'abc':word}
		response = self.app.get('/rhyme',query_string=data)		
		self.assertIn(b"Parameter 'word' is missing",response.data)

	def test_rhyming_words_empty(self):
		word = ''
		data = {'word':word}
		response = self.app.get('/rhyme',query_string=data)		
		self.assertIn(b"Word cannot be empty",response.data)		

	def test_suggest_words(self):
		word = 'helo'
		data = {'word':word}
		response =self.app.get('/suggest',query_string=data)
		self.assertEqual(response.status_code,200)

	def test_suggest_words_parameter(self):
		word = 'helo'
		data = {'word':word,'abc':word}
		response =self.app.get('/suggest',query_string=data)
		self.assertIn(b"Only one parameter 'word' allowed",response.data)

	def test_suggest_words_parameter1(self):
		word = 'helo'
		data = {'abc':word}
		response =self.app.get('/suggest',query_string=data)
		self.assertIn(b"Parameter 'word' is missing",response.data)

	def test_suggest_words_empty(self):
		word = ''
		data = {'word':word}
		response =self.app.get('/suggest',query_string=data)
		self.assertIn(b'Word cannot be empty',response.data)

if __name__ == "__main__":
	unittest.main()

