# See LICENSE.iitm for details
# See LICENSE.vyoma for details

import random
import sys
import cocotb
from cocotb.decorators import coroutine
from cocotb.triggers import Timer, RisingEdge
from cocotb.result import TestFailure
from cocotb.clock import Clock

from model_mkbitmanip import *

# Clock Generation
@cocotb.coroutine
def clock_gen(signal):
    while True:
        signal.value <= 0
        yield Timer(1) 
        signal.value <= 1
        yield Timer(1) 

# Sample Test
@cocotb.test()
def run_test(dut):

    # clock
    cocotb.fork(clock_gen(dut.CLK))

    # reset
    dut.RST_N.value <= 0
    yield Timer(10) 
    dut.RST_N.value <= 1

    ######### CTB : Modify the test to expose the bug #############
    # input transaction
    mav_putvalue_src1 = 0x5
    mav_putvalue_src2 = 0x0
    mav_putvalue_src3 = 0x0
    mav_putvalue_instr = 0x101010B3

    # expected output from the model
    expected_mav_putvalue = bitmanip(mav_putvalue_instr, mav_putvalue_src1, mav_putvalue_src2, mav_putvalue_src3)

    # driving the input transaction
    dut.mav_putvalue_src1.value = mav_putvalue_src1
    dut.mav_putvalue_src2.value = mav_putvalue_src2
    dut.mav_putvalue_src3.value = mav_putvalue_src3
    dut.EN_mav_putvalue.value = 1
    dut.mav_putvalue_instr.value = mav_putvalue_instr
  
    yield Timer(1) 

    # obtaining the output
    dut_output = dut.mav_putvalue.value

    cocotb.log.info(f'DUT OUTPUT={hex(dut_output)}')
    cocotb.log.info(f'EXPECTED OUTPUT={hex(expected_mav_putvalue)}')
    
    # comparison
    error_message = f'Value mismatch DUT = {hex(dut_output)} does not match MODEL = {hex(expected_mav_putvalue)}'
    assert dut_output == expected_mav_putvalue, error_message


@cocotb.test()
def run_test_ANDN(dut):

    dut._log.info(f'Running test for ADD Instruction')

    # clock
    cocotb.fork(clock_gen(dut.CLK))

    # reset
    dut.RST_N.value <= 0
    yield Timer(10) 
    dut.RST_N.value <= 1

    ######### CTB : Modify the test to expose the bug #############
    # input transaction
    mav_putvalue_src1 = 0x45
    mav_putvalue_src2 = 0x36
    mav_putvalue_src3 = 0x0
    # My CODE
    desOp = list('0110011')
    desFunc3 = list('111')
    desFunc7 = list('0100000')
    inst = bin(0)[2:0]
    inst = inst.zfill(32)
    instList = list(inst)
    instList[0:7] = desFunc7
    instList[17:20] = desFunc3
    instList[-7::] = desOp
    inst = ''.join(instList)
    mav_putvalue_instr = int(inst,2)

    #mav_putvalue_instr = 0x101010B3

    # expected output from the model
    expected_mav_putvalue = bitmanip(mav_putvalue_instr, mav_putvalue_src1, mav_putvalue_src2, mav_putvalue_src3)

    # driving the input transaction
    dut.mav_putvalue_src1.value = mav_putvalue_src1
    dut.mav_putvalue_src2.value = mav_putvalue_src2
    dut.mav_putvalue_src3.value = mav_putvalue_src3
    dut.EN_mav_putvalue.value = 1
    dut.mav_putvalue_instr.value = mav_putvalue_instr
  
    yield Timer(1) 

    # obtaining the output
    dut_output = dut.mav_putvalue.value

    cocotb.log.info(f'DUT OUTPUT={hex(dut_output)}')
    cocotb.log.info(f'EXPECTED OUTPUT={hex(expected_mav_putvalue)}')
    
    # comparison
    error_message = f'TEST CASE FOR ANDN - 1. Value mismatch DUT = {hex(dut_output)} does not match MODEL = {hex(expected_mav_putvalue)}'
    assert dut_output == expected_mav_putvalue, error_message


	


@cocotb.test()
def run_test_ORN(dut):

    dut._log.info(f'Running test for ADD Instruction')

    # clock
    cocotb.fork(clock_gen(dut.CLK))

    # reset
    dut.RST_N.value <= 0
    yield Timer(10) 
    dut.RST_N.value <= 1

    ######### CTB : Modify the test to expose the bug #############
    # input transaction
    mav_putvalue_src1 = 0x45
    mav_putvalue_src2 = 0x36
    mav_putvalue_src3 = 0x0
    # My CODE
    desOp = list('0110011')
    desFunc3 = list('110')
    desFunc7 = list('0100000')
    inst = bin(0)[2:0]
    inst = inst.zfill(32)
    instList = list(inst)
    instList[0:7] = desFunc7
    instList[17:20] = desFunc3
    instList[-7::] = desOp
    inst = ''.join(instList)
    mav_putvalue_instr = int(inst,2)

    #mav_putvalue_instr = 0x101010B3

    # expected output from the model
    expected_mav_putvalue = bitmanip(mav_putvalue_instr, mav_putvalue_src1, mav_putvalue_src2, mav_putvalue_src3)

    # driving the input transaction
    dut.mav_putvalue_src1.value = mav_putvalue_src1
    dut.mav_putvalue_src2.value = mav_putvalue_src2
    dut.mav_putvalue_src3.value = mav_putvalue_src3
    dut.EN_mav_putvalue.value = 1
    dut.mav_putvalue_instr.value = mav_putvalue_instr
  
    yield Timer(1) 

    # obtaining the output
    dut_output = dut.mav_putvalue.value

    cocotb.log.info(f'DUT OUTPUT={hex(dut_output)}')
    cocotb.log.info(f'EXPECTED OUTPUT={hex(expected_mav_putvalue)}')
    
    # comparison
    error_message = f'TEST CASE FOR ORN - 2. Value mismatch DUT = {hex(dut_output)} does not match MODEL = {hex(expected_mav_putvalue)}'
    assert dut_output == expected_mav_putvalue, error_message
	


