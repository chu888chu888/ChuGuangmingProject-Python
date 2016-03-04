#-*-coding:utf-8-*-
"""
my fist App
"""
import sys
import urllib
def Main():
    htmlresult=urllib.urlopen("http://www.baidu.com").read()
    print htmlresult
#this is test
if __name__=="__main__":
    Main()