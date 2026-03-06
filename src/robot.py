from pyModbusTCP.client import ModbusClient
import utils

SERVER_HOST = "192.168.0.100"
SERVER_PORT = 5020
c = ModbusClient(host=SERVER_HOST, port=SERVER_PORT, auto_open=True, auto_close=True)

JOINT_OFFSET = 776
NUM_JOINTS = 7

joint_addresses = (776, 778, 780, 782, 784, 786, 788)
joint_pos = [0, 0, 0, 0, 0, 0, 0]

tool_addresses = (790, 792, 794)
tool_pos = [0, 0, 0]

def print_positions(positions: list) -> None:
    output_str = []
    index = 1
    for pos in positions:
        output_str.append(f'{index}: {pos:.2f}')
        index = index+1
    print(output_str)

def get_address_positions(addresses: list, positions: list) -> None:
    index = 0
    for address in addresses:
        reg_list = c.read_input_registers(address, 2)
        if reg_list is not None:
            (reg_low, reg_high) = reg_list
            positions[index] = utils.registers_to_float(reg_low, reg_high)
        else:
            print(f'Error: could not read {index+1} position')
            positions[index] = -1
        index = index + 1