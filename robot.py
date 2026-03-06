from pyModbusTCP.client import ModbusClient
import utils

SERVER_HOST = "127.0.0.1"
SERVER_PORT = 502
c = ModbusClient(host=SERVER_HOST, port=SERVER_PORT, auto_open=True, auto_close=True)

JOINT_OFFSET = 776
NUM_JOINTS = 7

joint_addresses = (776, 778, 780, 782, 784, 786, 788)
joint_pos = [0, 0, 0, 0, 0, 0, 0]

def get_joint_positions() -> tuple:
    joint = 0
    for address in joint_addresses:
        reg_list = c.read_input_registers(address, 2)
        if reg_list is not None:
            (reg_low, reg_high) = reg_list
            joint_pos[joint] = utils.registers_to_float(reg_low, reg_high)
        else:
            print(f'Error: could not read joint {joint+1} position')
            joint_pos[joint] = -1
        joint = joint + 1
