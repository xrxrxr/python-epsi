#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import csv
import os
import pandas as pd

with open("liste-des-immeubles-proteges-au-titre-des-monuments-historiques.csv") as f:
    os.mkdir("cible2")
    os.chdir("cible2/")
#    for row in f:
#        os.mkdir(row.strip())
    dframe = pd.read_table(‘liste-des-immeubles-proteges-au-titre-des-monuments-historiques.csv’, sep=’capet’)
export
