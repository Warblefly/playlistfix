### PlaylistFix by John Warburton
### Takes an M3U8 playlist from Foobar2000
### and inserts the missing #EXTM3U and #EXTINF tags
### then writes a new playlist named similarly to the old playlist

SUFFIX    = "-fixed"
HEADER    = "#EXTM3U\n"
ITEMHEAD  = "#EXTINF\n"
EXTENSION = ".m3u8"


import os, sys

filename = sys.argv[1]

def plLoad(filename):
    ### Returns a list of strings, each string being
    ### one line from the original file
    ### Returns value None if the file is already
    ### considered 'fixed'

    with open(filename, encoding='utf-8-sig') as h:
        lines = h.readlines()
        
    print("We have read %d lines." % len(lines))
    
    if lines[0][:7] == "#EXTM3U" and lines[1][:7] == "#EXTINF":
        print("This file is already correct. No changes will be made.")
        return(None)

    return(lines)

out = list()

out.append(HEADER)

lines = plLoad(filename)

if lines == None:
    exit()

for item in lines:
    if item != '':
        out.append(ITEMHEAD)
        out.append(item)

outputFile = os.path.splitext(filename)[0] + SUFFIX + EXTENSION

print("Now writing the playlist %s" % outputFile)

with open(outputFile, 'w') as outfile:
    outfile.writelines(out)
