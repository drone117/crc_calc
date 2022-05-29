# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import zlib


def calc(data, poly, filler):
    """Calculate the CRC remainder of a string of bits using a chosen polynomial.
    initial_filler should be '1' or '0'.
    """
    polynomial_bitstring = poly.lstrip('0')
    len_input = len(data)
    initial_padding = (len(polynomial_bitstring) - 1) * filler
    input_padded_array = list(data + initial_padding)
    while '1' in input_padded_array[:len_input]:
        cur_shift = input_padded_array.index('1')
        for i in range(len(polynomial_bitstring)):
            input_padded_array[cur_shift + i] \
            = str(int(polynomial_bitstring[i] != input_padded_array[cur_shift + i]))
    return ''.join(input_padded_array)[len_input:]



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #calc(b'PyCharm')
    poly = 0x04C11DB7
    poly ='0100110000010001110110110111'
    filler = '0'
    file = open('test.txt')
    input_string = file.read()
    data = (''.join(format(ord(x), 'b') for x in input_string))
    print(data)
    result = calc(data, poly, filler)
    print(result)
    result_int = int(result, 2)
    result_hex = hex(result_int)
    print(result_hex)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
