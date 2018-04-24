"""This file is here to generate example sentences"""

"""A long list of examples of my code can be found at www.jesus-speak.tumblr.com where an automated code is posting once every 6 hours based on the Bible"""

import sys
sys.path.append('../')
import mchain as mc

tex = input("Name the file you want the sentences based on, or enter none to use the default\n--> ")
n = input("How many sentences do you want to generate? (Defaults to 1)\n--> ")
if n == "":
    n = 1
else:
    n = int(n)

if tex == "":
    doc = mc.portText("extext.txt")
else:
    doc = mc.portText(tex)

voc,M = mc.getMat(doc)
s = mc.genSent(voc,M,n)
print("\n",s)

if input("\nShould this be saved? (y/[n])\n--> ") == "y":
    R = open("examples.txt",'r')
    t = R.read()
    R.close()
    t += "\n\n"
    t += s
    R = open("examples.txt",'w')
    R.write(t)
    R.close()
