from flask import Flask,request,jsonify
#from flask_cors import CORS
#from recommender import recommender


app = Flask(__name__)
#CORS(app) 

@app.route("/")
def home():
    return "Hello World! I'm using Flask."
        
@app.route('/movie', methods=['GET'])
def recommend_movies():
    #res = recommender()
    #res = recommender(request.args.get('title'))
    return jsonify(res)

if __name__=='__main__':
    app.run(port = 5000, debug = True)



