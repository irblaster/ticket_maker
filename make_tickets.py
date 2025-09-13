#!/usr/bin/python3

import csv
import sys
import os


with open('full_list.csv', newline='') as csvfile:
     reader = csv.DictReader(csvfile)
     for row in reader:
        name = row ['name']
        table = row ['table']
        print (name)
        output_name = 'ticket_' + table + "_" + name
        output_name = output_name.replace(" ", "_")
        output_name = output_name.replace("&", "")
        output_name = output_name.replace(".", "")
        output_name = output_name + '.jpg'
        print (table)
        input_name = 'seth_bar_mitzvah_ticket_' + table + '.jpg'
        cmd1 = 'convert -background none -fill white -gravity Center -size 538x120 -font ./ariblk.ttf -pointsize 36 caption:"' + name + '" text_box.png'
        cmd2 = 'convert ' + input_name + ' text_box.png -geometry +1081+260 -composite ' + output_name
        os.system(cmd1)
        os.system(cmd2)