@cocotb.test()
def run_test_XNOR(dut):

    dut._log.info(f'Running test for ADD Instruction')

    # clock
    cocotb.fork(clock_gen(dut.CLK))

    # reset
    dut.RST_N.value <= 0
    yield Timer(10) 
    dut.RST_N.value <= 1

    ######### CTB : Modify the test to expose the bug #############
    # input transaction
    mav_putvalue_src1 = 0x45
    mav_putvalue_src2 = 0x36
    mav_putvalue_src3 = 0x0
    # My CODE
    desOp = list('0110011')
    desFunc3 = list('100')
    desFunc7 = list('0100000')
    inst = bin(0)[2:0]
    inst = inst.zfill(32)
    instList = list(inst)
    instList[0:7] = desFunc7
    instList[17:20] = desFunc3
    instList[-7::] = desOp
    inst = ''.join(instList)
    mav_putvalue_instr = int(inst,2)

    #mav_putvalue_instr = 0x101010B3

    # expected output from the model
    expected_mav_putvalue = bitmanip(mav_putvalue_instr, mav_putvalue_src1, mav_putvalue_src2, mav_putvalue_src3)

    # driving the input transaction
    dut.mav_putvalue_src1.value = mav_putvalue_src1
    dut.mav_putvalue_src2.value = mav_putvalue_src2
    dut.mav_putvalue_src3.value = mav_putvalue_src3
    dut.EN_mav_putvalue.value = 1
    dut.mav_putvalue_instr.value = mav_putvalue_instr
  
    yield Timer(1) 

    # obtaining the output
    dut_output = dut.mav_putvalue.value

    cocotb.log.info(f'DUT OUTPUT={hex(dut_output)}')
    cocotb.log.info(f'EXPECTED OUTPUT={hex(expected_mav_putvalue)}')
    
    # comparison
    error_message = f'TEST CASE FOR XNOR - 3. Value mismatch DUT = {hex(dut_output)} does not match MODEL = {hex(expected_mav_putvalue)}'
    assert dut_output == expected_mav_putvalue, error_message
	


@cocotb.test()
def run_test_SLO(dut):

    dut._log.info(f'Running test for ADD Instruction')

    # clock
    cocotb.fork(clock_gen(dut.CLK))

    # reset
    dut.RST_N.value <= 0
    yield Timer(10) 
    dut.RST_N.value <= 1

    ######### CTB : Modify the test to expose the bug #############
    # input transaction
    mav_putvalue_src1 = 0x45
    mav_putvalue_src2 = 0x36
    mav_putvalue_src3 = 0x0
    # My CODE
    desOp = list('0110011')
    desFunc3 = list('001')
    desFunc7 = list('0100000')
    inst = bin(0)[2:0]
    inst = inst.zfill(32)
    instList = list(inst)
    instList[0:7] = desFunc7
    instList[17:20] = desFunc3
    instList[-7::] = desOp
    inst = ''.join(instList)
    mav_putvalue_instr = int(inst,2)

    #mav_putvalue_instr = 0x101010B3

    # expected output from the model
    expected_mav_putvalue = bitmanip(mav_putvalue_instr, mav_putvalue_src1, mav_putvalue_src2, mav_putvalue_src3)

    # driving the input transaction
    dut.mav_putvalue_src1.value = mav_putvalue_src1
    dut.mav_putvalue_src2.value = mav_putvalue_src2
    dut.mav_putvalue_src3.value = mav_putvalue_src3
    dut.EN_mav_putvalue.value = 1
    dut.mav_putvalue_instr.value = mav_putvalue_instr
  
    yield Timer(1) 

    # obtaining the output
    dut_output = dut.mav_putvalue.value

    cocotb.log.info(f'DUT OUTPUT={hex(dut_output)}')
    cocotb.log.info(f'EXPECTED OUTPUT={hex(expected_mav_putvalue)}')
    
    # comparison
    error_message = f'TEST CASE FOR SLO - 4. Value mismatch DUT = {hex(dut_output)} does not match MODEL = {hex(expected_mav_putvalue)}'
    assert dut_output == expected_mav_putvalue, error_message


