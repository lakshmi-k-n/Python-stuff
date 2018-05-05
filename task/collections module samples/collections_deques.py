import collections
import sys


def deque_examples():
  d = collections.deque([1,3,2,43],10)
  d.append("a")
  print d,"<---initial"
  d.appendleft('left')
  print d,"<--after appending from left"
  d.append('right')
  print d,"<--after appending from right"
  print "popping from right:",d.pop()
  print "popping from left:",d.popleft()
  print "right rotation:"
  d.rotate(1)
  print d
  print "left rotation:"
  d.rotate(-1)
  print d
  d.extendleft("lakshmi")
  print d

deque_examples()
  
