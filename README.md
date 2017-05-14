# WordApp

WordApp is an application build using Python 3 and Flask. It has the following features: 

1) Randomly return a word when user provides two or more words.

2) Provide list of rhyming words for any word given by user.

3) Provide list of suggested words for any word given by user.

To run WordApp you need to execute run.py with following command:

**python run.py**

By default app will run on port 5000 and main page can be checked using url: http://127.0.0.1:5000/

Input format and accessing three endpoints can be described as:

#### /random (http://127.0.0.1:5000/random)

For returning random words from list of words, this API is of type POST. Input to this API should be JSON
with **key = words** and **values = string concatenation of one or more strings separated by comma**.<br/>
eg : {"words" : "king,tim,knight,pawn,world,hello"}
Output from this API is JSON with **key=random** and **value=a random string from input**.
eg: {"random":"tim"}

#### /rhyme (http://127.0.0.1:5000/rhyme)

This is a GET request. Word for which rhyming words need to be found, is passed as a URL parameter.
Output of this is a JSON with **key=rhymes** and value = **rhyme words separated by comma**.<br/>
eg: Input: word = cooking <br/>
Output: {"rhymes": "booking,brooking,hooking,looking,overcooking"}

#### /suggest (http://127.0.0.1:5000/suggest)

This is a GET request. Suggestion words can be very useful in cases when user is not sure of correct spelling, this API will return ten words which will help user to find the correct spelling. This API suggests words according to English US dictionary.
The partial word can be passed as a Url parameter **word**. Output is a JSON with **key=suggestions** and value = **suggested words separated by comma**.<br/>
eg: Input:  word=amazi<br/>
Output: { "suggestions": "amaze,amazing,Mazama,Mazzini,AMA,amazon,Amazon" }
  

