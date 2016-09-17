rt urllib.request
import re
import os
aaasd
#######################################`
##############################################
def lastnum(lastnum=None,fname='lottery_numbers.txt'):
    if lastnum!=None:
        return lastnum-1
    elif os.path.isfile(fname):

        f=open(fname,'r')
        data=f.read()
        f.close

        if (len(data)!=0):
d
            f=open(fname,'r')
            lnum=(f.readlines()[1]).split('\t')[0]
            f.close

            return (lnum)
aaaaa
sdsdf
a
    else:
        f=open(fname,'w')
        f.close()
        print('please input lastnum or check the file!')


#######################################
def pickall(url=None,x=10):
    nlist=[]
    ser=[]
    num=[]
    c=n=0

    while len(nlist) < x:

        if len(nlist)==0:
            html = urllib.request.urlopen(url).read()
        else:
            html = urllib.request.urlopen(url[:-6]+'_'+str(c)+url[-6:]).read()
        aa=str(html).split('height="35">')

        for bb in aa[1:]:


            if len(nlist)>=x:
                break

            ser.append(bb.split('</td>')[0])
            num.append((bb.split('</span>')[0]).split('<span>')[-1])
            num.append((bb.split('</span>')[1]).split('<span>')[-1])
            num.append((bb.split('</span>')[2]).split('<span>')[-1])
            num.append((bb.split('</span>')[3]).split('<span>')[-1])
            num.append((bb.split('</span>')[4]).split('<span>')[-1])
            num.append((bb.split('</span>')[5]).split('<span>')[-1])
            num.sort()
            num.append((bb.split('="blue">')[1]).split('\\n')[0])
            nlist.append(ser+num)
            num=[]
            ser=[]
            n+=1
            i=os.system('cls')
            print(format(n/x, '.1%'))
        c+=1
    return nlist


def pickrecent(url=None,lastnum=lastnum()):

    nlist=[]
    ser=[]
    num=[]
    c=n=0
    k=None

    while True :
        if k=='done':
            break
        elif len(nlist)==0:
            html = urllib.request.urlopen(url).read()
        else:
            html = urllib.request.urlopen(url[:-6]+'_'+str(c)+url[-6:]).read()
        aa=str(html).split('height="35">')

        for bb in aa[1:]:
            x=int(bb.split('</td>')[0])

            if x<=int(lastnum):

                k='done'
                break

            ser.append(bb.split('</td>')[0])
            num.append((bb.split('</span>')[0]).split('<span>')[-1])
            num.append((bb.split('</span>')[1]).split('<span>')[-1])
            num.append((bb.split('</span>')[2]).split('<span>')[-1])
            num.append((bb.split('</span>')[3]).split('<span>')[-1])
            num.append((bb.split('</span>')[4]).split('<span>')[-1])
            num.append((bb.split('</span>')[5]).split('<span>')[-1])
            num.sort()
            num.append((bb.split('="blue">')[1]).split('\\n')[0])
            nlist.append(ser+num)
            num=[]
            ser=[]
            n+=1
            i=os.system('cls')

            print(format((n/(int(int(nlist[0][0])-int(lastnum)))),'.1%'))
        c+=1

    return nlist


#####################################################


def output2file(content=None,k='d',fname='lottery_numbers.txt'):

    if os.path.isfile(fname):
        pass
    else:
        f=open(fname,'w')
        f.close()


    if k=='d':
        f=open(fname,'w')
        f.write('期数'+'\t'+'红球1'+'\t'+'红球2'+'\t'+'红球3'+'\t'+'红球4'+'\t'+'红球5'+'\t'+'红球6'+'\t'+'蓝球'+'\t'+'\n')
        for aa in content:
            for bb in aa:
                f.write(str(bb)+'\t')
            f.write('\n')
        f.close()

        print ("download complete!")
        return True


    elif k=='r' and content != []:

        f = open( fname, "r" )
        fcontent = f.read()
        f.close()
        pos = fcontent.find( "蓝球\t\n" )
        print (pos)

        if pos != -1:


            f = open( fname, "w" )
            f.write( fcontent[:pos+3] )
            f = open( fname, "a" )
            for aa in content:
                f.write('\n')
                for bb in aa:
                    f.write(str(bb)+'\t')

            f.write(fcontent[pos+3:])
            f.close()

            print ("refresh complete!")
            return True

        else:
            print ("refresh error!")
            return True
    elif content == []:
        print ('no update!')

    else:
        return None

x=336
url="http://www.cwl.gov.cn/kjxx/ssq/hmhz/index.shtml"
allnum=pickall(url,x)
output2file(allnum)
sfbit

'''

aa=lastnum()
print (aa)
bb=pickrecent(url,aa)
print (bb)
output2file(bb,'r')

'''
