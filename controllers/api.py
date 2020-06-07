from application import app as api
from database.base import db
from flask import Flask, request, make_response, jsonify
import datetime
import json

from models.pothole import Pothole

# List potholes...
# [GET]
# @return response
@api.route('/list')
def list():
    potholes = Pothole.query.all()
    list = []

    # Serialize
    for pothole in range(0, len(potholes)):
        list.append({
            'id': potholes[pothole].id,
            'name': potholes[pothole].name,
            'lat': potholes[pothole].lat,
            'lng': potholes[pothole].lng,
            'desc': potholes[pothole].desc,
            'stat': potholes[pothole].stat,
            'date': potholes[pothole].date.strftime("%d-%m-%y %H:%M")
        })

    # There's data
    if list:
        return make_response(json.dumps(list), 200)

    # There's no data
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
    date = datetime.datetime.now()

    pothole = Pothole(name = name, lat = lat, lng = lng, desc = desc, stat = stat, date = date)
    pothole.save()

    return make_response(pothole.serialize(), 200)

# Update a pothole...
# [POST]
# @return response
@api.route('/update', methods = ['POST'])
def update():
    data = request.get_json()

    # Search
    pothole = Pothole.query.get(data['id'])

    # Check if exists
    if not pothole:
        message = {'message': 'Registro no existe'}
        return make_response(jsonify(message), 200)

    # Update
    pothole.stat = data['stat']
    pothole.date = datetime.datetime.now()
    db.session.commit()

    message = {'message': 'Registro actualizado.'}
    return make_response(jsonify(message), 200)

# Get statistics...
# [GET]
# @return response
@api.route('/statistics')
def statistics():
    potholes = Pothole.query.all()

    # There's no data
    if not potholes:
        message = {'message': 'no hay contenido para mostrar'}
        return make_response(jsonify(message), 204)

    # Compile and return
    reported = Pothole.query.filter(Pothole.stat == 'reported').count()
    repairing = Pothole.query.filter(Pothole.stat == 'repairing').count()
    repaired = Pothole.query.filter(Pothole.stat == 'repaired').count()
    total = reported + repairing + repaired

    data = {
        'current': {
            'total': total,
            'reported': reported,
            'repairing': repairing,
            'repaired': repaired,
        },
        'percentages': {
            'reported': round(reported * 100 / total, 2),
            'repairing': round(repairing * 100 / total, 2),
            'repaired': round(repaired * 100 / total, 2),
        }
    }

    return make_response(jsonify(data), 200)
