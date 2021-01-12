#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import csv
import fire
import os
import pathlib
import shutil
import pandas
import yaml
import re
import sys
import glob

for arg in sys.argv[2:]:
    for file in glob.iglob(arg):
        for line in open(file, 'r'):
            if re.search(sys.argv[1], line):
                print line,

    #ça marche oas



    jsonImm = pathlib.Path("liste-des-immeubles-proteges-au-titre-des-monuments-historiques.json")
dossierCible = pathlib.Path(dossierCible)

with open("liste-des-immeubles-proteges-au-titre-des-monuments-historiques.csv") as f:
    os.mkdir("cible2")
    os.chdir("cible2/")
#    for row in f:
#        os.mkdir(row.strip())
#    dframe = pd.read_table(‘liste-des-immeubles-proteges-au-titre-des-monuments-historiques.csv’, sep=’capet’)
    pattern = '^.*(Hugues|Capet|Robert|Henri|Phillipe|Louis|Jean I|Charles).*$'



    for data in dataJSONImm.fields:
        result = re.match(pattern, data["capétiens"])
        if result:
            os.chdir(data["reg"])
            os.chdir(data["dpt_lettre"])


for item in json_data:
    for data_item in item['data']:
        print data_item['name'], data_item['value']
