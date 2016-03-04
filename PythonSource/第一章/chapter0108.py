#-*-coding:utf-8-*-
"""
字符串例子
"""
import sys
def Main():
    sys.stdout.write("开始程序\n")
    str1='i am "python"\n'
    str2="i am 'Python' \r"
    str3="""
               i'm "Python",
               <a href="http://www.sina.com.cn"></a>
         """
    #你可以把html之类的东西都直接弄进来而不需要处理
    print str1,str2,str3
if __name__=="__main__":
    Main()