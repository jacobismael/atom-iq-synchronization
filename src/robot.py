from pyModbusTCP.client import ModbusClient
import utils
from utils import Status, State
import logging
from address import *

SERVER_HOST = "192.168.0.100"
SERVER_PORT = 5020
client = ModbusClient(
    host=SERVER_HOST, 
    port=SERVER_PORT, 
    auto_open=True, 
    auto_close=True
)

def print_positions(positions: list) -> None:
    output_str = []
    index = 1
    for pos in positions:
        output_str.append(f'{index}: {pos:.2f}')
        index = index+1
    print(output_str)

def get_address_positions(addresses: list[int]) -> list:
    positions = []
    for address in addresses:
        reg_list = client.read_input_registers(address, 2)
        if reg_list is not None:
            (reg_low, reg_high) = reg_list
            positions.append(utils.registers_to_float(reg_low, reg_high))
        else:
            logging.debug(f'Error: could not read position')
            positions.append(-1)
    return positions

def write_addresses(addresses: list[int], values: list[float]) -> Status:
    for address, value in zip(addresses, values):
        (reg_low, reg_high) = list(utils.float_to_registers(values[value]))
        logging.debug(f'Debug: Address:{address}, value: {value}')
        if not client.write_single_registers(address, reg_low):
            logging.error(f'Error: could not write {address} register')
            return Status.ERROR
        logging.debug(f'Debug: Address:{address+1}, value: {value+1}')
        if not client.write_single_registers(address+1, reg_high):
            logging.error(f'Error: could not write {address+1} register')
            return Status.ERROR
    return Status.SUCCESS

def move_joint_position(joints: list) -> None:
    if not write_addresses(command_value_addresses, joints):
        logging.debug("Error: Couldn't write to command argument registers. Aborting command")
    write_addresses(command_address, [1])

def move_tool_position(x , y, z, roll = 0.0, pitch = 0.0, yaw = 0.0) -> Status:
    # TODO: implement limiters
    args = [x, y, z, roll, pitch, yaw]
    if not write_addresses(command_value_addresses, args):
        logging.error("Error: Couldn't write to command argument registers. Aborting command")
        return Status.ERROR
    client.write_single_register(command_address, 2)
    logging.debug(f'Debug: cmdreg: {client.read_input_registers(command_address)}')
    logging.debug(f'Debug: status: {client.read_input_registers(1039)}')
    return Status.SUCCESS
