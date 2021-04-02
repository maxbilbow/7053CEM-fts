from injector import singleton, inject

from app.database.mongo import Database
from app.model.Booking import Booking
from app.repository.AbstractRepository import AbstractRepository, TableConfig
from config import Config

TABLE = Config.get("database.table.bookings")


@singleton
class BookingRepository(AbstractRepository):

    @staticmethod
    def from_dict(d: dict) -> Booking:
        return Booking.from_dict(d)

    @staticmethod
    def to_dict(te: Booking) -> dict:
        return te.to_dict()

    @inject
    def __init__(self, database: Database):
        super().__init__(database, TableConfig(TABLE))

