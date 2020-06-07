from application import app as api
from database.base import db
from flask import Flask, request, make_response, jsonify

from models.pothole import Pothole

# List route...
# [GET]
# @return response
@api.route('/list')
def list():
    potholes = Pothole.query.all()
    list = {}

    for pothole in range(0, len(potholes)):
        list[pothole + 1] = {
            'id': potholes[pothole].id,
            'name': potholes[pothole].name,
            'lat': potholes[pothole].lat,
            'lng': potholes[pothole].lng,
            'desc': potholes[pothole].desc,
            'stat': potholes[pothole].stat
        }

    if list:
        return make_response(list, 200)

    data = {'message': 'no hay contenido para mostrar'}
    return make_response(jsonify(data), 204)

# Save a pothole in database
# [POST]
# @return response
@api.route('/save', methods = ['POST'])
def save():
    data = request.get_json()

    # Check if it's registered
    if Pothole.query.filter((Pothole.lat == data['lat']) and (Pothole.lng == data['lng'])).first():
        data = {'message': 'este punto ha sido reportado previamente, intente nuevamente con otro punto.'}
        return make_response(jsonify(data), 422)

    # Check if it's info is completed
    if not data['name'] or not data['desc']:
        data = {'message': 'Hay campos requeridos, por favor llénelos para continuar.'}
        return make_response(jsonify(data), 422)

    # Save and return
    name = data['name']
    lat = data['lat']
    lng = data['lng']
    desc = data['desc']
    stat = 'reported'

    pothole = Pothole(name = name, lat = lat, lng = lng, desc = desc, stat = stat)
    pothole.save()

    return make_response(pothole.serialize(), 200)
