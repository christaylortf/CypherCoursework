import sys
from to_hex import *
from sub1 import *

print "Encryption/Decryption system by Chris Taylor (12005101)"
mode = raw_input("Would you like to encrypt or decrypt (e/d)?\n ")
freeText = raw_input("What is the string?\n")
num = raw_input("Passnumber:\n")

currentCypher = ""

if mode == "e":
	print "\n== Encrypt Mode =="
	print "Doing Encryption..."	
	
	# HEX
	currentCypher = to_hex(freeText)
	print currentCypher
	
	# Substitution1
	currentCypher = sub1_e(currentCypher,num)
	print currentCypher
	
	# Split String
	length = len(currentCypher)
	split1 = ""
	split2 = ""
	
	halflength = length/2
	for x in range (0,halflength):
		split1 += currentCypher[x]
	for x in range (halflength,length):
		split2 += currentCypher[x]
	
	print "Split1: " + split1 + "\n Split2: " + split2
	
	# Split1 Substitution 2
	split1 = sub1_e(split1,num)
	
	# Split2 Substitution 3
	split2 = sub1_e(split2,num)
	
	# Merge split1 and split2
	currentCypher = "" + split1 + split2
	
	#Substitution 4
	currentCypher = sub1_e(currentCypher,num)
	
	# Print Final
	print "\n Your Encrypted Message is: \n " + currentCypher + "\n"
elif mode == "d":
	print "\n== Decrypt Mode =="
	print "Doing Decryption..."
	
	currentCypher = freeText
	
	# Substitution 4
	currentCypher = sub1_d(currentCypher,num)
	
	#Split string
	length = len(currentCypher)
	split1 = ""
	split2 = ""
	
	halflength = length/2
	for x in range (0,halflength):
		split1 += currentCypher[x]
	for x in range (halflength,length):
		split2 += currentCypher[x]
		
	print "Split1: " + split1 + "\n Split2: " + split2
	
	# Split1 Substitution 2 
	split1 = sub1_d(split1,num)
	
	# Split2 Substitution 3
	split2 = sub1_d(split2,num)
	
	# Merge split 1 and split 2
	currentCypher = "" + split1 + split2
	
	# Substitution1
	currentCypher = sub1_d(currentCypher,num)
	print currentCypher
	
	# HEX
	currentCypher = from_hex(currentCypher)
	print currentCypher
	
	print "\n Your Decrypted Message is: \n " + currentCypher + "\n"
else:
	print "Please select a valid mode (e/d)"

