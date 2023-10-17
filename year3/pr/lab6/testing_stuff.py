from flask import Flask, request
from flask_restx import Api, Resource, fields

app = Flask(__name__)
api = Api(app, version='1.0', title='Electro Scooter API', description='A simple Electro Scooter API')
ns = api.namespace('scooters', description='Electro Scooter operations')

scooter = api.model('Scooter', {
    'id': fields.Integer(readonly=True, description='The scooter unique identifier'),
    'name': fields.String(required=True, description='The scooter name'),
    'battery_level': fields.Float(required=True, description='Battery level in percentage')
})

SCOOTERS_DB = {}

@ns.route('/')
class ScooterList(Resource):
    @ns.doc('list_scooters')
    @ns.marshal_list_with(scooter)
    def get(self):
        '''List all scooters'''
        return list(SCOOTERS_DB.values())

    @ns.doc('create_scooter')
    @ns.expect(scooter)
    @ns.marshal_with(scooter, code=201)
    def post(self):
        '''Create a new scooter'''
        scooter_id = len(SCOOTERS_DB) + 1
        SCOOTERS_DB[scooter_id] = {'id': scooter_id, **api.payload}
        return SCOOTERS_DB[scooter_id], 201

@ns.route('/<int:id>')
@ns.response(404, 'Scooter not found')
@ns.param('id', 'The scooter identifier')
class Scooter(Resource):
    @ns.doc('get_scooter')
    @ns.marshal_with(scooter)
    def get(self, id):
        '''Fetch a scooter given its identifier'''
        if id not in SCOOTERS_DB:
            api.abort(404)
        return SCOOTERS_DB[id]

    @ns.doc('delete_scooter')
    @ns.response(204, 'Scooter deleted')
    def delete(self, id):
        '''Delete a scooter given its identifier'''
        if id not in SCOOTERS_DB:
            api.abort(404)
        del SCOOTERS_DB[id]
        return '', 204

    @ns.doc('update_scooter')
    @ns.expect(scooter)
    @ns.marshal_with(scooter)
    def put(self, id):
        '''Update a scooter given its identifier'''
        if id not in SCOOTERS_DB:
            api.abort(404)
        SCOOTERS_DB[id].update(api.payload)
        return SCOOTERS_DB[id]

if __name__ == '__main__':
    app.run(debug=True)
