#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import csv
import os

with open("departements-france.csv") as f:
    os.chdir("cible/")
    for row in f:
        os.mkdir(row.strip())
