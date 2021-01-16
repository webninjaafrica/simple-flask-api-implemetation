from flask import Flask, render_template, session, jsonify
import json
from flask_sqlalchemy import SQLAlchemy
#Id, Name, Branch, College, Batch, Programme, Course, First_Language





app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="mysql+mysqlconnector://root:@localhost/students_info"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
app.config["SECRET_KEY"]="qw24352vgfd"

db=SQLAlchemy(app)

class students_data(db.Model):
	id=db.Column('id',db.Integer,primary_key=True)
	name=db.Column(db.VARCHAR(150))
	branch=db.Column(db.VARCHAR(150))
	college=db.Column(db.VARCHAR(150))
	batch=db.Column(db.VARCHAR(150))
	program=db.Column(db.VARCHAR(150))
	course=db.Column(db.VARCHAR(150))
	first_language=db.Column(db.VARCHAR(150))
	def __init__(self,name,branch,college,batch,program,course,first_language):
		self.name=name
		self.branch=branch
		self.college=college
		self.batch=batch
		self.program=program
		self.course=course
		self.first_language=first_language


#db.create_all()	

@app.route("/")
def index():
	data='''
	<html><head><title>STUDENTS _ API</title></head>
	<body><center>
	<h3>Click the link below to proceed to the api page...</h3><p><hr>
	<p> <a href='mcit/cst-students/all'>PROCCEED TO API</a></center></body>
	'''
	return data

@app.route("/mcit/cst-students/all")
def students_api():
	data=students_data.query.all()
	#print(data)
	cols=['id','name','branch','college','batch','program','course','first_language']
	res=[{col:getattr(d,col) for col in cols} for d in data]
	return jsonify(result=res)

if __name__=="__main__":
	app.run(debug=True)