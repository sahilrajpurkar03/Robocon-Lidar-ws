import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/rajpurkar/Isaac_Project/Robocon-Lidar-ws/install/summit_joystick_control'
