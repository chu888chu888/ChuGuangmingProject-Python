#-*-coding:utf-8-*-
"""
我的第一个应用程序
"""
import sys
def Main():
    sys.stdout.write("开始程序\n")
    i=1
    print i,type(i),id(i)
    i=1000000000
    print i,type(i),id(i)
    i=1.1
    print i,type(i),id(i)
#下面的语句看起来比较奇怪，一会儿我们会解析它
if __name__=="__main__":
    Main()