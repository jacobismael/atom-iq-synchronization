from pyModbusTCP.client import ModbusClient
import time
import logging
import robot

logging.basicConfig()
logging.getLogger('pyModbusTCP.client').setLevel(logging.DEBUG)

if __name__ == '__main__':
    robot.get_joint_positions()
    while True:
        print(robot.joint_pos)
        time.sleep(1)