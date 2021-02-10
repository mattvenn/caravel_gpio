`default_nettype none
module io_tester(
    input wire wb_clk_i,
    input wire wb_rst_i,

    // IOs
    input  wire [`MPRJ_IO_PADS-1:0] io_in,
    output wire [`MPRJ_IO_PADS-1:0] io_out,
    output wire [`MPRJ_IO_PADS-1:0] io_oeb
    );

    // outputs
    assign io_out[11] = wb_clk_i;
    assign io_out[12] = wb_clk_i;
    assign io_out[14] = wb_clk_i;

    // output enables
    assign io_oeb[ 8] = 1'b1;
    assign io_oeb[ 9] = 1'b1;
    assign io_oeb[10] = 1'b0;
    assign io_oeb[11] = 1'b1;
    assign io_oeb[12] = 1'b0;
    assign io_oeb[13] = 1'b1;
    assign io_oeb[14] = 1'b0;

endmodule
