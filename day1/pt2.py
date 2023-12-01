lines = [f.strip("\n") for f in open("input.txt")]
alllinenumbers=0

def linereplacer(line):
    line = line.replace("one", "1")
    line = line.replace("two", "2")
    line = line.replace("three", "3")
    line = line.replace("four", "4")
    line = line.replace("five", "5")
    line = line.replace("six", "6")
    line = line.replace("seven", "7")
    line = line.replace("eight", "8")
    line = line.replace("nine", "9")
    return line


for wholel in lines:
    firstnumber=""
    print(wholel)
    for linelength in range(len(wholel)):
        if(firstnumber!=""):
            break
        oldl = wholel[0:linelength]
        l = linereplacer(oldl)
        for letter in l:
            if letter.isnumeric():
                firstnumber=letter
                break
    lastnumber=""
    for linelength in range(len(wholel)):
        if(lastnumber!=""):
            break
        oldl = wholel[len(wholel)-linelength:len(wholel)]
        l = linereplacer(oldl)
        for letter in l:
            if letter.isnumeric():
                lastnumber=letter
                break
    actualnumber = firstnumber+lastnumber
    linefinalnumber=actualnumber[0]+actualnumber[-1]
    print(linefinalnumber)
    alllinenumbers+=int(linefinalnumber)


print(alllinenumbers)