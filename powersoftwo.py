# Calculation of powers of 2

import sys

n = int(sys.argv[1])
power = 1
i = 0
print('power' + ' '*2 + 'value')
while i <= n:
    # Write the ith power of 2
    print (str(i) + ' '*6 + str(power ))
    power = 2 * power
    i += 1