import sys

def launch():
    filename = getArguments()
    filecontent = getFileContent(filename)
    filearray = transformInArray(filecontent)
    filetab = findTheBestSquare(filearray)
    result = redraw(filetab, filearray)
    print(result)

def getFileContent(file):
    with open(file, 'r') as content:
        return content.read()

def getArguments():
    if len(sys.argv) != 2:
        print('please pass only one argument !')
        sys.exit(0)
    return sys.argv[1]

def transformInArray(filecontent):
    return filecontent.split("\n")

def redraw(filetab, filearray):
    a = -1
    line = []
    for x in filearray:
        a = a + 1
        b = -1
        for y in x:
            b = b + 1
            line.append(y)
            for z in filetab:
                var = z.split(':')
                if a == int(var[0]) and b == int(var[1]):
                    filetab.remove(z)
                    line[-1] = 'x'
        line.append('\n')
    return ''.join(line) 

def findTheBestSquare(filetab):
    tab = []
    temporarytab = []
    alttab = []
    for x in range(0, len(filetab)):
        for y in range(0, len(filetab[x])):
            if filetab[x][y] == 'o':
                temporarytab.clear()
            if filetab[x][y] == '.':
                temporarytab.append(str(x) + ":" + str(y))
                if len(temporarytab) > 1:
                    for a in temporarytab:
                        test = a.split(':')
                        for b in range(1, len(temporarytab)):
                            if int(test[0]) + b >= len(filetab):
                                alttab.clear()
                                break
                            if filetab[int(test[0]) + b ][int(test[1])] == '.':
                                alttab.append(str(int(test[0]) + b) + ':' + test[1])
                            if filetab[int(test[0]) + b ][int(test[1])] == 'o':
                                alttab.clear()
                                temporarytab.clear()
                                break
                        if len(alttab) == 0:
                            break
                    if len(alttab) > 0:
                        if len(tab) < len(temporarytab) + len(alttab):
                            tab = temporarytab + alttab
                        alttab.clear()
    return tab
