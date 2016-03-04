#-*-coding:utf-8-*-
import sys
def Main():
    array=[1,2,3]
    print array[0]
    #输出1
    array[0]='a'
    print array
    #输出['a',2,3]
    L=[123,'spam',1.23]
    #输出大小
    print len(L)
    print L[0]
    print L[:-1]#不包含最后一个
    print L+[4,5,6]#重新拼接一个新的列表
if __name__=="__main__":
    Main()