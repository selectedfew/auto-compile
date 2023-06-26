#!/usr/bin/python3

import os
import sys
import platform
import time

'''
SFXCompiler
>>> python xapp.py

All this script does is automatically compiles
the c++ test.cpp into an executable and then
executes the app after words.
'''

#x = eXecute
class XCompiler:

  def __init__(self):
    print("""\033[1;92m\nXCompiler [Ricardo Ortega - selectedfew@yahoo.com]\n\036""")
    '''print("   System:",platform.system(),os.name)
    print(" Platform:",platform.platform())
    print("Architect:",platform.machine())'''

  def checkIfRoot(self):
    if not os.getuid() == 0:
      sys.exit("""\033[1;91m\nMust run w/ Root[!]\n\033""")

  def initBlueText(self):
    print("""\033[1;94m\n\036""")

  def compileFile(self):
    time.sleep(1)
    removeCachePkgsNotInstalled = os.system("g++ -std=c++20 tests.cpp -o app")
    
  #Safety for debugging purposes
  def compileFileWithSecurity(self):
    time.sleep(1)
    compileFileWithSecurityArguments = os.system("g++ -std=c++20 -m32 -g -lpthread -fno-stack-protector tests.cpp -o app -z execstack -D_FORTIFY_SOURCE=0")
    
  def eXecuteFile(self):
    time.sleep(1)
    removeCachePkgsNotInstalled = os.system("./app")



def main():

  x = XCompiler() #Initialize
  x.checkIfRoot() #Check if root first...
  x.initBlueText() #Change text to blue
  
  #Can only choose one, so I commented this out x.compileFile() #For regular compiling
  x.compileFileWithSecurity()#For debugging
  
  x.eXecuteFile()

main()

