from flask import request
from flask.views import MethodView
from uuid import uuid4
from flask_smorest import abort
from schemas import CarSchema
from . import bp
from db import cars
from models.car_model import CarModel

@bp.route('/car', methods=['GET', 'POST'])
class CarList(MethodView):
    
    @bp.response(200, CarSchema(many=True))
    def get(self):
        return list(cars.values())
    
    @bp.arguments(CarSchema)
    @bp.response(201, CarSchema)
    def post(self, data):
        try:
            car = CarModel()
            car.from_dict(data)
            car.save_car()
            return {
                'success' : f'{car.make} {car.model} added'
            }, 201
        except:
            return {
                'error' : 'forgot to add make and model'
            }, 400
 

@bp.route('/car/<int:id>', methods=['GET', 'PUT', 'DELETE'])
class Car(MethodView):
    
    @bp.response(200, CarSchema)
    def get(self, id):
        car = CarModel.query.get(id)
        if car:
            return car
        else:
            abort(400, message='invalid car id')

    @bp.arguments(CarSchema)
    def put(self, data, id):
        car = CarModel.query.get(id)
        if car:
            car.from_dict(data)
            car.save_car()
            return { 'message': 'car updated' }, 200
        else:
            abort(400, message='invalid car id')    

    def delete(self, id):
        car = CarModel.query.get(id)
        if car:
            car.del_car()
            return { 'message': 'car deleted' }, 200
        else:
            abort(400, message='invalid car id')
