from flask_restful import Resource, reqparse
from models.hotel import HotelModel
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
    args = reqparse.RequestParser()
    args.add_argument('nome')
    args.add_argument('estrelas')
    args.add_argument('diaria')
    args.add_argument('cidade')

    def get(self, hotel_id):
        hotel = Hotel.findHotel(hotel_id)
        if hotel is not None:
            return hotel
        return {'message': 'Hotel not found'}, 404

    def post(self, hotel_id):
        data = Hotel.args.parse_args()
        novo_hotel = HotelModel(hotel_id, **data).json()
        hotels.append(novo_hotel)
        return novo_hotel, 200

    def put(self, hotel_id):
        hotel = Hotel.findHotel(hotel_id)
        data = Hotel.args.parse_args()
        novo_hotel = HotelModel(hotel_id, **data).json()
        if hotel is not None:
            hotel.update(novo_hotel)
            return novo_hotel, 200

        hotels.append(novo_hotel)
        return novo_hotel, 201

    def delete(self, hotel_id):
        global hotels
        hotels = [hotel for hotel in hotels if hotel['hotel_id'] != hotel_id]
        return {'message': 'Hotel Deleted'}

    def findHotel(hotel_id):
        for hotel in hotels:
            if (hotel['hotel_id'] == hotel_id):
                return hotel
        return None
