import csv
import argparse

table = []

with open('table1.csv') as csvfile: 
    readCSV = csv.reader(csvfile,delimiter=',')
    for row in readCSV:
        table.append(row)

count_players = len(table[1:])
count_col_table = len(table[0][0])
summary_list = []

for row in table[1:]:
    summary_list.append(float(row[len(row) - 1]))

print(summary_list)

berger_list = []


for row in table[1:]:
    player_id = 0
    brg = 0
    for col in row[2:len(row) - 2]:
        summary = summary_list[player_id]
        if col == "1":
            brg = brg + summary
        if col == "0.5" or col == "0,5" or col == '1/2':
            brg = brg + summary/2
        player_id += 1
    berger_list.append(brg)

print(berger_list)