import os
from ament_index_python.packages import get_package_share_directory
import launch
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    # yamlファイルまでのパス
    config = os.path.join(
            get_package_share_directory('param_education'),
            'config',
            'test_navi_map.yaml'
            )
    
    return LaunchDescription([
        Node(
            package='param_education',
            executable='set_from_launch_node',
            parameters=[config],  # yamlファイルからパラメータを設定
            output='screen')
        ])
