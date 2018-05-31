import HackAssembler as hack
import unittest

class MyTest(unittest.TestCase):
  def initi(self):
    hack.pgmv2=[]
    hack.pgm=[]
    hack.symbol_table={'R0':"000000000000000",'R1':"000000000000001",'R2':'{0:015b}'.format(2),'R3':'{0:015b}'.format(3),'R4':'{0:015b}'.format(4),'R5':'{0:015b}'.format(5),'R6':'{0:015b}'.format(6),'R7':'{0:015b}'.format(7),'R8':'{0:015b}'.format(8),'R9':'{0:015b}'.format(9),'R10':'{0:015b}'.format(10),'R11':'{0:015b}'.format(11),'R12':'{0:015b}'.format(12),'R13':'{0:015b}'.format(13),'R14':'{0:015b}'.format(14),'R15':'{0:015b}'.format(15),"SCREEN":'{0:015b}'.format(16384),"KBD":'{0:015b}'.format(24576),'SP':'{0:015b}'.format(0),"LCL":'{0:015b}'.format(1),"ARG":'{0:015b}'.format(2),"THIS":'{0:015b}'.format(3),"THAT":'{0:015b}'.format(4)}

  def test_firstpass_onelabel(self):  #testing 1st pass
    hack.pgmv2=[]
    hack.pgm=["(label)","@2"]
    hack.first_pass()
    label="label"
    self.assertEqual(hack.symbol_table[label],'{0:015b}'.format(0))
    self.assertEqual(hack.pgmv2[0],'@2')
  
  def test_firstpass_mult_labels(self):  #multilabel 1st pass
    hack.pgm="(OUTPUT_FIRST) @R0 D=M (OUTPUT_D) @R2 M=D (INFINITE_LOOP) @INFINITE_LOOP".split()
    pgmv2=["@R0","D=M","@R2","M=D","@INFINITE_LOOP"]
    hack.first_pass()
    self.assertEqual(hack.symbol_table['OUTPUT_FIRST'],'{0:015b}'.format(0))
    self.assertEqual(hack.symbol_table['OUTPUT_D'],'{0:015b}'.format(2))  
    self.assertEqual(hack.symbol_table['INFINITE_LOOP'],'{0:015b}'.format(4))
    self.assertEqual(hack.pgmv2,pgmv2)

  def test_second_pass_A_inst(self):     #second pass
    self.initi()
    hack.pgmv2=["@R0","@21","@1000","@VAR1","@VAR2","D=D-M","@R3","D;JMP","D;JGT","JMP"]
    result="0000000000000000\n0000000000010101\n0000001111101000\n0000000000010000\n0000000000010001\n1111010011010000\n0000000000000011\n1110001100000111\n1110001100000001\n1111110000000000\n"
    self.assertEqual(hack.machine_code(),result)
    
if __name__=='__main__':
  unittest.main()

        

