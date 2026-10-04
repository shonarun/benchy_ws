import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import ExecuteProcess, AppendEnvironmentVariable
from launch_ros.actions import Node

def generate_launch_description():
    pkg_share = get_package_share_directory('benchy_description')
    urdf_file = os.path.join(pkg_share, 'urdf', 'benchy.urdf')

    with open(urdf_file, 'r') as infp:
        robot_desc = infp.read()

    set_env = AppendEnvironmentVariable(
        name='GZ_SIM_RESOURCE_PATH',
        value=os.path.join(pkg_share, '..')
    )

    rsp = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[{'robot_description': robot_desc}]
    )

    gz_server = ExecuteProcess(
        cmd=['gz', 'sim', '-s', '-r', 'empty.sdf'],
        output='screen'
    )

    gz_gui = ExecuteProcess(
        cmd=['gz', 'sim', '-g'],
        output='screen'
    )

    spawn_entity = Node(
        package='ros_gz_sim',
        executable='create',
        arguments=[
            '-topic', 'robot_description',
            '-name', 'benchy'
        ],
        output='screen'
    )

    return LaunchDescription([
        set_env,
        rsp,
        gz_server,
        gz_gui,
        spawn_entity
    ])