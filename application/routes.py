from flask import request, jsonify
from flask_restful import Resource
from application.models import Device, TimeSeriesData, db

class DeviceResource(Resource):
    def post(self):
        data = request.get_json()
        # Validate and save device data
        return jsonify({'message': 'Device registered successfully.'})

class TimeSeriesResource(Resource):
    def post(self):
        data = request.get_json()
        # Validate and save time series data
        return jsonify({'message': 'Data ingested successfully.'})
