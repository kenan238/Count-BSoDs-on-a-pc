"""
Coded by kenan238
Scan how many BSoDs your pc had!
"""
import os
import sys
import time

def countBSODS():
    return len(next(os.walk("C:\\Windows\\minidump"))[2])
def loadAnim(t):
    mov=['|', '/', '-', '\\']
    for anim in range(t):
        for load in range(len(mov)):
            print(mov[load], end="\r")
            time.sleep(0.1)
start = input("Do you want to start scanning to see how many times your pc has got a BSOD?[y/n]:")
if start == "y" or "Y":
    print("Starting", end="")
    for i in range(20):
        print(".", end="")
        time.sleep(0.1)
    time.sleep(0.1)
    print("Ready")
    time.sleep(0.1)
    print("Scanning...")
    loadAnim(10)
    print("Your pc has got {} BSoD(s)".format(countBSODS()))
    time.sleep(60)
