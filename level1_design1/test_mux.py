# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer


@cocotb.test()
async def test_mux_inp0(dut):
    for inputValue in range(4):
        dut.inp0.value = inputValue
        dut.sel.value = 0
        await Timer(2, units='ns')

        dut._log.info(f'For Input={inputValue:02} Select= 0  OUT={int(dut.out.value):02}')
        assert dut.out.value == inputValue, "Test failed with: {input} {sel} = {output}".format(input=inputValue, sel=dut.sel.value, output = dut.out.value)

@cocotb.test()
async def test_mux_inp1(dut):
    for inputValue in range(4):
        dut.inp1.value = inputValue
        dut.sel.value = 1
        await Timer(2, units='ns')

        dut._log.info(f'For Input={inputValue:02} Select= 1  OUT={int(dut.out.value):02}')
        assert dut.out.value == inputValue, "Test failed with: {input} {sel} = {output}".format(input=inputValue, sel=dut.sel.value, output = dut.out.value)
		

@cocotb.test()
async def test_mux_inp2(dut):
    for inputValue in range(4):
        dut.inp2.value = inputValue
        dut.sel.value = 2
        await Timer(2, units='ns')

        dut._log.info(f'For Input={inputValue:02} Select= 2  OUT={int(dut.out.value):02}')
        assert dut.out.value == inputValue, "Test failed with: {input} {sel} = {output}".format(input=inputValue, sel=dut.sel.value, output = dut.out.value)
		

@cocotb.test()
async def test_mux_inp3(dut):
    for inputValue in range(4):
        dut.inp3.value = inputValue
        dut.sel.value = 3
        await Timer(2, units='ns')

        dut._log.info(f'For Input={inputValue:02} Select= 3  OUT={int(dut.out.value):02}')
        assert dut.out.value == inputValue, "Test failed with: {input} {sel} = {output}".format(input=inputValue, sel=dut.sel.value, output = dut.out.value)
		
@cocotb.test()
async def test_mux_inp4(dut):
    for inputValue in range(4):
        dut.inp4.value = inputValue
        dut.sel.value = 4
        await Timer(2, units='ns')

        dut._log.info(f'For Input={inputValue:02} Select= 4  OUT={int(dut.out.value):02}')
        assert dut.out.value == inputValue, "Test failed with: {input} {sel} = {output}".format(input=inputValue, sel=dut.sel.value, output = dut.out.value)
		

@cocotb.test()
async def test_mux_inp5(dut):
    for inputValue in range(4):
        dut.inp5.value = inputValue
        dut.sel.value = 5
        await Timer(2, units='ns')

        dut._log.info(f'For Input={inputValue:02} Select= 5  OUT={int(dut.out.value):02}')
        assert dut.out.value == inputValue, "Test failed with: {input} {sel} = {output}".format(input=inputValue, sel=dut.sel.value, output = dut.out.value)
		
@cocotb.test()
async def test_mux_inp6(dut):
    for inputValue in range(4):
        dut.inp6.value = inputValue
        dut.sel.value = 6
        await Timer(2, units='ns')

        dut._log.info(f'For Input={inputValue:02} Select= 6  OUT={int(dut.out.value):02}')
        assert dut.out.value == inputValue, "Test failed with: {input} {sel} = {output}".format(input=inputValue, sel=dut.sel.value, output = dut.out.value)
		
@cocotb.test()
async def test_mux_inp7(dut):
    for inputValue in range(4):
        dut.inp7.value = inputValue
        dut.sel.value = 7
        await Timer(2, units='ns')

        dut._log.info(f'For Input={inputValue:02} Select= 7  OUT={int(dut.out.value):02}')
        assert dut.out.value == inputValue, "Test failed with: {input} {sel} = {output}".format(input=inputValue, sel=dut.sel.value, output = dut.out.value)
		
@cocotb.test()
async def test_mux_inp8(dut):
    for inputValue in range(4):
        dut.inp8.value = inputValue
        dut.sel.value = 8
        await Timer(2, units='ns')

        dut._log.info(f'For Input={inputValue:02} Select= 8  OUT={int(dut.out.value):02}')
        assert dut.out.value == inputValue, "Test failed with: {input} {sel} = {output}".format(input=inputValue, sel=dut.sel.value, output = dut.out.value)
		
@cocotb.test()
async def test_mux_inp9(dut):
    for inputValue in range(4):
        dut.inp9.value = inputValue
        dut.sel.value = 9
        await Timer(2, units='ns')

        dut._log.info(f'For Input={inputValue:02} Select= 9  OUT={int(dut.out.value):02}')
        assert dut.out.value == inputValue, "Test failed with: {input} {sel} = {output}".format(input=inputValue, sel=dut.sel.value, output = dut.out.value)
		
