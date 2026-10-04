# Benchy Gazebo Simulation

A ROS 2 (Jazzy) and Gazebo (Harmonic) simulation package for the classic 3D-printing Benchy, managed entirely via [Pixi](https://pixi.sh/latest/). 

## Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/shonarun/benchy_ws.git
cd benchy_ws
```

### 2. Enter the Pixi Environment
```bash
pixi shell
```

### 3. Build the Workspace
```bash
colcon build
```

### 4. Source and Launch
```bash
source install/setup.bash
ros2 launch benchy_description benchy.launch.py
```