@cocotb.test()
def run_test_SRO(dut):

    dut._log.info(f'Running test for ADD Instruction')

    # clock
    cocotb.fork(clock_gen(dut.CLK))

    # reset
    dut.RST_N.value <= 0
    yield Timer(10) 
    dut.RST_N.value <= 1

    ######### CTB : Modify the test to expose the bug #############
    # input transaction
    mav_putvalue_src1 = 0x45
    mav_putvalue_src2 = 0x36
    mav_putvalue_src3 = 0x0
    # My CODE
    desOp = list('0110011')
    desFunc3 = list('101')
    desFunc7 = list('0100000')
    inst = bin(0)[2:0]
    inst = inst.zfill(32)
    instList = list(inst)
    instList[0:7] = desFunc7
    instList[17:20] = desFunc3
    instList[-7::] = desOp
    inst = ''.join(instList)
    mav_putvalue_instr = int(inst,2)

    #mav_putvalue_instr = 0x101010B3

    # expected output from the model
    expected_mav_putvalue = bitmanip(mav_putvalue_instr, mav_putvalue_src1, mav_putvalue_src2, mav_putvalue_src3)

    # driving the input transaction
    dut.mav_putvalue_src1.value = mav_putvalue_src1
    dut.mav_putvalue_src2.value = mav_putvalue_src2
    dut.mav_putvalue_src3.value = mav_putvalue_src3
    dut.EN_mav_putvalue.value = 1
    dut.mav_putvalue_instr.value = mav_putvalue_instr
  
    yield Timer(1) 

    # obtaining the output
    dut_output = dut.mav_putvalue.value

    cocotb.log.info(f'DUT OUTPUT={hex(dut_output)}')
    cocotb.log.info(f'EXPECTED OUTPUT={hex(expected_mav_putvalue)}')
    
    # comparison
    error_message = f'TEST CASE FOR SRO - 5. Value mismatch DUT = {hex(dut_output)} does not match MODEL = {hex(expected_mav_putvalue)}'
    assert dut_output == expected_mav_putvalue, error_message
	


@cocotb.test()
def run_test_ROL(dut):

    dut._log.info(f'Running test for ADD Instruction')

    # clock
    cocotb.fork(clock_gen(dut.CLK))

    # reset
    dut.RST_N.value <= 0
    yield Timer(10) 
    dut.RST_N.value <= 1

    ######### CTB : Modify the test to expose the bug #############
    # input transaction
    mav_putvalue_src1 = 0x45
    mav_putvalue_src2 = 0x36
    mav_putvalue_src3 = 0x0
    # My CODE
    desOp = list('0110011')
    desFunc3 = list('001')
    desFunc7 = list('0110000')
    inst = bin(0)[2:0]
    inst = inst.zfill(32)
    instList = list(inst)
    instList[0:7] = desFunc7
    instList[17:20] = desFunc3
    instList[-7::] = desOp
    inst = ''.join(instList)
    mav_putvalue_instr = int(inst,2)

    #mav_putvalue_instr = 0x101010B3

    # expected output from the model
    expected_mav_putvalue = bitmanip(mav_putvalue_instr, mav_putvalue_src1, mav_putvalue_src2, mav_putvalue_src3)

    # driving the input transaction
    dut.mav_putvalue_src1.value = mav_putvalue_src1
    dut.mav_putvalue_src2.value = mav_putvalue_src2
    dut.mav_putvalue_src3.value = mav_putvalue_src3
    dut.EN_mav_putvalue.value = 1
    dut.mav_putvalue_instr.value = mav_putvalue_instr
  
    yield Timer(1) 

    # obtaining the output
    dut_output = dut.mav_putvalue.value

    cocotb.log.info(f'DUT OUTPUT={hex(dut_output)}')
    cocotb.log.info(f'EXPECTED OUTPUT={hex(expected_mav_putvalue)}')
    
    # comparison
    error_message = f'TEST CASE FOR ROL - 6. Value mismatch DUT = {hex(dut_output)} does not match MODEL = {hex(expected_mav_putvalue)}'
    assert dut_output == expected_mav_putvalue, error_message

@cocotb.test()
def run_test_ROR(dut):

    dut._log.info(f'Running test for ADD Instruction')

    # clock
    cocotb.fork(clock_gen(dut.CLK))

    # reset
    dut.RST_N.value <= 0
    yield Timer(10) 
    dut.RST_N.value <= 1

    ######### CTB : Modify the test to expose the bug #############
    # input transaction
    mav_putvalue_src1 = 0x45
    mav_putvalue_src2 = 0x36
    mav_putvalue_src3 = 0x0
    # My CODE
    desOp = list('0110011')
    desFunc3 = list('101')
    desFunc7 = list('0110000')
    inst = bin(0)[2:0]
    inst = inst.zfill(32)
    instList = list(inst)
    instList[0:7] = desFunc7
    instList[17:20] = desFunc3
    instList[-7::] = desOp
    inst = ''.join(instList)
    mav_putvalue_instr = int(inst,2)

    #mav_putvalue_instr = 0x101010B3

    # expected output from the model
    expected_mav_putvalue = bitmanip(mav_putvalue_instr, mav_putvalue_src1, mav_putvalue_src2, mav_putvalue_src3)

    # driving the input transaction
    dut.mav_putvalue_src1.value = mav_putvalue_src1
    dut.mav_putvalue_src2.value = mav_putvalue_src2
    dut.mav_putvalue_src3.value = mav_putvalue_src3
    dut.EN_mav_putvalue.value = 1
    dut.mav_putvalue_instr.value = mav_putvalue_instr
  
    yield Timer(1) 

    # obtaining the output
    dut_output = dut.mav_putvalue.value

    cocotb.log.info(f'DUT OUTPUT={hex(dut_output)}')
    cocotb.log.info(f'EXPECTED OUTPUT={hex(expected_mav_putvalue)}')
    
    # comparison
    error_message = f'TEST CASE FOR ROR - 7. Value mismatch DUT = {hex(dut_output)} does not match MODEL = {hex(expected_mav_putvalue)}'
    assert dut_output == expected_mav_putvalue, error_message


