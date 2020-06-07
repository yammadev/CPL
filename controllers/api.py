from application import app as api
from database.base import db
from flask import Flask, request, make_response, jsonify

from models.pothole import Pothole

# List potholes...
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

    message = {'message': 'no hay contenido para mostrar'}
    return make_response(jsonify(message), 204)

# Save a pothole...
# [POST]
# @return response
@api.route('/save', methods = ['POST'])
def save():
    data = request.get_json()

    # Check if it's registered
    if Pothole.query.filter((Pothole.lat == data['lat']) and (Pothole.lng == data['lng'])).first():
        message = {'message': 'este punto ha sido reportado previamente, intente nuevamente con otro punto.'}
        return make_response(jsonify(message), 422)

    # Check if it's info is completed
    if not data['name'] or not data['desc']:
        message = {'message': 'Hay campos requeridos, por favor llénelos para continuar.'}
        return make_response(jsonify(message), 422)

    # Save and return
    name = data['name']
    lat = data['lat']
    lng = data['lng']
    desc = data['desc']
    stat = 'reported'

    pothole = Pothole(name = name, lat = lat, lng = lng, desc = desc, stat = stat)
    pothole.save()

    return make_response(pothole.serialize(), 200)

# Update a pothole...
# [POST]
# @return response
@api.route('/update', methods = ['POST'])
def update():
    data = request.get_json()

    pothole = Pothole.query.get(data['id'])

    if not pothole:
        message = {'message': 'Registro no existe'}
        return make_response(jsonify(message), 200)

    pothole.stat = data['stat']
    db.session.commit()

    message = {'message': 'Registro actualizado.'}
    return make_response(jsonify(message), 200)
