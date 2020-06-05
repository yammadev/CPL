from application import app as api
from database.base import db
from flask import Flask, render_template, request, jsonify

from models.pothole import Pothole

# List route...
# [GET]
# @return response
@api.route('/list')
def list():
    potholes = Pothole.query.all()
    potholes_json = {}

    for pothole in range(0, len(potholes)):
        potholes_json[pothole + 1] = {
          'name': potholes[pothole].name,
          'position': [potholes[pothole].lat, potholes[pothole].lng],
          'desc': potholes[pothole].desc
        }

    if potholes_json:
        return jsonify(potholes_json)

    return jsonify(error = 'Database is empty... Please fill it')

# Save a pothole in database
# [POST]
# @return # TODO:
@api.route('/save', methods = ['POST'])
def save():
	potholes = Pothole.query.all()
	aux = []
	repeat = 0

	if request.method == 'POST':
		name = request.form['name']
		lat = request.form['latitude']
		lng = request.form['longitude']
		des = request.form['description']
		loc = (lat, lng)

    	for i in potholes:
    		aux.append((i.lat, i.lng))

    	for i in aux:
    		if i == loc:
      			repeat += 1

    	if repeat > 0:
    		return render_template('index.html', potholes = potholes)     # TODO

    	pothole = Pothole(name = name, lat = lat, lng = lng, desc = des)
    	pothole.save()
    	return render_template('index.html', potholes = potholes)
