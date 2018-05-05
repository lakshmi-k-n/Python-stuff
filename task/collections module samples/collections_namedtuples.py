from collections import namedtuple
import csv
import sys

def namedtupl():
  point = namedtuple('point',['x','y'],verbose=False)

  p = point(12,11)
  print p.x,p.y
 
def csv_processing():
  employee = namedtuple("employee","name age title dpt pay place dele rank level final")

  for emp in map(employee._make,csv.reader(open(sys.argv[1],"rU"))):
    print emp.name,emp.age



namedtupl() 
csv_processing()
