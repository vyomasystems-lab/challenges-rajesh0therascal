# Simple tests for an adder module
import cocotb
from cocotb.triggers import Timer
import random

@cocotb.test()
async def vedicMult_basic_test(dut):
    """Test for 5 + 10"""

    A = 5
    B = 10

    # input driving
    dut.a.value = A
    dut.b.value = B

    await Timer(2, units='ns')
    
    assert dut.prod.value == A*B, "Adder result is incorrect: {A} * {B} != {PROD}, expected value={EXP}".format(
            A=int(dut.a.value), B=int(dut.b.value), PROD=int(dut.prod.value), EXP=A*B)


@cocotb.test()
async def vedicMult_randomised_test(dut):
    """Test for adding 2 random numbers multiple times"""

    for i in range(5):

        A = random.randint(0, 256)
        B = random.randint(0, 256)

        dut.a.value = A
        dut.b.value = B

        await Timer(2, units='ns')
        
        dut._log.info(f'A={A:05} B={B:05} model={A+B:05} DUT={int(dut.prod.value):05}')
        assert dut.prod.value == A*B, "Randomised test failed with: {A} + {B} = {SUM}".format(
            A=dut.a.value, B=dut.b.value, SUM=dut.prod.value)


@cocotb.test()
async def vedicMult_rippleAdderTest(dut):
    """Test for adding 2 random numbers multiple times"""

    for i in range(5):

        A = random.randint(0, 256)
        B = random.randint(0, 256)

        dut.a.value = A
        dut.b.value = B

        await Timer(2, units='ns')
        
        dut._log.info(f'A={A:05} B={B:05} model={A+B:05} DUT={int(dut.prod.value):05}')
        dut._log.info(f'Ripple Adder 8 bit output is  {int(dut.sum0.value)}')

        assert dut.prod.value == A*B, "Randomised test failed with: {A} + {B} = {SUM}".format(
            A=dut.a.value, B=dut.b.value, SUM=dut.prod.value)