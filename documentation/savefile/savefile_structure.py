"""Script to output Savefile content for HMDS"""

import sys, getopt, re, json

def getSavefileTable():
    markdownFile = open("./savefile_structure.md", "r")
    markdownContent = markdownFile.read()
    markdownFile.close()

    markdownTable = re.findall("^\| .{10,}\|$", markdownContent, re.M)

    markdownTableList = []
    for row in markdownTable:
        item = row.split("|")
        markdownTableList.append(item[1:4])
    return markdownTableList

def getSavefileContent(inputfile):
    file = open(inputfile, "rb")
    content = file.read()
    file.close()
    return content

def getSavefileInfo(start:int, length:int):
    end = start + length
    textArray = content[start:end]
    text = ""
    for char in textArray:
        text += chr(char)
    return text

def getMultilineSavefileInfo(range, length: int, item: str):
    range = "".join(range.split())
    range = range.split("-")
    start = int(range[0], 16)
    i = 1
    while start != int(range[1], 16):
        printSavefileInfo(start, length, f"{item} {str(i)}")
        start = start + 16
        i = i + 1

def printSavefileInfo(start: int, length: int, item: str):
    print(f"{item}:", getSavefileInfo(start, length))

inputfile = ''
outputfile = ''
try:
    arguments, values = getopt.getopt(sys.argv[1:],"ho:i:",["infile=","outfile="])
except getopt.GetoptError:
    sys.exit(2)
for opt, arg in arguments:
    if opt == '-h':
        print("-i input -o output ")
        sys.exit()
    elif opt in ("-i", "--infile"):
        inputfile = arg
    elif opt in ("-o", "--outfile"):
        outputfile = arg
if inputfile == "":
    print("No input has been given")
    sys.exit(2)
if outputfile == "":
    outputfile = inputfile

table = getSavefileTable()

content = getSavefileContent(inputfile)

print(f"{table[0][2].rstrip()}: Value")
for row in table[1:]:
    if re.search("-", row[0]):
        getMultilineSavefileInfo(row[0], int(row[1]), row[2].rstrip())
    else:
        printSavefileInfo(int(row[0], 16), int(row[1]), row[2].rstrip())
