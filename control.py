import sys
from to_hex import *
mode = sys.argv[1]

currentCypher = ""

if mode == "e":
	print "== Encrypt Mode =="
	print "Doing Encryption... 0%"	
	currentCypher = to_hex(sys.argv[2])
	print "Current Cypher is: " + currentCypher + " 25%"
elif mode == "d":
	print "== Decrypt Mode =="
	print "Doing Decryption 0%"
	currentCypher = from_hex(sys.argv[2])
	print "Current Cypher is: "+ currentCypher + " 25%"
else:
	print "Please select a valid mode (e/d)"
