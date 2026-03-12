from pyModbusTCP.client import ModbusClient
import time
import logging
# import robot
import sys
import os
import argparse

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Process some arguments.")
    parser.add_argument(
        '-c', '--coords',
        type=int,
        nargs=3,
        help='Move robot to coordinates <x,y,z>',
        required=False
    )

    parser.add_argument(
        '-d', '--debug',
        action='store_true',
        help='Enable debugging log',
        required=False
    )

    args = parser.parse_args()

    if args.debug:
        logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
        logging.getLogger('pyModbusTCP.client').setLevel(logging.DEBUG)
        logging.debug("Enabled Debugging Mode")


    if args.coords:
        logging.debug(f"X: {args.coords[0]}, Y: {args.coords[1]}, Z: {args.coords[2]}")
    else:
        logging.debug("No coordinates provided, using default behavior.")

    

    # robot.get_address_positions(robot.tool_addresses, robot.tool_pos)
    # robot.print_positions(robot.tool_pos)
    # robot.get_address_positions(robot.joint_addresses, robot.joint_pos)
    # robot.print_positions(robot.joint_pos)
    # time.sleep(1)

    # robot.move_tool_position(0, 0.5, 1)
