#!/usr/bin/python3

import csv
import sys
import os
import glob
import re

pattern = "full_tickets/ticket_*jpg"


files = glob.glob (pattern)
files.sort()
total_len = len(files)
# pad to multiple of 5
print (" total_len = " + str(total_len))
while total_len % 5 != 0 :
  files.append("blank_ticket.jpg")
  total_len = total_len + 1
print (" new total_len = " + str(total_len))
idx = 0
sheet=1
while idx <= total_len-5 :
  print(files[idx])
  print(files[idx+1])
  print(files[idx+2])
  print(files[idx+3])
  print(files[idx+4])
  cmd1 = "convert " + re.escape(files[idx]) + " " +  re.escape(files[idx+1]) + " " +  re.escape(files[idx+2]) + " " + re.escape(files[idx+3]) + " " + re.escape(files[idx+4]) + " -append  temp.jpg"
  cmd2 = "convert  ticket_cut_guide.jpg  temp.jpg -geometry +375+150 -composite ticket_out_sheet_" + str(sheet) + ".jpg"
  os.system(cmd1)
  os.system(cmd2)
  sheet=sheet+1
  idx = idx + 5

  