@cocotb.test()
async def test_mux_inp10(dut):
    for inputValue in range(4):
        dut.inp10.value = inputValue
        dut.sel.value = 10
        await Timer(2, units='ns')

        dut._log.info(f'For Input={inputValue:02} Select= 10  OUT={int(dut.out.value):02}')
        assert dut.out.value == inputValue, "Test failed with: {input} {sel} = {output}".format(input=inputValue, sel=dut.sel.value, output = dut.out.value)
		
@cocotb.test()
async def test_mux_inp11(dut):
    for inputValue in range(4):
        dut.inp11.value = inputValue
        dut.sel.value = 11
        await Timer(2, units='ns')

        dut._log.info(f'For Input={inputValue:02} Select= 11  OUT={int(dut.out.value):02}')
        assert dut.out.value == inputValue, "Test failed with: {input} {sel} = {output}".format(input=inputValue, sel=dut.sel.value, output = dut.out.value)
		
@cocotb.test()
async def test_mux_inp12(dut):
    for inputValue in range(4):
        dut.inp12.value = inputValue
        dut.sel.value = 12
        await Timer(2, units='ns')

        dut._log.info(f'For Input={inputValue:02} Select= 12  OUT={int(dut.out.value):02}')
        assert dut.out.value == inputValue, "Test failed with: {input} {sel} = {output}".format(input=inputValue, sel=dut.sel.value, output = dut.out.value)
		

@cocotb.test()
async def test_mux_inp13(dut):
    for inputValue in range(4):
        dut.inp13.value = inputValue
        dut.sel.value = 13
        await Timer(2, units='ns')

        dut._log.info(f'For Input={inputValue:02} Select= 13  OUT={int(dut.out.value):02}')
        assert dut.out.value == inputValue, "Test failed with: {input} {sel} = {output}".format(input=inputValue, sel=dut.sel.value, output = dut.out.value)
		

@cocotb.test()
async def test_mux_inp14(dut):
    for inputValue in range(4):
        dut.inp14.value = inputValue
        dut.sel.value = 14
        await Timer(2, units='ns')

        dut._log.info(f'For Input={inputValue:02} Select= 14  OUT={int(dut.out.value):02}')
        assert dut.out.value == inputValue, "Test failed with: {input} {sel} = {output}".format(input=inputValue, sel=dut.sel.value, output = dut.out.value)
		

@cocotb.test()
async def test_mux_inp15(dut):
    for inputValue in range(4):
        dut.inp15.value = inputValue
        dut.sel.value = 15
        await Timer(2, units='ns')

        dut._log.info(f'For Input={inputValue:02} Select= 15  OUT={int(dut.out.value):02}')
        assert dut.out.value == inputValue, "Test failed with: {input} {sel} = {output}".format(input=inputValue, sel=dut.sel.value, output = dut.out.value)
		

@cocotb.test()
async def test_mux_inp16(dut):
    for inputValue in range(4):
        dut.inp16.value = inputValue
        dut.sel.value = 16
        await Timer(2, units='ns')

        dut._log.info(f'For Input={inputValue:02} Select= 16  OUT={int(dut.out.value):02}')
        assert dut.out.value == inputValue, "Test failed with: {input} {sel} = {output}".format(input=inputValue, sel=dut.sel.value, output = dut.out.value)
		

@cocotb.test()
async def test_mux_inp17(dut):
    for inputValue in range(4):
        dut.inp17.value = inputValue
        dut.sel.value = 17
        await Timer(2, units='ns')

        dut._log.info(f'For Input={inputValue:02} Select= 17  OUT={int(dut.out.value):02}')
        assert dut.out.value == inputValue, "Test failed with: {input} {sel} = {output}".format(input=inputValue, sel=dut.sel.value, output = dut.out.value)
		

@cocotb.test()
async def test_mux_inp18(dut):
    for inputValue in range(4):
        dut.inp18.value = inputValue
        dut.sel.value = 18
        await Timer(2, units='ns')

        dut._log.info(f'For Input={inputValue:02} Select= 18  OUT={int(dut.out.value):02}')
        assert dut.out.value == inputValue, "Test failed with: {input} {sel} = {output}".format(input=inputValue, sel=dut.sel.value, output = dut.out.value)
		

@cocotb.test()
async def test_mux_inp19(dut):
    for inputValue in range(4):
        dut.inp19.value = inputValue
        dut.sel.value = 19
        await Timer(2, units='ns')

        dut._log.info(f'For Input={inputValue:02} Select= 19  OUT={int(dut.out.value):02}')
        assert dut.out.value == inputValue, "Test failed with: {input} {sel} = {output}".format(input=inputValue, sel=dut.sel.value, output = dut.out.value)
		

@cocotb.test()
async def test_mux_inp20(dut):
    for inputValue in range(4):
        dut.inp20.value = inputValue
        dut.sel.value = 20
        await Timer(2, units='ns')

        dut._log.info(f'For Input={inputValue:02} Select= 20  OUT={int(dut.out.value):02}')
        assert dut.out.value == inputValue, "Test failed with: {input} {sel} = {output}".format(input=inputValue, sel=dut.sel.value, output = dut.out.value)
		

