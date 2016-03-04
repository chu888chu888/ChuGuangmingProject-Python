
#-*-coding:utf-8-*-
import sys
def Main():
    test=['never',1,2,'yes',1,'no','maybe']
    print test[0:3]#包括test[0],不包括test[3]
    print test[0:6:2]#包括test[0],不包括test[6],而且步长为2
    print test[:-1]#包括开始，不包括最后一个
    print test[-3:]#抽取最后3个
if __name__=="__main__":
    Main()