import os
import datetime as dt


def complete_to_max(string_to_expand):
    out_string = '{:^46}'.format(string_to_expand)
    return out_string


name = "Jordan Amman Airport"

latitude = '{degree:3d}{minutes:2d}'.format(degree=31, minutes=43)
longitude = '{degree:3d}{minutes:2d}'.format(degree=360-35, minutes=59)
elevation = '{:6d}'.format(730)

header = "40250"+complete_to_max(name)+latitude+"  "+longitude+elevation+"\n"
fhout = open('JordanSite.GDS', 'w')
fhout.write(header)
fhin = open('JordanSite.txt', 'r')
#Reads header
fhin.readline()
for line in fhin:
    line = line.strip('\n')
    line = line.strip('\r')
    arr = line.split('\t')
    if line:
        date_ = dt.datetime.strptime(arr[0], "%m/%d/%Y")
        if arr[4] != '':
            maxT = '{:5.0f}'.format(float(arr[4])*10)
        else:
            maxT = '{:5.0f}'.format(-999)
        if arr[5] != '':
            minT = '{:5.0f}'.format(float(arr[5])*10)
        else:
            minT = '{:5.0f}'.format(-999)
        if arr[6] != '':
            P = '{:5.0f}'.format(float(arr[6])*10)
        else:
            P = '{:5.0f}'.format(-999)
        
        fhout.write('%s%s  %s  %s\n'%(date_.strftime("%y%m%d"), maxT, minT, P))
fhout.close()
fhin.close()
