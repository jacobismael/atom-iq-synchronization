from pyModbusTCP.client import ModbusClient
import utils
from address import *

SERVER_HOST = "192.168.0.100"
SERVER_PORT = 5020
c = ModbusClient(host=SERVER_HOST, port=SERVER_PORT, auto_open=True, auto_close=True)

def print_positions(positions: list) -> None:
    output_str = []
    index = 1
    for pos in positions:
        output_str.append(f'{index}: {pos:.2f}')
        index = index+1
    print(output_str)

def get_address_positions(addresses: list[int], positions: list) -> None:
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

def write_addresses(addresses: list[int], values: list[float]) -> bool:
    value = 0
    for address in addresses:
        reg_list = list(utils.float_to_registers(values[value]))
        if not c.write_multiple_registers(address, reg_list) or c.read_input_registers([1039], 1) is 0:
            print(f'Error: could not write {address} register')
            return False
        value = value + 1
        # end of arguments
        if(value == len(values)):
            break
        return True

def move_joint_position(joints: list) -> None:
    if not write_addresses(command_value_addresses, joints):
        print("Error: Couldn't write to command argument registers. Aborting command")
    write_addresses(command_address, [1])

def move_tool_position(x , y, z, roll = 0.0, pitch = 0.0, yaw = 0.0) -> None:
    # TODO: implement limiters
    args = [x, y, z, roll, pitch, yaw]
    if not write_addresses(command_value_addresses, args):
        print("Error: Couldn't write to command argument registers. Aborting command")
    write_addresses(command_address, [2])