@cocotb.test()
def run_test_SH1ADD(dut):

    dut._log.info(f'Running test for ADD Instruction')

    # clock
    cocotb.fork(clock_gen(dut.CLK))

    # reset
    dut.RST_N.value <= 0
    yield Timer(10) 
    dut.RST_N.value <= 1

    ######### CTB : Modify the test to expose the bug #############
    # input transaction
    mav_putvalue_src1 = 0x45
    mav_putvalue_src2 = 0x36
    mav_putvalue_src3 = 0x0
    # My CODE
    desOp = list('0110011')
    desFunc3 = list('010')
    desFunc7 = list('0010000')
    inst = bin(0)[2:0]
    inst = inst.zfill(32)
    instList = list(inst)
    instList[0:7] = desFunc7
    instList[17:20] = desFunc3
    instList[-7::] = desOp
    inst = ''.join(instList)
    mav_putvalue_instr = int(inst,2)

    #mav_putvalue_instr = 0x101010B3

    # expected output from the model
    expected_mav_putvalue = bitmanip(mav_putvalue_instr, mav_putvalue_src1, mav_putvalue_src2, mav_putvalue_src3)

    # driving the input transaction
    dut.mav_putvalue_src1.value = mav_putvalue_src1
    dut.mav_putvalue_src2.value = mav_putvalue_src2
    dut.mav_putvalue_src3.value = mav_putvalue_src3
    dut.EN_mav_putvalue.value = 1
    dut.mav_putvalue_instr.value = mav_putvalue_instr
  
    yield Timer(1) 

    # obtaining the output
    dut_output = dut.mav_putvalue.value

    cocotb.log.info(f'DUT OUTPUT={hex(dut_output)}')
    cocotb.log.info(f'EXPECTED OUTPUT={hex(expected_mav_putvalue)}')
    
    # comparison
    error_message = f'TEST CASE FOR SH1ADD - 8. Value mismatch DUT = {hex(dut_output)} does not match MODEL = {hex(expected_mav_putvalue)}'
    assert dut_output == expected_mav_putvalue, error_message


@cocotb.test()
def run_test_SH2ADD(dut):

    dut._log.info(f'Running test for ADD Instruction')

    # clock
    cocotb.fork(clock_gen(dut.CLK))

    # reset
    dut.RST_N.value <= 0
    yield Timer(10) 
    dut.RST_N.value <= 1

    ######### CTB : Modify the test to expose the bug #############
    # input transaction
    mav_putvalue_src1 = 0x45
    mav_putvalue_src2 = 0x36
    mav_putvalue_src3 = 0x0
    # My CODE
    desOp = list('0110011')
    desFunc3 = list('100')
    desFunc7 = list('0010000')
    inst = bin(0)[2:0]
    inst = inst.zfill(32)
    instList = list(inst)
    instList[0:7] = desFunc7
    instList[17:20] = desFunc3
    instList[-7::] = desOp
    inst = ''.join(instList)
    mav_putvalue_instr = int(inst,2)

    #mav_putvalue_instr = 0x101010B3

    # expected output from the model
    expected_mav_putvalue = bitmanip(mav_putvalue_instr, mav_putvalue_src1, mav_putvalue_src2, mav_putvalue_src3)

    # driving the input transaction
    dut.mav_putvalue_src1.value = mav_putvalue_src1
    dut.mav_putvalue_src2.value = mav_putvalue_src2
    dut.mav_putvalue_src3.value = mav_putvalue_src3
    dut.EN_mav_putvalue.value = 1
    dut.mav_putvalue_instr.value = mav_putvalue_instr
  
    yield Timer(1) 

    # obtaining the output
    dut_output = dut.mav_putvalue.value

    cocotb.log.info(f'DUT OUTPUT={hex(dut_output)}')
    cocotb.log.info(f'EXPECTED OUTPUT={hex(expected_mav_putvalue)}')
    
    # comparison
    error_message = f'TEST CASE FOR SH2ADD - 9. Value mismatch DUT = {hex(dut_output)} does not match MODEL = {hex(expected_mav_putvalue)}'
    assert dut_output == expected_mav_putvalue, error_message


@cocotb.test()
def run_test_SH3ADD(dut):

    dut._log.info(f'Running test for ADD Instruction')

    # clock
    cocotb.fork(clock_gen(dut.CLK))

    # reset
    dut.RST_N.value <= 0
    yield Timer(10) 
    dut.RST_N.value <= 1

    ######### CTB : Modify the test to expose the bug #############
    # input transaction
    mav_putvalue_src1 = 0x45
    mav_putvalue_src2 = 0x36
    mav_putvalue_src3 = 0x0
    # My CODE
    desOp = list('0110011')
    desFunc3 = list('110')
    desFunc7 = list('0010000')
    inst = bin(0)[2:0]
    inst = inst.zfill(32)
    instList = list(inst)
    instList[0:7] = desFunc7
    instList[17:20] = desFunc3
    instList[-7::] = desOp
    inst = ''.join(instList)
    mav_putvalue_instr = int(inst,2)

    #mav_putvalue_instr = 0x101010B3

    # expected output from the model
    expected_mav_putvalue = bitmanip(mav_putvalue_instr, mav_putvalue_src1, mav_putvalue_src2, mav_putvalue_src3)

    # driving the input transaction
    dut.mav_putvalue_src1.value = mav_putvalue_src1
    dut.mav_putvalue_src2.value = mav_putvalue_src2
    dut.mav_putvalue_src3.value = mav_putvalue_src3
    dut.EN_mav_putvalue.value = 1
    dut.mav_putvalue_instr.value = mav_putvalue_instr
  
    yield Timer(1) 

    # obtaining the output
    dut_output = dut.mav_putvalue.value

    cocotb.log.info(f'DUT OUTPUT={hex(dut_output)}')
    cocotb.log.info(f'EXPECTED OUTPUT={hex(expected_mav_putvalue)}')
    
    # comparison
    error_message = f'TEST CASE FOR SH3ADD - 10. Value mismatch DUT = {hex(dut_output)} does not match MODEL = {hex(expected_mav_putvalue)}'
    assert dut_output == expected_mav_putvalue, error_message


