#!/usr/bin/python3

import csv
import sys
import os
import glob


pattern = "ticket_*jpg"


files = glob.glob (pattern)

for filename in (files) :
  print (filename)


