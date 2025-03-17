class SafetyManager:
    """ Safety manager class to register and get safety checks. """

    _safety_checks = {}

    @classmethod
    def register(cls, safety_check_type=None):
        def decorator(safety_check_class):
            key = safety_check_type or safety_check_class.__name__
            cls._safety_checks[key] = safety_check_class
            return safety_check_class
        return decorator

    @classmethod
    def get_safety_check(cls, safety_check_type):
        return cls._safety_checks.get(safety_check_type)

    @classmethod
    def get_safety_checks(cls):
        return list(cls._safety_checks.values())