lines = [f.strip("\n") for f in open("input.txt")]
alllinenumbers=0
for l in lines:
    linenumbers=""
    for letter in l:
        if letter.isnumeric():
            linenumbers=linenumbers+letter
    linefinalnumber=linenumbers[0]+linenumbers[-1]
    print(linefinalnumber)
    alllinenumbers += int(linefinalnumber)
print(alllinenumbers)