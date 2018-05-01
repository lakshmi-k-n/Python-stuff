#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them
def parse_dir(dirlist):
  result=[]
  for i in dirlist:
    items=os.walk(i)
  print '\n\n'
  for root,dir,files in items:
    for i in files:
      if re.search(r'__\w+__',i):
        result.append(os.path.abspath(os.path.join(root,i)))
  return result
  
def copy_dirs(loc,dirlist):
  files=parse_dir(dirlist)
  for i in files:
      shutil.copy(i,loc)
def zip_dirs(zipfile,dirlist):
  cmd = 'zip -j ' + zipfile + ' '+dirlist
  #print dirlist
  print "Command to run:" + cmd   ## good to debug cmd before actually running it
  (status, output) = commands.getstatusoutput(cmd)
  if status:    ## Error case, print the command's output to stderr and exit
    sys.stderr.write(output)
    sys.exit(status)
  print output


def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
    sys.exit(1)
  if args[0] != '--todir' and args[0] != '--tozip':
    print '\n'.join(parse_dir(args))
  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]
    copy_dirs(todir,args)

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]
    args1=' '.join(parse_dir(args))
    zip_dirs(tozip,args1)

  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)

  # +++your code here+++
  # Call your functions
  
if __name__ == "__main__":
  main()
