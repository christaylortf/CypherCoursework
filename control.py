import sys
from to_hex import *
from sub1 import *

print "Encryption/Decryption system by Chris Taylor (12005101)"
mode = raw_input("Would you like to encrypt or decrypt (e/d)?\n ")
freeText = raw_input("What is the string?\n")

currentCypher = ""

if mode == "e":
	print "\n== Encrypt Mode =="
	print "Doing Encryption..."	
	currentCypher = to_hex(freeText)
	print currentCypher
	currentCypher = sub1_e(currentCypher)
	print currentCypher

	print "\n Your Encrypted Message is: \n " + currentCypher + "\n"
elif mode == "d":
	print "\n== Decrypt Mode =="
	print "Doing Decryption..."
	currentCypher = freeText
	print "Current Cypher is: \n" + currentCypher
	currentCypher = sub1_d(currentCypher)
	print currentCypher
	currentCypher = from_hex(currentCypher)
	print currentCypher
else:
	print "Please select a valid mode (e/d)"

