def read_file(fname):
    fname1=fname+'.txt'
    with open(fname1,'r') as f:
        x=list(f.readlines())
    for i in range(len(x)):
        print(x[i])
        x[i]=x[i][0:len(x[i])-1]
        print(x[i])
    for i in range(len(x)):
        print(x[i])
        w=x[i].split()
        print(w)
        x[i]=w
    print(x)
    return x
#x is list of list of words in a line
def create_tree(fobj):
    letters=[]
    for line in fobj:
        for word in line:
            for letter in word:
                letters+=[letter]
    print(letters)
    count=[]
    for letter in letters:
        if [letter,letters.count(letter)] not in count:
            count+=[[letter,letters.count(letter)]]
    counting=[]
    print('count-',count)
    for i in count:
        counting+=[i[1]]
    counting.sort(reverse=True)
    print(counting)
    akeys={}
    cnum=0
    nrank=len(counting)
    lcount=len(count)
    for i in range(lcount):
        for j in count:
            if j[1]==counting[0] and akeys=={}:
                akeys[j[0]]=0
                count.remove(j)
                counting.pop(0)
            elif j[1]==counting[0]:
                lkeys=akeys.values()
                lkeys=list(lkeys)
                akeys[j[0]]=max(lkeys)+1
                count.remove(j)
                counting.pop(0)    
    print('akeys-',akeys)
    return akeys

def rem_last_dem(repWord1):
    repWord=''
    for i in range(len(repWord1)):
                if i!=len(repWord1)-1:
                    repWord+=repWord1[i]
    return repWord

def makeRLines(lines):
    rlines=[]
    for line in lines:
        newline = "3".join(line)
        newline+='4'
        rlines+=newline
    print(rlines)
    return rlines
        
def make_zip(lines,rank):
    rlines=[]
    for line in lines:
        for wordNum in range(len(line)):
            currWord=line[wordNum]
            repWord1=''
            for letter in currWord:
                repWord1+=str(rank[letter])+'2'
            repWord=rem_last_dem(repWord1)
            print(currWord,repWord)
            line[wordNum]=repWord
    print(lines)
    rlines=str(''.join((makeRLines(lines))))
    return rlines

def createZFile(rlines,fname):
    zfname=fname+'zipRank.txt'
    with open(zfname,'w') as f:
        f.write(rlines)

chk=True

while chk:
    print('zipRanker7374')
    print()
    print()
    print('Enter txt file name to zip : ')
    fname=input()
    print()
    fobj=read_file(fname)
    rank=create_tree(fobj)
    ndata=make_zip(fobj,rank)
    createZFile(ndata,fname)
    print('Zipped in new file with file name appended with zipRank')
    chk=bool(input('Press enter key or 0 to exit or any other key to stay : '))
                
    
                
    
        
