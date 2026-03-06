from pyModbusTCP.client import ModbusClient
import time
import logging
import robot
import sys
import os

if('-debug' in sys.argv or '-d' in sys.argv):
    logging.basicConfig()
    logging.getLogger('pyModbusTCP.client').setLevel(logging.DEBUG)

if __name__ == '__main__':
    while True:
        robot.get_address_positions(robot.tool_addresses, robot.tool_pos)
        robot.print_positions(robot.tool_pos)
        robot.get_address_positions(robot.joint_addresses, robot.joint_pos)
        robot.print_positions(robot.joint_pos)
        os.system('clear')
        time.sleep(1)
