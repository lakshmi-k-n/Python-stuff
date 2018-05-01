import os
import sys
import pipes


def checksum():
  list=[]
  md5=[]
  cmd="md5sum "
  
  for root,dirs,files in os.walk("/home/lakshmi/"):
    for file in files:
      if file.endswith("mp3"):
        path=os.path.join(root,file)
       # print path
        out=os.popen(cmd+pipes.quote(path))

        fil=out.read()
        outlist=fil.split()
        if outlist[0] not in md5:
          md5.append(outlist[0])
        else:
          list.append(path)
        out.close()  
  return list


def main():
  print checksum()

if __name__=="__main__":
  main()
