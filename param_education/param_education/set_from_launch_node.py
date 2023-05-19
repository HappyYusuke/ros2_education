import rclpy
from rclpy.node import Node

class ParamNode(Node):
    def __init__(self):
        super().__init__('set_from_launch_node')
        self.declare_parameters(
            namespace='',
            parameters=[
                ('final_location', rclpy.Parameter.Type.DOUBLE_ARRAY),
                ('location1', rclpy.Parameter.Type.DOUBLE_ARRAY),
                ('location2', rclpy.Parameter.Type.DOUBLE_ARRAY),
                ('location3', rclpy.Parameter.Type.DOUBLE_ARRAY),
                ('start', rclpy.Parameter.Type.DOUBLE_ARRAY)
            ])

    def get_my_param(self):
        param_list = None
        while not self.has_parameter('final_location'):
            self.get_logger().info('Could not get params ...')
            rclpy.spin_once(self, timeout_sec=0.5)
        param_list = self.get_parameters(['final_location', 'location1', 'location2', 'location3', 'start'])
        if param_list:
            for data in param_list:
                param = data.value
                self.get_logger().info(f"{param}")

def main(args=None):
    rclpy.init(args=args)
    node = ParamNode()
    try:
        #node.get_my_param()
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()
