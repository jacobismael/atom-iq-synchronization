from pyModbusTCP.utils import decode_ieee, encode_ieee, word_list_to_long, long_list_to_word

def registers_to_float(reg1: int, reg2: int) -> float:
    """Combines reg1 (low) and reg2 (high) into a float."""
    long_list = word_list_to_long([reg1, reg2], big_endian=False)
    return decode_ieee(long_list[0])

def float_to_registers(value: float) -> tuple[int, int]:
    """Splits a float into reg1 (low) and reg2 (high)."""
    val_int = encode_ieee(value)
    word_list = long_list_to_word([val_int], big_endian=False)
    return word_list[0], word_list[1]