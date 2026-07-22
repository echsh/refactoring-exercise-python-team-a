from datetime import datetime

from .models import EquipmentData, UserData
from .notification import RecordingNotificationService
from .repository import InMemoryReservationRepository
from .reservation_manager import ReservationManager


def main():
    repository = InMemoryReservationRepository()
    notification = RecordingNotificationService()
    manager = ReservationManager(repository, notification)

    student = UserData(
        id="u001",
        name="山田花子",
        type="STUDENT",
        training_completed=True,
    )

    gpu = EquipmentData(
        code="gpu-01",
        name="GPU Server 01",
        type="GPU_SERVER",
        active=True,
    )

    reservation = manager.reserve(
        student,
        gpu,
        datetime(2026, 7, 20, 13, 0),
        datetime(2026, 7, 20, 14, 20),
        True,
        False,
    )

    print(manager.make_summary(reservation, True))
    print(notification.sent_messages)


if __name__ == "__main__":
    main()
