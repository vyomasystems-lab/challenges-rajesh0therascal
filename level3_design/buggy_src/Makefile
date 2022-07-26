# See LICENSE.vyoma for details

TOPLEVEL_LANG ?= verilog

PWD=$(shell pwd)

VERILOG_SOURCES = $(PWD)/vedic8x8.v $(PWD)/vedic4x4.v $(PWD)/vedic2x2.v $(PWD)/ripple_adder_12bit.v $(PWD)/ripple_adder_8bit.v $(PWD)/ripple_adder_6bit.v $(PWD)/ripple_adder_4bit.v $(PWD)/full_adder.v $(PWD)/half_adder.v              # provide your design path

TOPLEVEL := vedic8x8      # design file
MODULE   := test_src    # test file

include $(shell cocotb-config --makefiles)/Makefile.sim

clean_all: clean
	rm -rf *.xml sim_build __pycache__ 
