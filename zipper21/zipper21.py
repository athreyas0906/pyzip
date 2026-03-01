print('MADE BY ATHREYA, @athreyas0906 on github')
def read_file(fname):
    fname1=fname+'.txt'
    with open(fname1,'r') as f:
        lines=list(f.readlines())
    for i in range(len(lines)):
        lines[i]=lines[i][0:len(lines[i])-1]
    for i in range(len(lines)):
        l1=lines[i]
        l11=''
        for j in l1:
            if j.isalpha() or j==' ':
                l11+=j.lower()
        lines[i]=l11
    for i in range(len(lines)):
        w=lines[i].split()
        lines[i]=w
    return lines
#lines is list of list of words in a line, returns lines
def createwordlist(lines):
    wordlist=[]
    for line in lines:
        for word in line:
            wordlist+=[word]
    return wordlist
#wordlist is list of words in order
def uniquewords(wordlist):
    uniword=[]
    for word in wordlist:
        if [word,wordlist.count(word)] not in uniword:
            uniword+=[[word,wordlist.count(word)]]
    uwl=list(uniword)
    return uwl
#uniword is the list of (word,count of the word in file), returns uwl
def rankwords(uwl,fname):
    wordcount=[]
    for word in uwl:
        wordcount+=[word[1]]
    wordcount.sort(reverse=True)
    uniquewordcount=[]
    uwc=list(wordcount)
    for count in wordcount:
        if count not in uniquewordcount:
            uniquewordcount+=[str(count)+'\n']
    fname1=fname+'count.txt'
    with open(fname1,'w') as f:
        f.writelines(uniquewordcount)
    return uwc
#writes a count list in desc for reference, returns uwc
def ranklist(uwc,uwl,fname):
    wrl=[] #wordranklist
    luwl=len(uwl)
    uuwc=[]
    for i in uwc:
        if i not in uuwc:
            uuwc+=[i]
    luuwc=len(uuwc)
    for i in range(luuwc):
        cwl=[] #current rank words list
        maxuwc=uuwc[0]
        for pair in uwl:
            if pair[1]==maxuwc:
                cwl+=[pair[0]]
        uuwc.pop(0)
        cwl.sort()
        wrl+=[cwl]
    wrl1=[]
    for i in wrl:
        if len(i)==1:
            i1=str(i[0])
        else:
            i1=' '.join(i)
        wrl1+=[i1+'\n']
    fname1=fname+'rank.txt'
    with open(fname1,'w') as f:
        f.writelines(wrl1)
    return wrl
#makes rank list with words in order of occurance, returns wrl
def createzip(fname,wrl,uwl,uwc,lines):
    newlines=[]
    uuwc=[]
    for i in uwc:
        if i not in uuwc:
            uuwc+=[i]
    for line in lines:
        newline=[]
        for word in line:
            wcount=0
            wrank=0
            windex=0
            for pair in uwl:#find the frequency
                if pair[0]==word:
                    wcount=pair[1]
            for ind1 in range(len(uuwc)):#find rank of word using frequency(0 to len(uwc), in increasing order, with 0 being highest frequency)
                if uuwc[ind1]==wcount:
                    wrank=str(ind1)
            for ind2 in range(len(wrl[int(wrank)])):#find the index of word in wrl with index of its rank
                if wrl[int(wrank)][ind2]==word:
                    windex=str(ind2)
            walais=str(wrank)+'i'+str(windex)
            newline+=[walais]#add word alais to the list of new words in new line
        newlines+=[' '.join(newline)+'\n']#add the new line
    fname1=fname+'zipper21.txt'
    with open(fname1,'w') as f:
        f.writelines(newlines)
#makes the new zipped file
chk=True
while chk:
    print('zipper21')
    print()
    fname=input('Enter txt file name to zip : ')
    print()
    lines=read_file(fname)
    wordlist=createwordlist(lines)
    uwl=uniquewords(wordlist)
    uwc=rankwords(uwl,fname)
    wrl=ranklist(uwc,uwl,fname)
    createzip(fname,wrl,uwl,uwc,lines)
    chk=bool(input('Press enter key or 0 to exit or any other key to stay : '))
            
            
