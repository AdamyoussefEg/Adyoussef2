#مشروع جدول الضرب
from pystyle import *
print(Box.Lines(" [+] Learn python with Adam [+] "))
Write.Print(" [+] This program for simple Cal. \n",Colors.blue_to_red,interval=0.1)
print(Box.DoubleCube("Example [3]"))
while True:
    Numbers = int(Write.Input(" [+] write your number :",Colors.white_to_blue,interval=0.1) )
    for i in range(1,11):
        print(Numbers,"x",i,"=",Numbers*i)