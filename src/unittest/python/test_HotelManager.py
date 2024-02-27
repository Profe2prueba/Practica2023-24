import datetime
from unittest import TestCase
from src.main.python.UC3MTravel.HotelManager import HotelManager

class TestRoomReservation(TestCase):

    def test_room_reservation_valid1(self):
        my_reservation=HotelManager()
        value= my_reservation.room_reservation(credit_card="5105105105105100",
                                               name_surname="Jhon Doe",
                                               id_Card="12345",phone_number="123456789",
                                               room_type="double",
                                               arrival_date="21/03/2024",num_days="2")
        print (value)
        self.assertEqual(value,"fb063bf9e1988aba5fb6d62cce0c417c")


