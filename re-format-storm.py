import os
import re
import io


def format_file(fname):
    fh = open(fname, 'r')
    pref, ext = os.path.splitext(fname)
    #print ext
    new_name = "%s_ref%s"%(pref, ext)
    
    fh2 = open(new_name, 'w')
    line = ''
    while "da mo year  prcp" not in line:
        refline = "# %s"%line
        fh2.write(refline)
        line = fh.readline()
    temp_ = io.StringIO()
    if "da mo year  prcp" in line:
        refline = "%s%s%s%s%s%s%s%s%s\n"%('#'.ljust(1),\
                                          'id'.rjust(8),\
                                         'day'.rjust(8),\
                                         'month'.rjust(8),\
                                         'year'.rjust(8),\
                                         'Rain'.rjust(8),
                                         'Dur'.rjust(8),\
                                         'Tp'.rjust(8),\
                                         'Ip'.rjust(8))
        
        temp_.write(refline)
        
        refline = "%s%s%s%s%s%s%s%s%s\n"%('#'.ljust(1),\
                                          ' '.rjust(8),\
                                         ' '.rjust(8),\
                                         ' '.rjust(8),\
                                         ' '.rjust(8),\
                                         '(mm)'.rjust(8),
                                         '(h)'.rjust(8),\
                                         ' '.rjust(8),\
                                         ' '.rjust(8))
        temp_.write(refline)
    fh.readline()
    cnt = 0
    
    for line in fh:
        line = re.sub(' +', ' ', line)
        line = line.strip('\n')
        line = line.strip('\r')
        arr = line.split(' ')
        if len(arr) < 8:
            continue
        if float(arr[4]) <= 0.0:
            continue
        else:
            cnt+=1
            refline = "%s%s%s%s%s%s%s%s%s\n"%(' '.rjust(1),\
                                         str(cnt).rjust(8),\
                                         arr[1].rjust(8),\
                                         arr[2].rjust(8),\
                                         arr[3].rjust(8),\
                                         arr[4].rjust(8),
                                         arr[5].rjust(8),\
                                         arr[6].rjust(8),\
                                         arr[7].rjust(8))
            temp_.write(refline)
    fh.close()
    fh2.write("%i # The number of rain events\n"%cnt)
    fh2.write("0 # Breakpoint data? (0 for no, 1 for yes)\n")
    fh2.write(temp_.getvalue())
    fh2.close()


format_file('JordanSite.CLI')
