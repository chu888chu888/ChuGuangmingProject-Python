#-*-coding:utf-8-*-
import sys
import os
def main():
    sys.stdout.write("查看根目录下的目录\n")
    print os.listdir("/")
if __name__=="__main__":
    main()