@cocotb.test()
def run_test_SBCLR(dut):

    dut._log.info(f'Running test for ADD Instruction')

    # clock
    cocotb.fork(clock_gen(dut.CLK))

    # reset
    dut.RST_N.value <= 0
    yield Timer(10) 
    dut.RST_N.value <= 1

    ######### CTB : Modify the test to expose the bug #############
    # input transaction
    mav_putvalue_src1 = 0x45
    mav_putvalue_src2 = 0x1C
    mav_putvalue_src3 = 0x0
    # My CODE
    desOp = list('0110011')
    desFunc3 = list('001')
    desFunc7 = list('0100100')
    inst = bin(0)[2:0]
    inst = inst.zfill(32)
    instList = list(inst)
    instList[0:7] = desFunc7
    instList[17:20] = desFunc3
    instList[-7::] = desOp
    inst = ''.join(instList)
    mav_putvalue_instr = int(inst,2)

    #mav_putvalue_instr = 0x101010B3

    # expected output from the model
    expected_mav_putvalue = bitmanip(mav_putvalue_instr, mav_putvalue_src1, mav_putvalue_src2, mav_putvalue_src3)

    # driving the input transaction
    dut.mav_putvalue_src1.value = mav_putvalue_src1
    dut.mav_putvalue_src2.value = mav_putvalue_src2
    dut.mav_putvalue_src3.value = mav_putvalue_src3
    dut.EN_mav_putvalue.value = 1
    dut.mav_putvalue_instr.value = mav_putvalue_instr
  
    yield Timer(1) 

    # obtaining the output
    dut_output = dut.mav_putvalue.value

    cocotb.log.info(f'DUT OUTPUT={hex(dut_output)}')
    cocotb.log.info(f'EXPECTED OUTPUT={hex(expected_mav_putvalue)}')
    
    # comparison
    error_message = f'TEST CASE FOR SBCLR - 11. Value mismatch DUT = {hex(dut_output)} does not match MODEL = {hex(expected_mav_putvalue)}'
    assert dut_output == expected_mav_putvalue, error_message


@cocotb.test()
def run_test_SBSET(dut):

    dut._log.info(f'Running test for ADD Instruction')

    # clock
    cocotb.fork(clock_gen(dut.CLK))

    # reset
    dut.RST_N.value <= 0
    yield Timer(10) 
    dut.RST_N.value <= 1

    ######### CTB : Modify the test to expose the bug #############
    # input transaction
    mav_putvalue_src1 = 0x45
    mav_putvalue_src2 = 0x1C
    mav_putvalue_src3 = 0x0
    # My CODE
    desOp = list('0110011')
    desFunc3 = list('001')
    desFunc7 = list('0010100')
    inst = bin(0)[2:0]
    inst = inst.zfill(32)
    instList = list(inst)
    instList[0:7] = desFunc7
    instList[17:20] = desFunc3
    instList[-7::] = desOp
    inst = ''.join(instList)
    mav_putvalue_instr = int(inst,2)

    #mav_putvalue_instr = 0x101010B3

    # expected output from the model
    expected_mav_putvalue = bitmanip(mav_putvalue_instr, mav_putvalue_src1, mav_putvalue_src2, mav_putvalue_src3)

    # driving the input transaction
    dut.mav_putvalue_src1.value = mav_putvalue_src1
    dut.mav_putvalue_src2.value = mav_putvalue_src2
    dut.mav_putvalue_src3.value = mav_putvalue_src3
    dut.EN_mav_putvalue.value = 1
    dut.mav_putvalue_instr.value = mav_putvalue_instr
  
    yield Timer(1) 

    # obtaining the output
    dut_output = dut.mav_putvalue.value

    cocotb.log.info(f'DUT OUTPUT={hex(dut_output)}')
    cocotb.log.info(f'EXPECTED OUTPUT={hex(expected_mav_putvalue)}')
    
    # comparison
    error_message = f'TEST CASE FOR SBSET - 12. Value mismatch DUT = {hex(dut_output)} does not match MODEL = {hex(expected_mav_putvalue)}'
    assert dut_output == expected_mav_putvalue, error_message


