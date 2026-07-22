BILLING_UNIT_MINUTES = 30
EMERGENCY_SURCHARGE = 2000

class CommonUtil:
    EQUIPMENT_LABELS = {
        "LASER_CUTTER": "レーザーカッター",
        "GPU_SERVER": "GPUサーバ",
        "MOTION_CAPTURE": "モーションキャプチャ",
    }

    USER_LABELS = {
        "STUDENT": "学生",
        "STAFF": "教職員",
        "EXTERNAL": "学外利用者",
    }

    EQUIPMENT_HOURLY_RATES = {
        "LASER_CUTTER": 1200,
        "GPU_SERVER": 2000,
        "MOTION_CAPTURE": 5000,
    }

    USER_MULTIPLIERS = {
        "STUDENT": 0.5,
        "STAFF": 0.8,
        "EXTERNAL": 1.5,
    }

    @staticmethod
    def empty(value):
        return value is None or value.strip() == ""

    @staticmethod
    def calculate_fee(
        user_type,
        equipment_type,
        start_at,
        end_at,
        emergency,
    ):
        if equipment_type not in CommonUtil.EQUIPMENT_HOURLY_RATES:
            raise ValueError(
                f"unknown equipment type: {equipment_type}"
            )

        if user_type not in CommonUtil.USER_MULTIPLIERS:
            raise ValueError(
                f"unknown user type: {user_type}"
            )

        hourly_rate = CommonUtil.EQUIPMENT_HOURLY_RATES[
            equipment_type
        ]
        multiplier = CommonUtil.USER_MULTIPLIERS[user_type]

        total_seconds = (end_at - start_at).total_seconds()
        billing_unit_seconds = BILLING_UNIT_MINUTES * 60

        units = math.ceil(
            total_seconds / billing_unit_seconds
        )

        units_per_hour = 60 / BILLING_UNIT_MINUTES

        result = int(
            hourly_rate
            * (units / units_per_hour)
            * multiplier
        )

        if emergency:
            result += EMERGENCY_SURCHARGE

        return result

    @staticmethod
    def equipment_label(equipment_type):
        return CommonUtil.EQUIPMENT_LABELS.get(
            equipment_type,
            "不明な設備",
        )

    @staticmethod
    def user_label(user_type):
        return CommonUtil.USER_LABELS.get(
            user_type,
            "不明な利用者",
        )