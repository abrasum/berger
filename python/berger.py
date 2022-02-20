import csv
import argparse

def openCsv(filename = ""):
    table = []
    with open(filename) as csvfile: 
        readCSV = csv.reader(csvfile,delimiter=',')
        for row in readCSV:
            table.append(row)
    return table


def calcBerger(table = []):
    summary_list = []
    for row in table[1:]:
        summary_list.append(float(row[len(row) - 1].replace(',','.')))
    berger_list = []
    for row in table[1:]:
        player_id = 0
        brg_list = []
        for col in row[2:len(row) - 1]:
            final_result = summary_list[player_id]
            if col == "1":
                brg_list.append(final_result)
            if col == '0.5' or col == '0,5' or col == '1/2':
                brg_list.append(final_result/2)
            player_id += 1
        berger_list.append(sum(brg_list))
    return berger_list

def writeCsv(filename = "", table = [], berger = []):
    berger.insert(0,'berger')
     
    with open(filename, 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        i = 0
        for row in table:
            row.append(berger[i])
            spamwriter.writerow(row)
            i += 1

parser = argparse.ArgumentParser(description='Berger')
parser.add_argument('-file', type=str, help='Input path to file with table')
parser.add_argument('-out', type=str, help='File name for output result')

args = parser.parse_args()
file = args.file
output = args.out
table = openCsv(file)
berger = calcBerger(table)
writeCsv(output,table,berger)
