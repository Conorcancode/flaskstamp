import datetime
from time import mktime, time

def parse(string):
    timeFormats = {'unix': None, 'utc': None}

    if(string == None):
        return currentTimeStamp(timeFormats)
        
    elif('-' in string):
        date = string.split('-')

        if(len(date) >= 3 and len(date) <= 5):
            return pastTimeStampUTC(date, timeFormats)
        else:
            return {'Error': 'Invalid Date'}
    elif(string.isdigit()):
        return pastTimeStampUnix(string, timeFormats)
    else:
        return {'Error': 'Invalid Date'}


def pastTimeStampUTC(date, timeFormats):
    dateNum = []
    
    for x in range(len(date)):
        dateNum.append(int(date[x]))

    timeStamp = datetime.datetime(dateNum[0], dateNum[1], dateNum[2])

    timeFormats['utc'] = timeStamp
    timeFormats['unix'] = mktime(timeStamp.timetuple())

    return timeFormats

def pastTimeStampUnix(stringDate, timeFormats):
    if(len(stringDate) < 11):
        intDate = int(stringDate)
        timeFormats['unix'] = intDate
        timeFormats['utc'] = datetime.datetime.utcfromtimestamp(intDate)

        return timeFormats

    else:
        return {'Error': 'Invalid Date'}

def currentTimeStamp(timeFormats):
    timeFormats['utc'] = datetime.datetime.now()
    timeFormats['unix'] = time()

    return timeFormats