#!/usr/bin/env python3
# -*- coding: utf-8 -*-
##Iso-8859-1
import os
import csv


# Parent Directory path 
parent_dir = "~/projets/python-epsi"
# Directory 
directory = "python-epsi"
# Path 
path = os.path.join(parent_dir, directory) 


with open('departements-france.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ',
                            quotechar='|')
    for row in spamreader:
        print(', '.join(row))

  
if not os.path.exists(', '.join(row)):
            os.makedirs(', '.join(row))
            print("create folder " + ', '.join(row))


