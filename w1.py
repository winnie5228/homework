# encoding: utf-8

def coer(num):
    for x in xrange(num):
        print '*',
    print ''

def tringle(floor):
    for x in xrange(0,floor+1):
         coer(math(x))
        # print x
def math(num):
    return 2*num+1
    #呼叫 return 會返回值  藉由 return 可以把原來的值藉由公式化後轉出算出的值
def main():
    tringle(5)
    # print math(5)





if __name__ == '__main__':
    main()
    pass