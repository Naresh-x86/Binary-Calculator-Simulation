# Button functions for binary calculator operations
import numpy as np

# Global state variables
operand_a = np.uint8(0)  # 8-bit operand A
operand_b = np.uint8(0)  # 8-bit operand B  
result = np.uint16(0)    # 16-bit result

# Track current bit positions for operands (0-7, left to right)
operand_a_bits = 0  # Number of bits currently set in operand A
operand_b_bits = 0  # Number of bits currently set in operand B

def get_calculator_state():
    """Get current state for LED display"""
    return operand_a, operand_b, result

def del_row1():
    """Delete Row 1 (Clear first 8-bit input)"""
    global operand_a, operand_a_bits
    operand_a = np.uint8(0)
    operand_a_bits = 0
    print(f"Cleared Row 1: {format(operand_a, '08b')}")

def del_row2():
    """Delete Row 2 (Clear second 8-bit input)"""
    global operand_b, operand_b_bits
    operand_b = np.uint8(0)
    operand_b_bits = 0
    print(f"Cleared Row 2: {format(operand_b, '08b')}")

def append_1_row1():
    """Append 1 to Row 1"""
    global operand_a, operand_a_bits
    if operand_a_bits < 8:
        operand_a = np.left_shift(operand_a, 1)
        operand_a = np.bitwise_or(operand_a, np.uint8(1))
        operand_a_bits += 1
        print(f"Appended 1 to Row 1: {format(operand_a, '08b')}")

def append_0_row1():
    """Append 0 to Row 1"""
    global operand_a, operand_a_bits
    if operand_a_bits < 8:
        operand_a = np.left_shift(operand_a, 1)
        operand_a_bits += 1
        print(f"Appended 0 to Row 1: {format(operand_a, '08b')}")

def append_1_row2():
    """Append 1 to Row 2"""
    global operand_b, operand_b_bits
    if operand_b_bits < 8:
        operand_b = np.left_shift(operand_b, 1)
        operand_b = np.bitwise_or(operand_b, np.uint8(1))
        operand_b_bits += 1
        print(f"Appended 1 to Row 2: {format(operand_b, '08b')}")

def append_0_row2():
    """Append 0 to Row 2"""
    global operand_b, operand_b_bits
    if operand_b_bits < 8:
        operand_b = np.left_shift(operand_b, 1)
        operand_b_bits += 1
        print(f"Appended 0 to Row 2: {format(operand_b, '08b')}")

def del_output():
    """Delete All Output (Clear result)"""
    global result
    result = np.uint16(0)
    print(f"Cleared Output: {format(result, '016b')}")

def not_output():
    """NOT Operation (Bitwise NOT on result)"""
    global result
    result = np.bitwise_not(result)
    print(f"NOT Output: {format(result, '016b')}")

def and_op():
    """AND Operation (Bitwise AND)"""
    global result
    result = np.bitwise_and(np.uint16(operand_a), np.uint16(operand_b))
    print(f"AND: {format(operand_a, '08b')} & {format(operand_b, '08b')} = {format(result, '016b')}")

def or_op():
    """OR Operation (Bitwise OR)"""
    global result
    result = np.bitwise_or(np.uint16(operand_a), np.uint16(operand_b))
    print(f"OR: {format(operand_a, '08b')} | {format(operand_b, '08b')} = {format(result, '016b')}")

def xor_op():
    """XOR Operation (Bitwise XOR)"""
    global result
    result = np.bitwise_xor(np.uint16(operand_a), np.uint16(operand_b))
    print(f"XOR: {format(operand_a, '08b')} ^ {format(operand_b, '08b')} = {format(result, '016b')}")

def mod_op():
    """MOD Operation (Modulo)"""
    global result
    if operand_b != 0:
        result = np.uint16(operand_a % operand_b)
        print(f"MOD: {operand_a} % {operand_b} = {result} ({format(result, '016b')})")
    else:
        print("MOD: Division by zero!")

def add_op():
    """ADD Operation"""
    global result
    result = np.uint16(operand_a) + np.uint16(operand_b)
    print(f"ADD: {operand_a} + {operand_b} = {result} ({format(result, '016b')})")

def div_op():
    """DIV Operation (Division)"""
    global result
    if operand_b != 0:
        result = np.uint16(operand_a // operand_b)
        print(f"DIV: {operand_a} // {operand_b} = {result} ({format(result, '016b')})")
    else:
        print("DIV: Division by zero!")

def sub_op():
    """SUB Operation (Subtraction)"""
    global result
    # Handle underflow by converting to signed, then back to unsigned
    temp_result = int(operand_a) - int(operand_b)
    if temp_result < 0:
        result = np.uint16(65536 + temp_result)  # Two's complement for 16-bit
    else:
        result = np.uint16(temp_result)
    print(f"SUB: {operand_a} - {operand_b} = {result} ({format(result, '016b')})")

def mult_op():
    """MULT Operation (Multiplication)"""
    global result
    result = np.uint16(operand_a) * np.uint16(operand_b)
    print(f"MULT: {operand_a} * {operand_b} = {result} ({format(result, '016b')})")
