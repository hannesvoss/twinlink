from rclpy.node import Node

class Device(Node):
    """ Base class for ROS2 devices. """

    def __init__(self, name: str, namespace: str = None):
        self.name = name
        self.namespace = namespace

    def get_name(self) -> str:
        return self.name

    def get_namespace(self) -> str:
        return self.namespace

    def get_fully_qualified_name(self) -> str:
        if self.namespace:
            return f"{self.namespace}/{self.name}"
        return self.name

    def get_fully_qualified_topic_name(self, topic_name: str) -> str:
        return f"{self.get_fully_qualified_name()}/{topic_name}"

    def get_fully_qualified_service_name(self, service_name: str) -> str:
        return f"{self.get_fully_qualified_name()}/{service_name}"

    def get_fully_qualified_parameter_name(self, parameter_name: str) -> str:
        return f"{self.get_fully_qualified_name()}/{parameter_name}"

    def create_subscription(self, msg_type, topic_name, callback, qos_profile):
        pass

    def create_publisher(self, msg_type, topic_name, qos_profile):
        pass
