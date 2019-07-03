import android
import os
import time
import sys

W = "\033[0m"
G  = '\033[32;1m'
R = '\033[31;1m'
os.system("apt install figlet ")
os.system('figlet AUTO')
os.system('figlet MESSAGE')
print R+"""HELLO IN MY TOOLS FOR SEND ONE MESSAGE TO MULTI NUMBERS THIS IS A PROBLEM WHICH THE WORLD SUFFER BECAUSE IT 
I DECIDE MADE THIS TOOL FOR HELP ME AND YOU IN WIN TIME 
IT 'S VERY IMPORTANT FOR A COMPANY 
DON'T FOGET SHARE """

'''Open android programs by importing '''
#_*_coding:utf-8_*_
droid = android.Android()
number = raw_input(W+"YOUR NUMBERLIST :")
message = raw_input(R+"WRITE YOUR MESSAGE:")

j = open(number,"r")
h = j.readlines()
for password in h:
   print G+'''SENDING {} TO {}'''.format(message,password)     
   droid.smsSend("{}".format(password),message
.encode("utf-8"))
   time.sleep(2)
'''founder by mzoir zakariya '''
