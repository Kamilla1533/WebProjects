from flask import *
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api()

courses = {1 : {"name" : "Python Developer", "jobs" : 10},
           2 : {"name" : "C++ Developer", "jobs" : 15}}

class Main(Resource):
    def get(self, course_id):
        if course_id == 0:
            return courses
        else:
            return courses[course_id]

api.add_resource(Main, "/api/main/<int:course_id>")
api.init_app(app)

#if __name__ == 'main':
app.run(debug=True, port=8000, host="127.0.0.1")