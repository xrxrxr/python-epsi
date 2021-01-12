#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import csv
import os

#if os.path.isfile('cible/01,Ain,84,Auvergne-Rhône-Alpes/'):
#    print("File already exist =P 😛")
#else:



with open("departements-france.csv") as f:
    os.mkdir("cible")
    os.chdir("cible/")
    for row in f:
        os.mkdir(row.strip())
