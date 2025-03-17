class DeviceManager:
    """ Device manager class to register and get devices. """

    _devices = {}

    @classmethod
    def register(cls, device_type=None):
        def decorator(device_class):
            key = device_type or device_class.__name__
            cls._devices[key] = device_class
            return device_class
        return decorator

    @classmethod
    def get_device(cls, device_type):
        return cls._devices.get(device_type)

    @classmethod
    def get_devices(cls):
        return list(cls._devices.values())