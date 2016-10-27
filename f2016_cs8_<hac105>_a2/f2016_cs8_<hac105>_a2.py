def main():
    to_stop=False
    total_lines = 0
    total_distance = 0

    while not to_stop:
        print("1 : f2016_cs8_a2_data.1.csv")
        print("2 : f2016_cs8_a2_data.2.csv")
        filename = input("Which file do you wish to open? file 1 press 1, file 2 press 2 ")
        if filename == 1:
            current, distance = processfile1()
            total_lines = current
            total_distance = distance
            again = input('Do you want to add another file? Press 0 to add. If not press 8 ')
            if again == 0:
                new1, new2 = processfile2()
                total_lines = new1 + current
                total_distance = new2 + distance
            print("Total # of lines: " + str(total_lines))
            print("Total distance run: " + str(total_distance))
        elif filename == 2:
            current, distance = processfile2()
            total_lines = current
            total_distance = distance
            again = input('Do you want to add another file? Press 0 to add. If not press 8')
            if again == 0:
                new1, new2 = processfile1()
                total_lines = new1 + current
                total_distance = new2 + distance
            print("Total # of lines: " + str(total_lines))
            print("Total distance run: " + str(total_distance))
        else:
            print("File to be read: quit")
            print("Total # of lines: " + str(total_lines))
            print("Total distance run: " + str(total_distance))
            quit()

def processfile1():
     file_being_read = open('/Users/macbookpro/PycharmProjects/CS0008-f2016/f2016_cs8_<hac105>_a2/f2016_cs8_a2.data.1.csv', "r")
     current_lines = 0
     current_total_distance = 0
     for line in file_being_read:
        data = line.strip("\n")
        data = data.split(',')
        current_lines += 1
        current_total_distance += float(data[1])
     file_being_read.close()
     print("\nFile to be read: 1" )
     print("Partial Total # of lines : " + str(current_lines))
     print("Partial distance run     : " + str(current_total_distance))
     print("\n-------------------------------------\n")
     return (current_lines, current_total_distance)

def processfile2():
     file_being_read = open('/Users/macbookpro/PycharmProjects/CS0008-f2016/f2016_cs8_<hac105>_a2/f2016_cs8_a2.data.2.csv',"r")
     current_lines = 0
     current_total_distance = 0
     for eachline in file_being_read:
        data = eachline.strip("\n")
        data = data.split(',')
        current_lines += 1
        current_total_distance += float(data[1])
     file_being_read.close()
     print("\nFile to be read: 2" )
     print("Partial Total # of lines : " + str(current_lines))
     print("Partial distance run     : " + str(current_total_distance))
     print("\n-------------------------------------\n")
     return(current_lines, current_total_distance)


main()
