from flask_restful import Resource
import logging as logger
import pymysql

conn = pymysql.connect(host="15.206.81.188", user="root", password="Password@123", database="testdb")
mydbconnection = conn.cursor()
class Task(Resource):

    def post(self,emp_id,emp_name):
        logger.debug("Inisde the post method of Task - adding user")
        mydbconnection.execute("INSERT INTO employee VALUES ('%i', '%s')"%(emp_id, emp_name))
        #return {"message" : mydbconnection.fetchall()},200
        conn.commit()
        conn.close()

    def get(self,emp_id=None,emp_name=None):
        logger.debug("Inisde the get method of Task")
        sql = "SELECT * FROM employee"
        mydbconnection.execute(sql)
       # mydbconnection.execute("SELECT * FROM employee;")
        return {"message" : mydbconnection.fetchall()},200
        conn.commit()
        conn.close()

    def put(self,emp_id,emp_name):
        logger.debug("Inisde the put method of Task")
        mydbconnection.execute("UPDATE employee SET emp_name=('%s') WHERE emp_id=('%i');"),200
        #return {"message" : mydbconnection.fetchall()},200
        conn.commit()
        conn.close()

    def delete(self,emp_id,emp_name):
        logger.debug("Inisde the delete method of Task")
        mydbconnection.execute("DELETE FROM employee WHERE emp_id=('%i');"),200
        #return {"message" : "Inside delete method"}
        conn.commit()
        conn.close()





