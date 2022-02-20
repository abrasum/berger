import csv
import argparse


# with open('588399947422-aws-billing-detailed-line-items-2015-09.c‌​sv') as csvfile: 
#    readCSV = csv.reader(csvfile,delimiter=',') 
#    for row in readCSV : 
#        print row



# Instantiate the parser
parser = argparse.ArgumentParser(description='Optional app description')
parser.add_argument('file', help='A required file path')

args = parser.parse_args()
file_path = args.file

def read_csv():
  print("test")

read_csv()