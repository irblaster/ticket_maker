#!/bin/bash
convert -background none -fill white -gravity Center -size 540x100 -font ./ariblk.ttf -pointsize 26 caption:"Mr. & Mrs. Michael Libeskind" text_box.png
convert seth_bar_mitzvah_ticket_blank.jpg text_box.png -geometry +1082+282 -composite output_image9.jpg

