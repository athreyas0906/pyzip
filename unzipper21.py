def getdata(fname):
    fname1=fname+'zipper21.txt'
    lines=[]
    with open(fname1,'r') as f:
        lines=list(f.readlines())
    for i in range(len(lines)):
        lines[i]=lines[i][0:len(lines[i])-1]
        lines[i]=lines[i].split()
    for line in lines:
        for i in range(len(line)):
            line[i]=line[i].split('i')
    wrl=[]
    fname1=fname+'rank.txt'
    with open(fname1,'r') as f:
        wrl=list(f.readlines())
    for i in range(len(wrl)):
        wrl[i]=wrl[i][0:len(wrl[i])-1]
        wrl[i]=wrl[i].split()
    fname1=fname+'count.txt'
    uwc=[]
    with open(fname1,'r') as f:
        uwc=list(f.readlines())
    for i in range(len(uwc)):
        uwc[i]=uwc[i][0:len(uwc[i])-1]
    return lines,wrl
def decoder(lines,wrl):
    for line in lines:
        for wordNum in range(len(line)):
            index=line[wordNum]
            wrank,ind=int(index[0]),int(index[1])
            word=wrl[wrank][ind]
            line[wordNum]=word
    for i in range(len(lines)):
        if len(lines[i])==1:
            lines[i]=str(lines[i])
        else:
            lines[i]=' '.join(lines[i])
    for line in lines:
        print(line)
fname=input('enter file to decode : ')
lines,wrl=getdata(fname)
decoder(lines,wrl)