@cocotb.test()
async def test_mux_inp21(dut):
    for inputValue in range(4):
        dut.inp21.value = inputValue
        dut.sel.value = 21
        await Timer(2, units='ns')

        dut._log.info(f'For Input={inputValue:02} Select= 21  OUT={int(dut.out.value):02}')
        assert dut.out.value == inputValue, "Test failed with: {input} {sel} = {output}".format(input=inputValue, sel=dut.sel.value, output = dut.out.value)
		

@cocotb.test()
async def test_mux_inp22(dut):
    for inputValue in range(4):
        dut.inp22.value = inputValue
        dut.sel.value = 22
        await Timer(2, units='ns')

        dut._log.info(f'For Input={inputValue:02} Select= 22  OUT={int(dut.out.value):02}')
        assert dut.out.value == inputValue, "Test failed with: {input} {sel} = {output}".format(input=inputValue, sel=dut.sel.value, output = dut.out.value)
		

@cocotb.test()
async def test_mux_inp23(dut):
    for inputValue in range(4):
        dut.inp23.value = inputValue
        dut.sel.value = 23
        await Timer(2, units='ns')

        dut._log.info(f'For Input={inputValue:02} Select= 23  OUT={int(dut.out.value):02}')
        assert dut.out.value == inputValue, "Test failed with: {input} {sel} = {output}".format(input=inputValue, sel=dut.sel.value, output = dut.out.value)
		

@cocotb.test()
async def test_mux_inp24(dut):
    for inputValue in range(4):
        dut.inp24.value = inputValue
        dut.sel.value = 24
        await Timer(2, units='ns')

        dut._log.info(f'For Input={inputValue:02} Select= 24  OUT={int(dut.out.value):02}')
        assert dut.out.value == inputValue, "Test failed with: {input} {sel} = {output}".format(input=inputValue, sel=dut.sel.value, output = dut.out.value)
		

@cocotb.test()
async def test_mux_inp25(dut):
    for inputValue in range(4):
        dut.inp25.value = inputValue
        dut.sel.value = 25
        await Timer(2, units='ns')

        dut._log.info(f'For Input={inputValue:02} Select= 25  OUT={int(dut.out.value):02}')
        assert dut.out.value == inputValue, "Test failed with: {input} {sel} = {output}".format(input=inputValue, sel=dut.sel.value, output = dut.out.value)
		

@cocotb.test()
async def test_mux_inp26(dut):
    for inputValue in range(4):
        dut.inp26.value = inputValue
        dut.sel.value = 26
        await Timer(2, units='ns')

        dut._log.info(f'For Input={inputValue:02} Select= 26  OUT={int(dut.out.value):02}')
        assert dut.out.value == inputValue, "Test failed with: {input} {sel} = {output}".format(input=inputValue, sel=dut.sel.value, output = dut.out.value)
		

@cocotb.test()
async def test_mux_inp27(dut):
    for inputValue in range(4):
        dut.inp27.value = inputValue
        dut.sel.value = 27
        await Timer(2, units='ns')

        dut._log.info(f'For Input={inputValue:02} Select= 27  OUT={int(dut.out.value):02}')
        assert dut.out.value == inputValue, "Test failed with: {input} {sel} = {output}".format(input=inputValue, sel=dut.sel.value, output = dut.out.value)
		

@cocotb.test()
async def test_mux_inp28(dut):
    for inputValue in range(4):
        dut.inp28.value = inputValue
        dut.sel.value = 28
        await Timer(2, units='ns')

        dut._log.info(f'For Input={inputValue:02} Select= 28  OUT={int(dut.out.value):02}')
        assert dut.out.value == inputValue, "Test failed with: {input} {sel} = {output}".format(input=inputValue, sel=dut.sel.value, output = dut.out.value)
		

@cocotb.test()
async def test_mux_inp29(dut):
    for inputValue in range(4):
        dut.inp29.value = inputValue
        dut.sel.value = 29
        await Timer(2, units='ns')

        dut._log.info(f'For Input={inputValue:02} Select= 29  OUT={int(dut.out.value):02}')
        assert dut.out.value == inputValue, "Test failed with: {input} {sel} = {output}".format(input=inputValue, sel=dut.sel.value, output = dut.out.value)
		

@cocotb.test()
async def test_mux_inp30(dut):
    for inputValue in range(4):
        dut.inp30.value = inputValue
        dut.sel.value = 30
        await Timer(2, units='ns')

        dut._log.info(f'For Input={inputValue:02} Select= 30  OUT={int(dut.out.value):02}')
        assert dut.out.value == inputValue, "Test failed with: {input} {sel} = {output}".format(input=inputValue, sel=dut.sel.value, output = dut.out.value)
		
