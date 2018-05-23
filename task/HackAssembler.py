import sys
import string
import re
import collections
#symbol_table={}
compmap={'0':"0101010",'1':'0111111','-1':'0111010','D':'0001100','A':'0110000','!D':"0001101",''}
destmap={}
jmpmap={}


symbol_table={'R0':"0000000000000000",'R1':"0000000000000001",'R2':'{0:016b}'.format(2),'R3':'{0:016b}'.format(3),'R4':'{0:016b}'.format(4),'R5':'{0:016b}'.format(5),'R6':'{0:016b}'.format(6),'R7':'{0:016b}'.format(7),'R8':'{0:016b}'.format(8),'R9':'{0:016b}'.format(9),'R10':'{0:016b}'.format(10),'R11':'{0:016b}'.format(11),'R12':'{0:016b}'.format(12),'R13':'{0:016b}'.format(13),'R14':'{0:016b}'.format(14),'R15':'{0:016b}'.format(15),"SCREEN":'{0:016b}'.format(16384),"KBD":'{0:016b}'.format(24576),'SP':'{0:016b}'.format(0),"LCL":'{0:016b}'.format(1),"ARG":'{0:016b}'.format(2),"THIS":'{0:016b}'.format(3),"THAT":'{0:016b}'.format(4)}

pgm=[]
labels={}
pgm_real={}
pgmv2=[]
variables={}

def initial():
  global symbol_table
 # print symbol_table
def pre_process():
  global pgm_real,pgm
  fp=open(sys.argv[1])
  com=re.compile(r'//.*')
  textfp=com.sub('',fp.read())
  com=re.compile(r' +')
  textfp=com.sub('',textfp)
  pgm=textfp.split()
    
  #for i in range(0,len(pgm)):
   # pgm_real[i+1]=pgm[i]
  #print pgm_real  

def first_pass():
  global labels,pgmv2,pgm
  com=re.compile(r'^\((.*)\)')
  for i in range(0,len(pgm)):
    inst=pgm[i]
    match=com.search(inst)
    if match:
      labels[match.group(1)]='{0:016b}'.format(i)
    else:
      pgmv2.append(inst)
  print pgmv2,'\n',pgm,'\n',labels
      
       
def second_pass():
  global variables
  n=16
  hackF=open("file.hack","w")
  C_exp=re.compile(r'((.*)=)?([0!&|1ACDM+-]+)(;(.*))?')
  for line in pgmv2:
    if line.startswith("@"):  #if instruction is A instruction
      A_inst=line[1:]  
      if A_inst not in variables:
        variables[A_inst]='{0:015b}'.format(n)
        n+=1
      str='0'+variables[A_inst]
    else:   #if instruction is C instruction
      match=C_inst.search()
      dest=match.group(2)
      comp=match.group(3)
      jmp=match.group(5)
              #assigning bin values to c insts       
      comp_bin=compmap[comp]       #7bit value
      if dest=='' or dest==None:dest_bin='000'
      else:dest_bin=destmap[dest]
      if jmp=='' or jmp==None:jmp_bin='000'
      else:jmp_bin=jmpmap[jmp] 

      str='111'+comp+dest+jump
    hackF.write(str)
    hackF.write("\n")
  hackF.close() 
      

def main(): 
  pre_process()
  first_pass()
if __name__=="__main__":
  main()
