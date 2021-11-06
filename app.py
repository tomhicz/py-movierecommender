from flask import Flask,request,jsonify
#from flask_cors import CORS
from recommender import recommender
from recommender2 import recommender2


app = Flask(__name__)
#CORS(app) 

@app.route("/")
def home():
    return "Hello World! I'm using Flask."
        
@app.route('/movie', methods=['GET'])
def recommend_movies():
    searchword = request.args.get('name', '')
    res = recommender(searchword)
    #res = recommender(request.args.get('title'))
    return jsonify(res)
    #return f'you requested {searchword}'

@app.route('/movies', methods=['GET'])
def recommend_movies2():
    searchword = request.args.get('name', '')
    res = recommender2(searchword)
    #res = recommender(request.args.get('title'))
    return jsonify(res)
    #return f'you requested {searchword}'

#This runs on the local dev server only 
if __name__=='__main__':
    app.run(port = 5000, debug = True)



