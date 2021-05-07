
from collections import deque


class PRNG:

    def decimalToBinary(self, n):
        return bin(n).replace("0b", "")

    def string_to_bitstring(self, string):
        byte_arr = list()
        for i in string:
            if i == '1':
                byte_arr.append(1)
            else:
                byte_arr.append(0)
        binary_format = bytearray(byte_arr)
        return binary_format

    def __init__(self, seed=0):
        """
        Sets up the internal state of the prng with a seed modulus 1024
        """
        seed = seed % 1024
        bit_string = self.decimalToBinary(seed)
        zero_string = [0 for i in range(10)]
        for i in range(len(bit_string)):
            if bit_string[i] == '1':
                zero_string[i] = 1
        self.internal_state = deque(list(zero_string))

    def get_random_bits(self, number=4):
        output = ''
        for _ in range(number):
            output = output + str(self.internal_state[9])
            first_xor = self.internal_state[7] ^ self.internal_state[9]
            second_xor = first_xor ^ self.internal_state[4]
            third_xor = second_xor ^ self.internal_state[3]
            self.internal_state.rotate()
            self.internal_state[0] = third_xor

        output = self.von_neumann_pp(output)
        return self.string_to_bitstring(output)

    @staticmethod
    def von_neumann_pp(input_string):
        it = iter(input_string)
        outputstring = ''
        for x in it:
            res = (x, next(it))
            if res == ('0', '0') or res == ('1', '1'):
                continue
            else:
                outputstring = outputstring + res[0]
        return outputstring


prng = PRNG(899)
bits = prng.get_random_bits(10000)
print(bits)
