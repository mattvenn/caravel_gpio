import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge, ClockCycles


# takes ~60 seconds on my PC
@cocotb.test()
async def test_start(dut):
    clock = Clock(dut.clock, 25, units="ns")
    cocotb.fork(clock.start())
    
    dut.RSTB <= 0
    dut.power1 <= 0;
    dut.power2 <= 0;
    dut.power3 <= 0;
    dut.power4 <= 0;

    await ClockCycles(dut.clock, 8)
    dut.power1 <= 1;
    await ClockCycles(dut.clock, 8)
    dut.power2 <= 1;
    await ClockCycles(dut.clock, 8)
    dut.power3 <= 1;
    await ClockCycles(dut.clock, 8)
    dut.power4 <= 1;

    await ClockCycles(dut.clock, 80)
    dut.RSTB <= 1

    await RisingEdge(dut.check_pin)

@cocotb.test()
async def test_io(dut):
    clock = Clock(dut.clock, 25, units="ns")

    cocotb.fork(clock.start())

    for i in range(20):
        await ClockCycles(dut.clock, 1)
        dut.mprj_io[ 8] <= 1;
        dut.mprj_io[ 9] <= 1;
        dut.mprj_io[10] <= 1;
        dut.mprj_io[13] <= 1;
        await ClockCycles(dut.clock, 1)
        dut.mprj_io[ 8] <= 0;
        dut.mprj_io[ 9] <= 0;
        dut.mprj_io[10] <= 0;
        dut.mprj_io[13] <= 0;
