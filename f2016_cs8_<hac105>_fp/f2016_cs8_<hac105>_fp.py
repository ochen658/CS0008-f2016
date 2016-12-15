# get a class
class participant:

    name = "don't know"
    # set an accumulator for distance and runs
    distance = 0
    # total number of runs by the participant
    runs = 0

    # use the initializer methods
    def __init__(self, name, distance=0):
        self.name = name
        # if distance is not zero we need to use if
        if distance > 0:
            # create a distance
            self.distance = distance
            # set number of runs accordingly
            self.runs = 1

    # addDistance method
    def addDistance(self, distance):
        if distance > 0:
            self.distance += distance
            self.runs += 1

    # addDistances method
    def addDistances(self, distances):
        # use for loop
        for distance in distances:
            if distance > 0:
                self.distance += distance
                self.runs += 1

    # This function will return the name of the participant
    def getName(self):
        return self.name

    # return the total distance run computed
    def getDistance(self):
        return self.distance

    # return the number of runs
    def getRuns(self):
        return self.runs

    # end def getRuns

    # stringify the object
    def __str__(self):
        return \
            "Name : " + format(self.name, '>20s') + \
            ". Distance run : " + format(self.distance, '9.4f') + \
            ". Runs : " + format(self.runs, '4d')
        # end def __init__

    # convert to csv
    def converttocsv(self):
        return ','.join([self.name, str(self.runs), str(self.distance)])
    # end def tocsv

# use getDataFromFlie method
def getDataFromFile(file):
    # create an empty list
    output = []
    # read file line
    for line in open(file,'r'):
        #first line that is the header
        if "distance" in line:
            continue
        # remove \n ending the line and split line at ","
        temp1 = line.rstrip('\n').split(',')
        # use try/except to avoid unhendled errors
        try:
            # append record to output list with name and distance
            # remove spaces from name and convert distance to float
            output.append({'name': temp1[0].strip(' '), 'distance':float(temp1[1])})
        except:
            print('Invalid row : '+line.rstrip('\n'))
    # return data records
    return output


# ask for master file from user
masterFile = input("Enter the master file : ")

# This part will read master file and get data files
try:
    dataFiles = [file.rstrip('\n') for file in open(masterFile,'r')]
except:
    print("Sorry I can't read master file or invalid file name")
    exit(1)

z = sum([getDataFromFile(file) for file in dataFiles],[])

number_Files_being_read = len(dataFiles)


# total number of lines read by using len()

totalLines = len(z)

# total number distance run by every participant is
# the sum of the "distance" element of the items in the list datas.
totalDistanceRun = sum([item['distance'] for item in z])

# create an empty dictionary
participants = {}

# loops on all the records
for item in z:
    if not item['name'] in participants.keys():
        participants[item['name']] = participant(item['name'])
    # insert distance in the list for this participant
    participants[item['name']].addDistance(item['distance'])
# end for

# initialize accumulators
# minum distance run with name
minDistance = { 'name' : None, 'distance': None }
# maximum distance run with name
maxDistance = { 'name' : None, 'distance': None }
# appearences dictionary
apparences = {}
#
# computes the total distance run for each participant iterating on all the participants
for name, object in participants.items():
    # get the total distance run by this participant
    distance = object.getDistance()
    # check if we need to update min
    if minDistance['name'] is None or minDistance['distance'] > distance:
        minDistance['name'] = name
        minDistance['distance'] = distance
    # check if we need to update max
    if maxDistance['name'] is None or maxDistance['distance'] < distance:
        maxDistance['name'] = name
        maxDistance['distance'] = distance

    # get number of runs, shows from participant object
    participant_shows = object.getRuns()
    #
    # check if we need to initialize this entry
    if not participant_shows in apparences.keys():
        apparences[participant_shows] = []
    apparences[participant_shows].append(name)
# end for

#
# compute total number of participant which is the length of the participantDistances
total_Participant = len(participants);

#use the len() method to count the total number of participants
totalNumberOfParticipantWithMultipleRecords = len([1 for item in participants.values() if item.getRuns() > 1])

# set format strings
INTEGER = '5d'
FLOAT = '12.5f'
STRING = '20s'


#output
print("")
print(" Number of Input files read   : " + format(number_Files_being_read,INTEGER))
print(" Total number of lines read   : " + format(totalLines,INTEGER))
print("")
print(" Total distance run           : " + format(totalDistanceRun,FLOAT))
print("")
print(" Max distance run             : " + format(maxDistance['distance'],FLOAT))
print("   by participant             : " + format(maxDistance['name'],STRING))
print("")
print(" Min distance run             : " + format(minDistance['distance'],FLOAT))
print("   by participant             : " + format(minDistance['name'],STRING))
print("")
print(" Total number of participants : " + format(total_Participant,INTEGER))
print(" Number of participants")
print("  with multiple records       : " + format(totalNumberOfParticipantWithMultipleRecords,FLOAT))
print("")


# this part is to create output file
outputFile = "f2016_cs8_hac105_a3.output.csv"
fh = open(outputFile,'w')
fh.write('name,records,distance\n')
for name, object in participants.items():
    fh.write(object.converttocsv() + '\n')
fh.close()

#file closed