@cocotb.test()
def run_test_SBINV(dut):

    dut._log.info(f'Running test for ADD Instruction')

    # clock
    cocotb.fork(clock_gen(dut.CLK))

    # reset
    dut.RST_N.value <= 0
    yield Timer(10) 
    dut.RST_N.value <= 1

    ######### CTB : Modify the test to expose the bug #############
    # input transaction
    mav_putvalue_src1 = 0x45
    mav_putvalue_src2 = 0x1C
    mav_putvalue_src3 = 0x0
    # My CODE
    desOp = list('0110011')
    desFunc3 = list('001')
    desFunc7 = list('0110100')
    inst = bin(0)[2:0]
    inst = inst.zfill(32)
    instList = list(inst)
    instList[0:7] = desFunc7
    instList[17:20] = desFunc3
    instList[-7::] = desOp
    inst = ''.join(instList)
    mav_putvalue_instr = int(inst,2)

    #mav_putvalue_instr = 0x101010B3

    # expected output from the model
    expected_mav_putvalue = bitmanip(mav_putvalue_instr, mav_putvalue_src1, mav_putvalue_src2, mav_putvalue_src3)

    # driving the input transaction
    dut.mav_putvalue_src1.value = mav_putvalue_src1
    dut.mav_putvalue_src2.value = mav_putvalue_src2
    dut.mav_putvalue_src3.value = mav_putvalue_src3
    dut.EN_mav_putvalue.value = 1
    dut.mav_putvalue_instr.value = mav_putvalue_instr
  
    yield Timer(1) 

    # obtaining the output
    dut_output = dut.mav_putvalue.value

    cocotb.log.info(f'DUT OUTPUT={hex(dut_output)}')
    cocotb.log.info(f'EXPECTED OUTPUT={hex(expected_mav_putvalue)}')
    
    # comparison
    error_message = f'TEST CASE FOR SBINV - 13. Value mismatch DUT = {hex(dut_output)} does not match MODEL = {hex(expected_mav_putvalue)}'
    assert dut_output == expected_mav_putvalue, error_message


@cocotb.test()
def run_test_SBEXT(dut):

    dut._log.info(f'Running test for ADD Instruction')

    # clock
    cocotb.fork(clock_gen(dut.CLK))

    # reset
    dut.RST_N.value <= 0
    yield Timer(10) 
    dut.RST_N.value <= 1

    ######### CTB : Modify the test to expose the bug #############
    # input transaction
    mav_putvalue_src1 = 0x45
    mav_putvalue_src2 = 0x1C
    mav_putvalue_src3 = 0x0
    # My CODE
    desOp = list('0110011')
    desFunc3 = list('101')
    desFunc7 = list('0100100')
    inst = bin(0)[2:0]
    inst = inst.zfill(32)
    instList = list(inst)
    instList[0:7] = desFunc7
    instList[17:20] = desFunc3
    instList[-7::] = desOp
    inst = ''.join(instList)
    mav_putvalue_instr = int(inst,2)

    #mav_putvalue_instr = 0x101010B3

    # expected output from the model
    expected_mav_putvalue = bitmanip(mav_putvalue_instr, mav_putvalue_src1, mav_putvalue_src2, mav_putvalue_src3)

    # driving the input transaction
    dut.mav_putvalue_src1.value = mav_putvalue_src1
    dut.mav_putvalue_src2.value = mav_putvalue_src2
    dut.mav_putvalue_src3.value = mav_putvalue_src3
    dut.EN_mav_putvalue.value = 1
    dut.mav_putvalue_instr.value = mav_putvalue_instr
  
    yield Timer(1) 

    # obtaining the output
    dut_output = dut.mav_putvalue.value

    cocotb.log.info(f'DUT OUTPUT={hex(dut_output)}')
    cocotb.log.info(f'EXPECTED OUTPUT={hex(expected_mav_putvalue)}')
    
    # comparison
    error_message = f'TEST CASE FOR SBEXT - 14. Value mismatch DUT = {hex(dut_output)} does not match MODEL = {hex(expected_mav_putvalue)}'
    assert dut_output == expected_mav_putvalue, error_message


@cocotb.test()
def run_test_GORC(dut):

    dut._log.info(f'Running test for ADD Instruction')

    # clock
    cocotb.fork(clock_gen(dut.CLK))

    # reset
    dut.RST_N.value <= 0
    yield Timer(10) 
    dut.RST_N.value <= 1

    ######### CTB : Modify the test to expose the bug #############
    # input transaction
    mav_putvalue_src1 = 0x45
    mav_putvalue_src2 = 0x1C
    mav_putvalue_src3 = 0x0
    # My CODE
    desOp = list('0110011')
    desFunc3 = list('101')
    desFunc7 = list('0010100')
    inst = bin(0)[2:0]
    inst = inst.zfill(32)
    instList = list(inst)
    instList[0:7] = desFunc7
    instList[17:20] = desFunc3
    instList[-7::] = desOp
    inst = ''.join(instList)
    mav_putvalue_instr = int(inst,2)

    #mav_putvalue_instr = 0x101010B3

    # expected output from the model
    expected_mav_putvalue = bitmanip(mav_putvalue_instr, mav_putvalue_src1, mav_putvalue_src2, mav_putvalue_src3)

    # driving the input transaction
    dut.mav_putvalue_src1.value = mav_putvalue_src1
    dut.mav_putvalue_src2.value = mav_putvalue_src2
    dut.mav_putvalue_src3.value = mav_putvalue_src3
    dut.EN_mav_putvalue.value = 1
    dut.mav_putvalue_instr.value = mav_putvalue_instr
  
    yield Timer(1) 

    # obtaining the output
    dut_output = dut.mav_putvalue.value

    cocotb.log.info(f'DUT OUTPUT={hex(dut_output)}')
    cocotb.log.info(f'EXPECTED OUTPUT={hex(expected_mav_putvalue)}')
    
    # comparison
    error_message = f'TEST CASE FOR GORC - 15. Value mismatch DUT = {hex(dut_output)} does not match MODEL = {hex(expected_mav_putvalue)}'
    assert dut_output == expected_mav_putvalue, error_message


