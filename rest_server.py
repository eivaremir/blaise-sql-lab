from flask import Flask, request
from flask_restful import Resource, Api
from waitress import serve
app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'about':'hello world'}
    
    def post(self):
        some_json=request.get_json()
        return {'you sent': some_json},201
class Multi(Resource):
    def get(self,num):
        return {'result':num*10}

api.add_resource(HelloWorld,"/")
api.add_resource(Multi,"/multi/<int:num>")

if __name__== '__main__':
    app.run(port=8080, debug=True)
    #serve(app,host='127.0.0.1', port=8080, threads=1) #WAITRESS!