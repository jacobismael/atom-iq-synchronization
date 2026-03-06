from pyModbusTCP.client import ModbusClient
import time
import logging
import robot
import sys

if('-debug' in sys.argv or '-d' in sys.argv):
    logging.basicConfig()
    logging.getLogger('pyModbusTCP.client').setLevel(logging.DEBUG)

if __name__ == '__main__':
    robot.get_joint_positions()
    while True:
        robot.get_joint_positions()
        robot.print_joint_positions()
        time.sleep(1)
