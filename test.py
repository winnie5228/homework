# encoding: utf-8

def core(num):
    for x in xrange(num):
        print '*',
        #加,不跳行
    print ''
    #印空白是跳行
def tringle(floor):
    for x in xrange(0,floor+1):
        core(function(x))
def function(num):
    return 2*num+1

def main():
    tringle(3)

if __name__ == '__main__':
    main()
