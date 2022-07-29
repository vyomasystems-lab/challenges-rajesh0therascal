# Simple tests for an adder module
import cocotb
from cocotb.triggers import Timer
import random

@cocotb.test()
async def vedicMult_basic_Test(dut):
    """Test for 5 * 10"""

    A = 5
    B = 10

    # input driving
    dut.a.value = A
    dut.b.value = B

    await Timer(2, units='ns')
    
    assert dut.prod.value == A*B, "Adder result is incorrect: {A} * {B} != {PROD}, expected value={EXP}".format(
            A=int(dut.a.value), B=int(dut.b.value), PROD=int(dut.prod.value), EXP=A*B)


@cocotb.test()
async def vedicMult_randomised_Test(dut):

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
async def vedicMult_rippleAdder8bitTest(dut):


    for i in range(5):

        A = random.randint(0, 256)
        B = random.randint(0, 256)

        dut.a.value = A
        dut.b.value = B

        await Timer(2, units='ns')
        
        dut._log.info(f'A={A:05} B={B:05} model={A+B:05} DUT={int(dut.prod.value):05}')
        dut._log.info(f'Ripple Adder 8 bit output is  {int(dut.sum0.value)}')

        assert int(dut.sum0.value) == int(dut.mult2.value)+((dut.mult0.value & (0xF0))>>4), "Ripple Adder 8 bit test failed"


@cocotb.test()
async def vedicMult_rippleAdder12bitTest(dut):

    for i in range(5):

        A = random.randint(0, 256)
        B = random.randint(0, 256)

        dut.a.value = A
        dut.b.value = B

        await Timer(2, units='ns')
        
        dut._log.info(f'A={A:05} B={B:05} model={A+B:05} DUT={int(dut.prod.value):05}')
        dut._log.info(f'Ripple Adder 8 bit output is  {int(dut.sum0.value)}')

        assert int(dut.sum1.value) == (int(dut.mult3.value) << 4)+ int(dut.mult1.value), "Ripple Adder 12 bit test failed"


@cocotb.test()
async def vedicMult_rippleAdder4x4Test(dut):

    for i in range(5):

        A = random.randint(0, 256)
        B = random.randint(0, 256)

        dut.a.value = A
        dut.b.value = B

        await Timer(2, units='ns')
        
        dut._log.info(f'A={A:05} B={B:05} model={A+B:05} DUT={int(dut.prod.value):05}')
        dut._log.info(f'Ripple Adder 8 bit output is  {int(dut.sum0.value)}')

        assert (A & 0x0F) * (B & 0x0F) == int(dut.mult0.value), "4x4 Multiplier test failed"

@cocotb.test()
async def vedicMult_rippleAdder2x2Test(dut):

    for i in range(5):

        A = random.randint(0, 256)
        B = random.randint(0, 256)

        dut.a.value = A
        dut.b.value = B

        await Timer(2, units='ns')
        
        dut._log.info(f'A={A:05} B={B:05} model={A+B:05} DUT={int(dut.prod.value):05}')

        assert (A & 0x03) * (B & 0x03) == int(dut.VD0.mult0.value), "2x2 Multiplier test failed"

@cocotb.test()
async def vedicMult_rippleAdder2x2PinPointTest(dut):

    failCount = 0

    for i in range(5):

        A = random.randint(0, 256)
        B = random.randint(0, 256)

        dut.a.value = A
        dut.b.value = B

        A0B0 = (A & (0X01)) & (B & (0X01))
        A1B1 = ((A & (0X02))>>1) & ((B & (0X02))>>1)
        A0B1 = (A & (0X01)) & ((B & (0X02))>>1)
        A1B0 = ((A & (0X02))>>1) & (B & (0X01))

        await Timer(2, units='ns')

        if (A0B0 != int(dut.VD0.VD0.a0b0.value)):
            dut._log.info(f'A0B0 value failed A0B0 model output is {A0B0} Actual output is {int(dut.VD0.VD0.a0b0.value)} ')
            failCount = failCount + 1

        if (A0B1 != int(dut.VD0.VD0.a0b1.value)):
            dut._log.info(f'A0B1 value failed A0B1 model output is {A0B1} Actual output is {int(dut.VD0.VD0.a0b1.value)} ')
            failCount = failCount + 1

        if (A1B0 != int(dut.VD0.VD0.a1b0.value)):
            dut._log.info(f'A1B0 value failed A1B0 model output is {A1B0} Actual output is {int(dut.VD0.VD0.a1b0.value)} ')
            failCount = failCount + 1

        if (A1B1 != int(dut.VD0.VD0.a1b1.value)):
            dut._log.info(f'A1B1 value failed A1B1 model output is {A1B1} Actual output is {int(dut.VD0.VD0.a1b1.value)} ')
            failCount = failCount + 1




        
        dut._log.info(f'A={A:05} B={B:05} model={A+B:05} DUT={int(dut.prod.value):05}')
        dut._log.info(f'Ripple Adder 8 bit output is  {int(dut.sum0.value)}')

        assert failCount == 0, "2x2 Multiplier pinpoint Test"