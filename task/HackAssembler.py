import sys
import string
import re
import collections
#symbol_table={}
compmap={'0':"0101010",'1':'0111111','-1':'0111010','D':'0001100','A':'0110000','!D':"0001101",'!A':'0110001','-D':'0001111','-A':'0110011','D+1':'0011111','A+1':'0110111','D-1':'0001110','A-1':'0110010','D+A':'0000010','D-A':'0010011','A-D':'0000111','D&A':'0000000','D|A':'0010101','M':'1110000','!M':'1110001','-M':'1110011','M+1':'1110111','M-1':'1110010','D+M':'1000010','D-M':'1010011','M-D':'1000111','D&M':'1000000','D|M':'1010101'}


destmap={'M':'001','D':'010','MD':'011','A':'100','AM':'101','AD':'110','AMD':'111'}
jmpmap={'JGT':'001','JEQ':'010','JGE':'011','JLT':'100','JNE':'101','JLE':'110','JMP':'111'}


symbol_table={'R0':"000000000000000",'R1':"000000000000001",'R2':'{0:015b}'.format(2),'R3':'{0:015b}'.format(3),'R4':'{0:015b}'.format(4),'R5':'{0:015b}'.format(5),'R6':'{0:015b}'.format(6),'R7':'{0:015b}'.format(7),'R8':'{0:015b}'.format(8),'R9':'{0:015b}'.format(9),'R10':'{0:015b}'.format(10),'R11':'{0:015b}'.format(11),'R12':'{0:015b}'.format(12),'R13':'{0:015b}'.format(13),'R14':'{0:015b}'.format(14),'R15':'{0:015b}'.format(15),"SCREEN":'{0:015b}'.format(16384),"KBD":'{0:015b}'.format(24576),'SP':'{0:015b}'.format(0),"LCL":'{0:015b}'.format(1),"ARG":'{0:015b}'.format(2),"THIS":'{0:015b}'.format(3),"THAT":'{0:015b}'.format(4)}

pgm=[]   #extracted program from the plain file,stripped off of whitespaces and comments

pgmv2=[]   #extracted program from pgm after first pass


 # pre processing : stripping comments and whitespaces
def pre_process():
  global pgm
  fp=open(sys.argv[1])
  com=re.compile(r'//.*')
  textfp=com.sub('',fp.read())
  com=re.compile(r' +')
  textfp=com.sub('',textfp)
  pgm=textfp.split()
    
#first pass
def first_pass():
  global labels,pgmv2,pgm
  offset=0
  com=re.compile(r'^\((.*)\)')
  for i in range(0,len(pgm)):
    inst=pgm[i]
    match=com.search(inst)
    if match:
      symbol_table[match.group(1)]='{0:015b}'.format(i-offset)
      offset+=1
    else:
      pgmv2.append(inst)
  #print pgmv2,'\n\n',pgm,'\n\n',symbol_table
      
#second pass
def second_pass():
  global variables,compmap,destmap,jmpmap,pgmv2
  n=16
  hackF=open("file.hack","w")
  C_exp=re.compile(r'((.*)=)?([0!&|1ACDM+-]+)(;(.*))?')
  for line in pgmv2:
    if line.startswith("@"):  #if instruction is A instruction
      A_inst=line[1:]  
      if A_inst.isdigit():
        str='0'+'{0:015b}'.format(int(A_inst))
      else:
        if A_inst not in symbol_table :
          symbol_table[A_inst]='{0:015b}'.format(n)
          n+=1
        str='0'+symbol_table[A_inst]
    else:   #if instruction is C instruction
      C_inst=line
      match=C_exp.search(C_inst)
      dest=match.group(2)
      comp=match.group(3)
      jmp=match.group(5)
              #assigning bin values to c insts       
      comp_bin=compmap[comp]       #7bit value
      if dest=='' or dest==None:dest_bin='000'
      else:dest_bin=destmap[dest]
      if jmp=='' or jmp==None:jmp_bin='000'
      else:jmp_bin=jmpmap[jmp] 

      str='111'+comp_bin+dest_bin+jmp_bin
    hackF.write(str)
    hackF.write("\n")
  hackF.close() 
      

def main(): 
  """USAGE
     $ Hackassembler.py filename.asm
     OUTPUT
     Produces a hack file : file.Hack that contains translated binary strings of the given asm file.
  """
  pre_process()
  first_pass()
  second_pass()
if __name__=="__main__":
  main()
