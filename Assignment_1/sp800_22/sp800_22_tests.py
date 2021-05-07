#!/usr/bin/env python

# sp800_22_tests.py
# 
# Copyright (C) 2017 David Johnston
# This program is distributed under the terms of the GNU General Public License.
# 
# This file is part of sp800_22_tests.
# 
# sp800_22_tests is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# sp800_22_tests is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with sp800_22_tests.  If not, see <http://www.gnu.org/licenses/>.

from __future__ import print_function

import argparse
import sys


import argparse

parser = argparse.ArgumentParser(description='Test data for distinguishability form random, using NIST SP800-22Rev1a algorithms.')
parser.add_argument('filename', type=str, nargs='?', help='Filename of binary file to test')
parser.add_argument('--be', action='store_false',help='Treat data as big endian bits within bytes. Defaults to little endian')
parser.add_argument('-t', '--testname', default=None,help='Select the test to run. Defaults to running all tests. Use --list_tests to see the list')
parser.add_argument('--list_tests', action='store_true',help='Display the list of tests')

args = parser.parse_args()

bigendian = args.be
filename = args.filename

# X 3.1  Frequency (Monobits) Test
# X 3.2  Frequency Test within a Block
# X 3.3  Runs Test
# X 3.4  Test for the Longest Run of Ones in a Block
# X 3.5  Binary Matrix Rank Test
# X 3.6  Discrete Fourier Transform (Specral) Test
# X 3.7  Non-Overlapping Template Matching Test
# X 3.8  Overlapping Template Matching Test
# X 3.9  Maurers Universal Statistical Test
# X 3.10 Linear Complexity Test
# X 3.11 Serial Test
# X 3.12 Approximate Entropy Test
# X 3.13 Cumulative Sums Test
# X 3.14 Random Excursions Test
# X 3.15 Random Excursions Variant Test 


testlist = [
        'monobit_test',
        'frequency_within_block_test',
        'runs_test',
        'longest_run_ones_in_a_block_test',
        'binary_matrix_rank_test',
        'dft_test',
        'non_overlapping_template_matching_test',
        'overlapping_template_matching_test',
        'maurers_universal_test',
        'linear_complexity_test',
        'serial_test',
        'approximate_entropy_test',
        'cumulative_sums_test',
        'random_excursion_test',
        'random_excursion_variant_test']

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

    def von_neumann_pp(self, inputstring):
        it = iter(inputstring)
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

gotresult=False
if args.testname:
    if args.testname in testlist:    
        m = __import__ ("sp800_22_"+args.testname)
        func = getattr(m,args.testname)
        print("TEST: %s" % args.testname)
        success,p,plist = func(bits)
        gotresult = True
        if success:
            print("PASS")
        else:
            print("FAIL")
 
        if p:
            print("P="+str(p))

        if plist:
            for pval in plist:
                print("P="+str(pval))
    else:
        print("Test name (%s) not known" % args.ttestname)
        exit()
else:
    results = list()
    
    for testname in testlist:
        print("TEST: %s" % testname)
        m = __import__ ("sp800_22_"+testname)
        func = getattr(m,testname)
        
        (success,p,plist) = func(bits)

        summary_name = testname
        if success:
            print("  PASS")
            summary_result = "PASS"
        else:
            print("  FAIL")
            summary_result = "FAIL"
        
        if p != None:
            print("  P="+str(p))
            summary_p = str(p)
            
        if plist != None:
            for pval in plist:
                print("P="+str(pval))
            summary_p = str(min(plist))
        
        results.append((summary_name,summary_p, summary_result))
        
    print()
    print("SUMMARY")
    print("-------")
    
    for result in results:
        (summary_name,summary_p, summary_result) = result
        print(summary_name.ljust(40),summary_p.ljust(18),summary_result)
    