@cocotb.test()
def run_test_GREV(dut):

    dut._log.info(f'Running test for ADD Instruction')

    # clock
    cocotb.fork(clock_gen(dut.CLK))

    # reset
    dut.RST_N.value <= 0
    yield Timer(10) 
    dut.RST_N.value <= 1

    ######### CTB : Modify the test to expose the bug #############
    # input transaction
    mav_putvalue_src1 = 0x45
    mav_putvalue_src2 = 0x1C
    mav_putvalue_src3 = 0x0
    # My CODE
    desOp = list('0110011')
    desFunc3 = list('101')
    desFunc7 = list('0110100')
    inst = bin(0)[2:0]
    inst = inst.zfill(32)
    instList = list(inst)
    instList[0:7] = desFunc7
    instList[17:20] = desFunc3
    instList[-7::] = desOp
    inst = ''.join(instList)
    mav_putvalue_instr = int(inst,2)

    #mav_putvalue_instr = 0x101010B3

    # expected output from the model
    expected_mav_putvalue = bitmanip(mav_putvalue_instr, mav_putvalue_src1, mav_putvalue_src2, mav_putvalue_src3)

    # driving the input transaction
    dut.mav_putvalue_src1.value = mav_putvalue_src1
    dut.mav_putvalue_src2.value = mav_putvalue_src2
    dut.mav_putvalue_src3.value = mav_putvalue_src3
    dut.EN_mav_putvalue.value = 1
    dut.mav_putvalue_instr.value = mav_putvalue_instr
  
    yield Timer(1) 

    # obtaining the output
    dut_output = dut.mav_putvalue.value

    cocotb.log.info(f'DUT OUTPUT={hex(dut_output)}')
    cocotb.log.info(f'EXPECTED OUTPUT={hex(expected_mav_putvalue)}')
    
    # comparison
    error_message = f'TEST CASE FOR GREV - 16. Value mismatch DUT = {hex(dut_output)} does not match MODEL = {hex(expected_mav_putvalue)}'
    assert dut_output == expected_mav_putvalue, error_message


@cocotb.test()
def run_test_CMIX(dut):

    dut._log.info(f'Running test for ADD Instruction')

    # clock
    cocotb.fork(clock_gen(dut.CLK))

    # reset
    dut.RST_N.value <= 0
    yield Timer(10) 
    dut.RST_N.value <= 1

    ######### CTB : Modify the test to expose the bug #############
    # input transaction
    mav_putvalue_src1 = 0x45
    mav_putvalue_src2 = 0x1C
    mav_putvalue_src3 = 0xAAAA5555
    # My CODE
    desOp = list('0110011')
    desFunc3 = list('001')
    desFunc7_2 = list('11')
    inst = bin(0)[2:0]
    inst = inst.zfill(32)
    instList = list(inst)
    instList[5:7] = desFunc7_2
    instList[17:20] = desFunc3
    instList[-7::] = desOp
    inst = ''.join(instList)
    mav_putvalue_instr = int(inst,2)

    #mav_putvalue_instr = 0x101010B3

    # expected output from the model
    expected_mav_putvalue = bitmanip(mav_putvalue_instr, mav_putvalue_src1, mav_putvalue_src2, mav_putvalue_src3)

    # driving the input transaction
    dut.mav_putvalue_src1.value = mav_putvalue_src1
    dut.mav_putvalue_src2.value = mav_putvalue_src2
    dut.mav_putvalue_src3.value = mav_putvalue_src3
    dut.EN_mav_putvalue.value = 1
    dut.mav_putvalue_instr.value = mav_putvalue_instr
  
    yield Timer(1) 

    # obtaining the output
    dut_output = dut.mav_putvalue.value

    cocotb.log.info(f'DUT OUTPUT={hex(dut_output)}')
    cocotb.log.info(f'EXPECTED OUTPUT={hex(expected_mav_putvalue)}')
    
    # comparison
    error_message = f'TEST CASE FOR CMIX - 17. Value mismatch DUT = {hex(dut_output)} does not match MODEL = {hex(expected_mav_putvalue)}'
    assert dut_output == expected_mav_putvalue, error_message


