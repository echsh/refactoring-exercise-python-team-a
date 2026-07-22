class UserData:
    VALID_TYPES = {"STUDENT", "STAFF", "EXTERNAL"}

    def __init__(self, id, name, type, training_completed=False, suspended=False, penalty_points=0,):
        if not isinstance(id, str) or id.strip() == "":
            raise ValueError("id must be a non-empty string")

        if not isinstance(name, str) or name.strip() == "":
            raise ValueError("name must be a non-empty string")

        if type not in self.VALID_TYPES:
            raise ValueError(f"unknown user type: {type}")

        if not isinstance(training_completed, bool):
            raise TypeError("training_completed must be bool")

        if not isinstance(suspended, bool):
            raise TypeError("suspended must be bool")

        if (
            not isinstance(penalty_points, int)
            or isinstance(penalty_points, bool)
            or penalty_points < 0
        ):
            raise ValueError("penalty_points must be a non-negative integer")

        self.id = id
        self.name = name
        self.type = type
        self.training_completed = training_completed
        self.suspended = suspended
        self.penalty_points = penalty_points


class EquipmentData:
    VALID_TYPES = {"LASER_CUTTER", "GPU_SERVER", "MOTION_CAPTURE",}

    def __init__(self, code, name, type, active=False,):
        if not isinstance(code, str) or code.strip() == "":
            raise ValueError("code must be a non-empty string")

        if not isinstance(name, str) or name.strip() == "":
            raise ValueError("name must be a non-empty string")

        if type not in self.VALID_TYPES:
            raise ValueError(f"unknown equipment type: {type}")

        if not isinstance(active, bool):
            raise TypeError("active must be bool")

        self.code = code
        self.name = name
        self.type = type
        self.active = active


class ReservationData:
    VALID_USER_TYPES = UserData.VALID_TYPES
    VALID_EQUIPMENT_TYPES = EquipmentData.VALID_TYPES

    def __init__(
        self,
        reservation_id,
        user_id,
        user_name,
        user_type,
        equipment_code,
        equipment_name,
        equipment_type,
        start_at,
        end_at,
        emergency=False,
        status="RESERVED",
        fee=0,
        cancellation_fee=0,
    ):
        if (
            user_id is None
            or user_id.strip() == ""
            or user_name is None
            or user_name.strip() == ""
            or user_type is None
            or user_type.strip() == ""
        ):
            raise ValueError("invalid user")

        if user_type not in self.VALID_USER_TYPES:
            raise ValueError(f"unknown user type: {user_type}")

        if (
            equipment_code is None
            or equipment_code.strip() == ""
            or equipment_name is None
            or equipment_name.strip() == ""
            or equipment_type is None
            or equipment_type.strip() == ""
        ):
            raise ValueError("invalid equipment")

        if equipment_type not in self.VALID_EQUIPMENT_TYPES:
            raise ValueError(f"unknown equipment type: {equipment_type}")

        if start_at is None or end_at is None:
            raise ValueError("start and end are required")

        if end_at <= start_at:
            raise ValueError("end must be after start")

        if start_at.date() != end_at.date():
            raise ValueError("reservation must be within one day")

        self.reservation_id = reservation_id
        self.user_id = user_id
        self.user_name = user_name
        self.user_type = user_type
        self.equipment_code = equipment_code
        self.equipment_name = equipment_name
        self.equipment_type = equipment_type
        self.start_at = start_at
        self.end_at = end_at
        self.emergency = emergency
        self.status = status
        self.fee = fee
        self.cancellation_fee = cancellation_fee
