from riscv_assembler.convert import AssemblyConverter
cnv = AssemblyConverter()
cnv.convert("hello.s")
#outputs to binary file simple.bin