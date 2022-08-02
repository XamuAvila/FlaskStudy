from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

hotels = [
    {
        'hotel_id': 'alpha',
        'nome': 'Alpha Hotel',
        'estrelas': 4.3,
        'diaria': 420.34,
        'cidade': 'Rio'
    },
    {
        'hotel_id': 'Xamu',
        'nome': 'Xamu Hotel',
        'estrelas': 4.3,
        'diaria': 420.34,
        'cidade': 'Rio'
    },
    {
        'hotel_id': 'Yas',
        'nome': 'Yas Hotel',
        'estrelas': 4.3,
        'diaria': 420.34,
        'cidade': 'Rio'
    },
]

class Hotels(Resource):
    def get(self):
        return {'hoteis': hotels}


api.add_resource(Hotels, '/hotels')

if __name__ == '__main__':
    app.run()
