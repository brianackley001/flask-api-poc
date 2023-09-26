from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


names = {
      "john": {"age": 25, "hobby": "reading"},
      "jane": {"age": 31, "hobby": "singing"},
      "tim": {"age": 84, "hobby": "wizard"},
      "bill": {"age": 22, "hobby": "wyld stallionz"},
      "ted": {"age": 22, "hobby": "wyld stallionz"}
      }
    
class HelloWorld(Resource):
  def get(self, name):
    return names[name]
  


api.add_resource(HelloWorld, "/helloworld/<string:name>")

if __name__ == "__main__":
  app.run(debug=True)