"""
ROTX script
"""
import sys

def rotx(data, rotval):
    if len(data) == 0:
        return data
    output = []
    for d in data:
        if (not d.isalpha()) or (
                # cause
                # u'\xaa'.isalpha() == True
                # ^ wat
                ord(d) < ord('A') or
                ord(d) > ord('z')):
            output.append(d)
            continue
        off = 65
        if d.islower():
            off += 32
        output.append(chr((((ord(d) - off) + rotval) % 26) + off))
    return ''.join(output)

print(rotx(sys.argv[1], int(sys.argv[2])))
