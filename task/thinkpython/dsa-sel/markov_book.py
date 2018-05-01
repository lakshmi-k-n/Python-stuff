import random
import sys

def process_file(filename):
  fp=open(filename)
  skip_header(fp)
  process_markov(fp)

def skip_header(fp):
  for line in fp:
    if line.startswith("*END*THE SMALL PRINT!"):
      break
def process_markov(fp):
  for line in fp:
    line=line.replace("-"," ")
    for words in line.split():
        



def main():
file = sys.argv[1]
process_file(file)


for i in range(200):
  print markov()

if __name__ == "__main__":
  main()





