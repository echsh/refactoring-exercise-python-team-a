BILLING_UNIT_MINUTES = 30
EMERGENCY_SURCHARGE = 2000

LASER_CUTTER_HOURLY_RATE = 1200
GPU_SERVER_HOURLY_RATE = 2000
MOTION_CAPTURE_HOURLY_RATE = 5000

STUDENT_FEE_MULTIPLIER = 0.5
STAFF_FEE_MULTIPLIER = 0.8
EXTERNAL_FEE_MULTIPLIER = 1.5

class CommonUtil:
    @staticmethod
    def empty(value):
        return value is None or value.strip() == ""

    @staticmethod
    def calculate_fee(user_type, equipment_type, start_at, end_at, emergency):
        total_seconds = int((end_at - start_at).total_seconds())
        unit_seconds = BILLING_UNIT_MINUTES * 60
        units = (total_seconds + unit_seconds - 1) // unit_seconds

        if equipment_type == "LASER_CUTTER":
            hourly_rate = LASER_CUTTER_HOURLY_RATE
        elif equipment_type == "GPU_SERVER":
            hourly_rate = GPU_SERVER_HOURLY_RATE
        elif equipment_type == "MOTION_CAPTURE":
            hourly_rate = MOTION_CAPTURE_HOURLY_RATE
        else:
            raise ValueError(f"unknown equipment type: {equipment_type}")

        if user_type == "STUDENT":
            multiplier = STUDENT_FEE_MULTIPLIER
        elif user_type == "STAFF":
            multiplier = STAFF_FEE_MULTIPLIER
        elif user_type == "EXTERNAL":
            multiplier = EXTERNAL_FEE_MULTIPLIER
        else:
            raise ValueError(f"unknown user type: {user_type}")

        units_per_hour = 60 / BILLING_UNIT_MINUTES
        result = int(hourly_rate * (units / units_per_hour) * multiplier)
        if emergency:
            result += EMERGENCY_SURCHARGE
        return result

    @staticmethod
    def equipment_label(equipment_type):
        if equipment_type == "LASER_CUTTER":
            return "レーザーカッター"
        if equipment_type == "GPU_SERVER":
            return "GPUサーバ"
        if equipment_type == "MOTION_CAPTURE":
            return "モーションキャプチャ"
        return "不明な設備"

    @staticmethod
    def user_label(user_type):
        if user_type == "STUDENT":
            return "学生"
        if user_type == "STAFF":
            return "教職員"
        if user_type == "EXTERNAL":
            return "学外利用者"
        return "不明な利用者"
