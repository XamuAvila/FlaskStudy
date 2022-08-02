from flask_restful import Resource

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


class Hotel(Resource):
    def get(self, hotel_id):
        for hotel in hotels:
            if (hotel['hotel_id'] == hotel_id):
                return hotel
        return {'message': 'Hotel not found'}, 404

    def post(self, hotel_id):
        pass
    def put(self, hotel_id):
        pass

    def delete(self, hotel_id):
        pass
