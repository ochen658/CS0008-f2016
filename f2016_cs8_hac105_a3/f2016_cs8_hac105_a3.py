#
# MN: header missing
#
# Notes:
# MN: where are the comments?
#

# MN: what does this function do?
def sort_by_distance(data):
    return data['distance']


# MN: what does this function do?
def main():
    files_numb = 0
    filesbeing_read = []
    more_than_once = []
    total_distance = 0
    number_of_line = 0
    #
    # MN: output file should be named f2016_cs8_hac105_a3.data.output.csv
    #a = open('f2016_cs8_<hac105>_a3.data.output.csv', 'w')
    a = open('f2016_cs8_hac105_a3.data.output.csv', 'w')
    #
    # MN: I'm not sure why you are writing these following file paths in the output file
    a.write('/Users/macbookpro/PycharmProjects/CS0008-f2016/Ch1-Ex3/f2016_cs8_a3.data.1.csv\n')
    a.write('/Users/macbookpro/PycharmProjects/CS0008-f2016/Ch1-Ex3/f2016_cs8_a3.data.2.csv\n')
    a.write('/Users/macbookpro/PycharmProjects/CS0008-f2016/Ch1-Ex3/f2016_cs8_a3.data.3.csv\n')
    a.close()
    #
    # MN: why do you open a file named: monster input file.cvs?
    #     shouldn't you ask the user for the master file name
    #y = open('monster input file.cvs', 'r')
    masterfile = input("Please provide the master list file name : ")
    y = open(masterfile, 'r')
    for x in y:
        # MN: what is the purpose of this statment?
        x = x[0:-1]
        # MN: I assume that you are reading each data file here
        t = open(x, 'r')
        for line in t:
            number_of_line += 1
            # MN: skip header lines. they have distance in them
            if 'distance' in line:
                continue
            # end if
            line = line.rstrip()
            line = line.split(',')
            try:
                line[1] = float(line[1])
                total_distance += line[1]
            except:
                # MN: y is the file handle. why do you assign 0 to it?
                y = 0

            # MN: I'm not sure I understand what you are doing here
            #     what is k and what is filesbeing_read?            
            k = 0
            for s in filesbeing_read:
                if line[0] in s.values():
                    k = 1
                    try:
                        d1 = s.get('distance', 'Error')
                        value = d1 + line[1]
                        s['distance'] = float(value)
                        if line[0] in more_than_once:
                            y = 0
                        else:
                            more_than_once.append(line[0])
                    except:
                        y = 0
            # MN: are you inserting a participant for the first time here?
            if k == 0:
                new_data = {}
                new_data['name'] = line[0]
                new_data['distance'] = line[1]
                filesbeing_read.append(new_data)

    # MN: this throw an error. probably beacuse we still have the headers in the list and for header distance would be a string
    filesbeing_read.sort(key=sort_by_distance)
    # MN: I assumed that by the way you construct filesbeing_read, the lenght of this variable is equivalent 
    #     to the number of participants
    total_participant = number_of_line - 3 - len(more_than_once)

    # MN: why do you hard code the number of files? what if I insert 4 data files int he master file?
    print('Number of Input files read', 3)
    print('Total number of lines read', number_of_line - 3)
    print('total distance run ', total_distance)
    #
    # MN: how do you kow that this is going to be the max distance?
    date = filesbeing_read[-2]
    print('max distance run', date['distance'])
    print('name', date['name'])
    date1 = filesbeing_read[0]
    print('min distance run', date1['distance'])
    print('name', date1['name'])
    print('Total number of participants', total_participant)
    print('participants with multiple records', len(more_than_once))


main()
