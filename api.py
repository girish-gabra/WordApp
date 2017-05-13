from flask import Flask
from flask_restful import Api, Resource
from resources.allresources import Welcome
from resources.allresources import RandomWord
from resources.allresources import RhymeForWord
from resources.allresources import SuggestWord

# Create a flask instance
app = Flask(__name__)

api = Api(app)	#Create Api for app instance

# Add the resources to our Api instance
api.add_resource(Welcome, '/')
api.add_resource(RandomWord,'/random')
api.add_resource(RhymeForWord,'/rhyme')
api.add_resource(SuggestWord,'/suggest')



