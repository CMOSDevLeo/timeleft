#!/usr/bin/env python3 
# program gives you the time which it takes to view the remaining video in some multiplied time
# created symbolic for not having to type .py after timeleft

import sys
multi = int(sys.argv[1])
minutes = int(sys.argv[2])
result = 0

seconds = minutes * 60

if multi == 25:
    result = round(seconds/1.25)
elif multi == 5 or multi == 50:
    result = round(seconds/1.5)
elif multi == 75:
    result = round(seconds/1.75)
elif multi == 2:
    result = seconds/2
else:
    print("correct input: timeleft [multi] [timeleft in minutes]")

secDiff = seconds - result
newMin, newSec= divmod(result, 60)
minDiff, secDiff = divmod(secDiff, 60)

print ("At 1," + str(multi) + "x remaining time is: " + str(newMin) + "." + str(newSec))
print("\nYou'd safe " + str(minDiff) + "." + str(secDiff) + " minutes") 
