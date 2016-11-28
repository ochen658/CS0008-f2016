#
# MN: header with user, instructor and course info is missing
#
# Notes:
# MN: no comments at all?

# MN: what does this function do?
def main():
 total_lines = 0
 total_distance = 0
 file=input('first file')
 while file and file!= 'q'and file!= 'quit':
    fh=open(file,'r')
    current, distance = processfile1(fh)
    printKV('Partial Total # of lines', current)
    printKV('Partial distance run', distance)
    fh.close()
    total_lines += current
    total_distance += distance
    file=input('next file')

 printKV(' Total # of lines',total_lines)
 printKV('Total distance run',total_distance)


# MN: what does this function do?
def processfile1(fh):
     current_total_distance = 0
     current_lines= 0
     for line in fh:
        data = line.rstrip("\n")
        data = data.split(',')
        current_lines += 1
        current_total_distance += float(data[1])
     fh.close()
     return (current_lines, current_total_distance)


# MN: what does this function do?
def printKV (key, value, klen=0):
    KL= max(len(key),klen)
    if isinstance(value, str):
        FS= '20s'
    elif isinstance(value, float):
        FS= '10.3f'
    elif isinstance(value, int):
        FS= '10'
    else:
        print("I don't know how to do it")
    print(format(key, str(KL))+'s', format(value, FS))

main()
