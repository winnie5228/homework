# encoding: utf-8

def core(num):
    for x in xrange(num):
        print '*',
    print ''  

def well(num):
    for x in xrange(num):
        print '#',
    print ''
def tringle(floor):
    for x in xrange(3,floor,-1):
        well(x)
        # print x
def tringle1(floor):
    for x in xrange(0,floor+1):
        core(math(x))

def math(num):
    return num*2+1      

def main():

    tringle1(2)
    tringle(0)
     

if __name__ == '__main__':
    main()