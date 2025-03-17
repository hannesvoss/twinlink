import threading

import rclpy

from .device_manager import DeviceManager


class TaskExecutor:
    """ Executes a trained policy on an environment. """

    def __init__(
        self,
        bidirectional=False,
    ):
        self._bidirectional = bidirectional

    def run(self, func):
        """ Run the task execution. """
        if self._bidirectional:
            print("[INFO] Starting ROS2 nodes")
            rclpy.init()
            executor, thread = self._start_ros_nodes(DeviceManager.get_devices())

        print("[INFO] Task execution started")
        return func()

    @staticmethod
    def _start_ros_nodes(nodes: list):
        """ Start both ROS 2 nodes using a MultiThreadedExecutor. """
        executor = rclpy.executors.MultiThreadedExecutor()
        for node in nodes:
            print(f"[INFO] Adding node: {node}")
            executor.add_node(node)

        thread = threading.Thread(target=executor.spin, daemon=True)

    def _sync_to_hardware(self):
        pass
