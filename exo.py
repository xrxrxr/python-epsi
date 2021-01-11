#!/usr/bin/env python3
import csv
import os
with open('departements-france.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ',
                            quotechar='|')
    for row in spamreader:
        print(', '.join(row))
    for each in spamreader:
        mdkir(', '.join(row))
