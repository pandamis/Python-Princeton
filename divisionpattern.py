import sys

n = int(sys.argv[1])

for i in range(1, n+1):
    line = ''
    # write ith row
    for j in range(1, n+1):
        if (i % j == 0) or (j % i == 0):
            line += '* '
        else:
            line += '  '
    print(line)
