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
    def __init__(self):
        self.reservation_id = None
        self.user_id = None
        self.user_name = None
        self.user_type = None
        self.equipment_code = None
        self.equipment_name = None
        self.equipment_type = None
        self.start_at = None
        self.end_at = None
        self.emergency = False
        self.status = None
        self.fee = 0
        self.cancellation_fee = 0
