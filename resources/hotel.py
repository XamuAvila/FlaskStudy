from flask_restful import Resource, reqparse

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
        args = reqparse.RequestParser()
        args.add_argument('nome')
        args.add_argument('estrelas')
        args.add_argument('diaria')
        args.add_argument('cidade')
        data = args.parse_args()
        novo_hotel = {
            'hotel_id': hotel_id,
            'nome': data['nome'],
            'estrelas': data['estrelas'],
            'diaria': data['diaria'],
            'cidade': data['cidade']
        }

        hotels.append(novo_hotel)
        return novo_hotel, 200
    def put(self, hotel_id):
        pass

    def delete(self, hotel_id):
        pass
