# Get base path
import sys
sys.path.append('../')

# Import
from app import app as main
from flask import Flask, render_template, request, redirect, url_for
from models.models import Pothole,db


@main.before_first_request
def create_tables():
    db.create_all()

# Index route...
# [GET]
# @return response
@main.route('/')
def index():
	data = Pothole.query.all()
	return render_template('index.html',data=data,status=2)

#Save a pothole in database
@main.route('/saveplothole', methods=['POST'])
def add_pothole():
	potholes = Pothole.query.all()
	aux = []
	repeat = 0
	if request.method == 'POST':
		name = request.form['name']
		lat = request.form['latitude']
		lng = request.form['longitude']
		des = request.form['description']
		loc = (lat,lng)

		for i in potholes:
			aux.append((i.lat,i.lngd))
		print(aux)
		for i in aux:
			if i == loc:
				repeat+=1
		
		if repeat > 0:
			return render_template('index.html',data=potholes,status=1)
		else:
			pothole = Pothole(name=name,lat=lat,lngd=lng,description=des)
			db.session.add(pothole)
			db.session.commit()
			return render_template('index.html',data=potholes,status=0)

