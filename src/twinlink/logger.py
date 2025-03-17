class Logger:
    """ this class will be used to log all changes on the ground truth state of the connected ROS devices """

    def __init__(self):
        self._log = []

    def log(self, device, state):
        self._log.append((device, state))

    def get_log(self):
        return self._log
