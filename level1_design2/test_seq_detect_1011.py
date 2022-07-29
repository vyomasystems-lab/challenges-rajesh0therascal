# See LICENSE.vyoma for details

# SPDX-License-Identifier: CC0-1.0

import os
import random
from pathlib import Path
import re

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge


@cocotb.test()
async def test_seq_op_same_cycle(dut):
    """Test for seq detection """

    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    # reset
    dut.reset.value = 1
    await FallingEdge(dut.clk)  
    dut.reset.value = 0
    bitString = "{0:b}".format(11)
    sequenceCount = [s.start() for s in re.finditer('1011', bitString)]
    dutCount = len(sequenceCount)
    testCount = 0
    for bit in range(len(bitString)):
        if bitString[bit] == '1':
            dut.inp_bit.value = 1
        else:
            dut.inp_bit.value = 0
        await FallingEdge(dut.clk)
        if (dut.seq_seen == 1):
            dut._log.info(f'Output Arrived in wrong state and current state is {int(dut.current_state)}')
            testCount = testCount + 1
            failureDetected = 1
    dut.inp_bit.value = 0
    await FallingEdge(dut.clk)
    dut._log.info(f'Output should arrive here')

    #if(dut.seq_seen == 1):
     #   testCount = testCount + 1
    
    dut._log.info(f'Failure is {testCount}')

    assert failureDetected != 1, "Test failed output is generated on the arrival of last bit of sequence but not on next cycle for sequence Input " + bitString


@cocotb.test()
async def test_seq_all_bruteforce(dut):
    """Test for seq detection """

    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    # reset
    dut.reset.value = 1
    await FallingEdge(dut.clk)  
    dut.reset.value = 0
    await FallingEdge(dut.clk) 

    for inputs in range(8,128):
        dut.reset.value = 1
        await FallingEdge(dut.clk)
        await FallingEdge(dut.clk)
        dut.reset.value = 0
        await FallingEdge(dut.clk)
        #dut._log.info(f'I am running')
        bitString = "{0:b}".format(inputs)
        sequenceCount = [s.start() for s in re.finditer('1011', bitString)]
        dutCount = len(sequenceCount)
        testCount = 0
        for bit in range(len(bitString)):
            if bitString[bit] == '1':
                dut.inp_bit.value = 1
            else:
                dut.inp_bit.value = 0
            await FallingEdge(dut.clk)
            if (dut.seq_seen == 1):
                testCount = testCount + 1
        
        dut.inp_bit.value = 0
        await FallingEdge(dut.clk)

        if testCount != dutCount:
            # dut._log.info(f'TEST PASSED For Input={bitString} Test Output= {testCount}  Gold Output ={dutCount}')
            failureDetected = 1
            dut._log.info(f'TEST FAILED For Input={bitString} Test Output= {testCount}  Gold Output ={dutCount}')

    assert failureDetected == 0, "Test failed with few sequences"

    #cocotb.log.info('#### CTB: Develop your test here! ######')


@cocotb.test()
async def test_seq_for_error_SEQ_1(dut):
    """Test for seq detection """

    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    # reset
    dut.reset.value = 1
    await FallingEdge(dut.clk)  
    dut.reset.value = 0
    bitString = "{0:b}".format(27)
    sequenceCount = [s.start() for s in re.finditer('1011', bitString)]
    dutCount = len(sequenceCount)
    testCount = 0
    failureDetected = 0
    for bit in range(len(bitString)):
        if bitString[bit] == '1':
            dut.inp_bit.value = 1
        else:
            dut.inp_bit.value = 0
        if (dut.seq_seen == 1):
            dut._log.info(f'Output should arrive here')
            testCount = testCount + 1
            failureDetected = 1
    
    dut._log.info(f'Failure is {failureDetected}')

    assert failureDetected == 1, "Test failed output is not generated for sequence Input " + bitString



@cocotb.test()
async def test_seq_for_error_SEQ_101(dut):
    """Test for seq detection """

    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    # reset
    dut.reset.value = 1
    await FallingEdge(dut.clk)  
    dut.reset.value = 0
    bitString = "{0:b}".format(43)
    sequenceCount = [s.start() for s in re.finditer('1011', bitString)]
    dutCount = len(sequenceCount)
    testCount = 0
    failureDetected = 0
    for bit in range(len(bitString)):
        if bitString[bit] == '1':
            dut.inp_bit.value = 1
        else:
            dut.inp_bit.value = 0
        if (dut.seq_seen == 1):
            dut._log.info(f'Output should arrive here')
            testCount = testCount + 1
            failureDetected = 1
    
    dut._log.info(f'Failure is {failureDetected}')

    assert failureDetected == 1, "Test failed output is not generated for sequence Input " + bitString
