#!/usr/bin/python3

# program gives you the time which it takes to view the remaining video in some multiplied time
# created symbolic for not having to type .py after timeleft

import sys
multi = float(sys.argv[1])
time = float(sys.argv[2])
result = 0

#print("multi:", multi)
#print("timeleft:", time)

if multi == 25:
    result = time/1.25
elif multi == 5 or multi == 50:
    result = time/1.5
elif multi == 75:
    result = time/1.75
elif multi == 2:
    result = time/2
else:
    print("correct input: timeleft [multi] [timeleft]")

diff = time - result

print ("At 1," + str(int(multi)) + "x remaining time is: " + str(round(result,2)))
print("\nYou'd safe " + str(round(diff,2)) + " minutes.")
