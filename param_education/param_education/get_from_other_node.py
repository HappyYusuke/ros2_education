import rclpy
from rclpy.node import Node
from rcl_interfaces.srv import GetParameters

class GetParam(Node):
    def __init__(self):
        super().__init__('get_from_other_node')
        self.param_name = ['final_location', 'location1', 'location2', 'location3', 'start']
        self.param_list = None
        self.param_client = self.create_client(GetParameters, '/set_from_launch_node/get_parameters')
        while not self.param_client.wait_for_service(timeout_sec=0.5):
            self.get_logger().info('Param server not available ...')

    def get_my_param(self):
        req = GetParameters.Request()
        req.names = self.param_name
        future = self.param_client.call_async(req)
        while rclpy.ok():
            rclpy.spin_once(self, timeout_sec=0.5)
            if future.done():
                self.param_list = future.result().values
                break
            self.get_logger().info('Could not get params ...')
        #self.get_logger().info(f'original: {self.param_list}')
        for data in self.param_list:
            param = data.double_array_value
            self.get_logger().info(f"{param}")

def main(args=None):
    rclpy.init(args=args)
    node = GetParam()
    try:
        node.get_my_param()
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()
