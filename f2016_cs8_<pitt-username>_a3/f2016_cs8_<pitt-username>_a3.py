def sort_by_distance(data):
    return data['distance']
def main():
    decision = 'Y'
    files_numb=0
    filesbeing_read = []
    total_distance = 0
    number_of_line = 0
    while decision == 'Y':
        files_numb+=1
        x = input('Which file would you like to open?')
        y = open(x,'r')
        for line in y:
            number_of_line += 1
            line = line.rstrip()
            line = line.split(',')

            try:
                line[1] = float(line[1])
                total_distance += line[1]
            except:
                y = 0
    #In this part I am trying to determine whether the participants have multiple records, but the output gives
                #me zero all the time.
            k = 0
            for t in filesbeing_read:
                if line[0] in t.values():
                    k = 1
                    try:
                        d1 = line.get('distance','Error')
                        value = d1 + line[1]
                        t['distance'] = value
                        t['multiple'] = 1
                    except:
                        y = 0
            if k == 0:
                new_data = {}
                new_data['name'] = line[0]
                new_data['distance'] = line[1]
                filesbeing_read.append(new_data)
            x=0
            for line in filesbeing_read:
                if len(line)== 3:
                    x += 1
        decision = input('Would you you like to open another file?Press "Y" to read file. ')
    filesbeing_read.sort(key = sort_by_distance)
    print('participants with multiple records',x)
    print('Number of Input files read',files_numb)
    print('Total number of lines read',number_of_line-files_numb)
    print('total distance run ',total_distance)
    date = filesbeing_read[-2]
    print('max distance run', date['distance'])
    print('name',date['name'])
    date1= filesbeing_read[1]
    print('min distance run', date1['distance'])
    print('name',date1['name'])
main()