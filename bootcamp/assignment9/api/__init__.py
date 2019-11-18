from flask_restful import Api
from app import flaskAppInstance
from .TaskAPI import Task


restServerInstance = Api(flaskAppInstance)

restServerInstance.add_resource(Task,"/api/v1.0/task/<int:emp_id>/<string:emp_name>")
