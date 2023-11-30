import csv
import sys

with open(sys.argv[1], 'r') as f:
    lineIdx = int(sys.argv[2])
    columnIdx = int(sys.argv[3])
    reader = csv.reader(f)

    for i, row in enumerate(reader):
        if i == lineIdx:
            print(row[columnIdx])

