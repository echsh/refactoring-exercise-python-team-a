import unittest

from lab_reservation.models import ReservationData
from lab_reservation.repository import InMemoryReservationRepository
from datetime import datetime


class InMemoryReservationRepositoryTest(unittest.TestCase):
    def setUp(self):
        self.repository = InMemoryReservationRepository()

    def test_find_by_id_returns_saved_reservation(self):
        saved = reservation("R-0001")
        self.repository.save(saved)

        result = self.repository.find_by_id("R-0001")

        self.assertIs(saved, result)

    def test_find_by_id_returns_none_for_unknown_id(self):
        result = self.repository.find_by_id("R-9999")

        self.assertIsNone(result)

    def test_find_all_preserves_save_order(self):
        first = reservation("R-0001")
        second = reservation("R-0002")
        self.repository.save(first)
        self.repository.save(second)

        result = self.repository.find_all()

        self.assertEqual([first, second], result)

    def test_find_all_returns_independent_list(self):
        saved = reservation("R-0001")
        self.repository.save(saved)

        result = self.repository.find_all()
        result.clear()

        self.assertEqual([saved], self.repository.find_all())


def reservation(reservation_id):
    return ReservationData(
        reservation_id=reservation_id,
        user_id="s001",
        user_name="テストユーザー",
        user_type="STUDENT",
        equipment_code="gpu-01",
        equipment_name="GPUサーバ",
        equipment_type="GPU_SERVER",
        start_at=datetime(2026, 7, 20, 10, 0),
        end_at=datetime(2026, 7, 20, 11, 0),
    )


if __name__ == "__main__":
    unittest.main()