class ReservationRepository:
    def save(self, reservation):
        raise NotImplementedError

    def find_by_id(self, reservation_id):
        raise NotImplementedError

    def find_all(self):
        raise NotImplementedError


class InMemoryReservationRepository(ReservationRepository):
    def __init__(self):
        self.data = {}

    def save(self, reservation):
        self.data[reservation.reservation_id] = reservation

    def find_by_id(self, reservation_id):
        return self.data.get(reservation_id)

    def find_all(self):
        return list(self.data.values())