@cocotb.test()
def run_test_CMOV(dut):

    dut._log.info(f'Running test for ADD Instruction')

    # clock
    cocotb.fork(clock_gen(dut.CLK))

    # reset
    dut.RST_N.value <= 0
    yield Timer(10) 
    dut.RST_N.value <= 1

    ######### CTB : Modify the test to expose the bug #############
    # input transaction
    mav_putvalue_src1 = 0x45
    mav_putvalue_src2 = 0x1C
    mav_putvalue_src3 = 0xAAAA5555
    # My CODE
    desOp = list('0110011')
    desFunc3 = list('101')
    desFunc7_2 = list('11')
    inst = bin(0)[2:0]
    inst = inst.zfill(32)
    instList = list(inst)
    instList[5:7] = desFunc7_2
    instList[17:20] = desFunc3
    instList[-7::] = desOp
    inst = ''.join(instList)
    mav_putvalue_instr = int(inst,2)

    #mav_putvalue_instr = 0x101010B3

    # expected output from the model
    expected_mav_putvalue = bitmanip(mav_putvalue_instr, mav_putvalue_src1, mav_putvalue_src2, mav_putvalue_src3)

    # driving the input transaction
    dut.mav_putvalue_src1.value = mav_putvalue_src1
    dut.mav_putvalue_src2.value = mav_putvalue_src2
    dut.mav_putvalue_src3.value = mav_putvalue_src3
    dut.EN_mav_putvalue.value = 1
    dut.mav_putvalue_instr.value = mav_putvalue_instr
  
    yield Timer(1) 

    # obtaining the output
    dut_output = dut.mav_putvalue.value

    cocotb.log.info(f'DUT OUTPUT={hex(dut_output)}')
    cocotb.log.info(f'EXPECTED OUTPUT={hex(expected_mav_putvalue)}')
    
    # comparison
    error_message = f'TEST CASE FOR CMOV - 18. Value mismatch DUT = {hex(dut_output)} does not match MODEL = {hex(expected_mav_putvalue)}'
    assert dut_output == expected_mav_putvalue, error_message


@cocotb.test()
def run_test_FSL(dut):

    dut._log.info(f'Running test for ADD Instruction')

    # clock
    cocotb.fork(clock_gen(dut.CLK))

    # reset
    dut.RST_N.value <= 0
    yield Timer(10) 
    dut.RST_N.value <= 1

    ######### CTB : Modify the test to expose the bug #############
    # input transaction
    mav_putvalue_src1 = 0x45
    mav_putvalue_src2 = 0x1C
    mav_putvalue_src3 = 0xAAAA5555
    # My CODE
    desOp = list('0110011')
    desFunc3 = list('001')
    desFunc7_2 = list('10')
    inst = bin(0)[2:0]
    inst = inst.zfill(32)
    instList = list(inst)
    instList[5:7] = desFunc7_2
    instList[17:20] = desFunc3
    instList[-7::] = desOp
    inst = ''.join(instList)
    mav_putvalue_instr = int(inst,2)

    #mav_putvalue_instr = 0x101010B3

    # expected output from the model
    expected_mav_putvalue = bitmanip(mav_putvalue_instr, mav_putvalue_src1, mav_putvalue_src2, mav_putvalue_src3)

    # driving the input transaction
    dut.mav_putvalue_src1.value = mav_putvalue_src1
    dut.mav_putvalue_src2.value = mav_putvalue_src2
    dut.mav_putvalue_src3.value = mav_putvalue_src3
    dut.EN_mav_putvalue.value = 1
    dut.mav_putvalue_instr.value = mav_putvalue_instr
  
    yield Timer(1) 

    # obtaining the output
    dut_output = dut.mav_putvalue.value

    cocotb.log.info(f'DUT OUTPUT={hex(dut_output)}')
    cocotb.log.info(f'EXPECTED OUTPUT={hex(expected_mav_putvalue)}')
    
    # comparison
    error_message = f'TEST CASE FOR FSL - 19. Value mismatch DUT = {hex(dut_output)} does not match MODEL = {hex(expected_mav_putvalue)}'
    assert dut_output == expected_mav_putvalue, error_message

@cocotb.test()
def run_test_FSR(dut):

    dut._log.info(f'Running test for ADD Instruction')

    # clock
    cocotb.fork(clock_gen(dut.CLK))

    # reset
    dut.RST_N.value <= 0
    yield Timer(10) 
    dut.RST_N.value <= 1

    ######### CTB : Modify the test to expose the bug #############
    # input transaction
    mav_putvalue_src1 = 0x45
    mav_putvalue_src2 = 0x1C
    mav_putvalue_src3 = 0xAAAA5555
    # My CODE
    desOp = list('0110011')
    desFunc3 = list('101')
    desFunc7_2 = list('10')
    inst = bin(0)[2:0]
    inst = inst.zfill(32)
    instList = list(inst)
    instList[5:7] = desFunc7_2
    instList[17:20] = desFunc3
    instList[-7::] = desOp
    inst = ''.join(instList)
    mav_putvalue_instr = int(inst,2)

    #mav_putvalue_instr = 0x101010B3

    # expected output from the model
    expected_mav_putvalue = bitmanip(mav_putvalue_instr, mav_putvalue_src1, mav_putvalue_src2, mav_putvalue_src3)

    # driving the input transaction
    dut.mav_putvalue_src1.value = mav_putvalue_src1
    dut.mav_putvalue_src2.value = mav_putvalue_src2
    dut.mav_putvalue_src3.value = mav_putvalue_src3
    dut.EN_mav_putvalue.value = 1
    dut.mav_putvalue_instr.value = mav_putvalue_instr
  
    yield Timer(1) 

    # obtaining the output
    dut_output = dut.mav_putvalue.value

    cocotb.log.info(f'DUT OUTPUT={hex(dut_output)}')
    cocotb.log.info(f'EXPECTED OUTPUT={hex(expected_mav_putvalue)}')
    
    # comparison
    error_message = f'TEST CASE FOR FSR - 20. Value mismatch DUT = {hex(dut_output)} does not match MODEL = {hex(expected_mav_putvalue)}'
    assert dut_output == expected_mav_putvalue, error_message

