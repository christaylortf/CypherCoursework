import string,sys
from random import randrange


def sub1_e(message):
	cypher = ""
	#creates a alphabet of all chars in hex values
	alphabet = string.hexdigits

	for a in message:
		cypher = cypher + alphabet[((alphabet.index(a) + 2) % 21)]
	
	return cypher

def sub1_d(message):
	cypher = ""
        #creates a alphabet of lowercase ascii characters
        alphabet = string.hexdigits

        for a in message:
                cypher = cypher + alphabet[((alphabet.index(a) - 2) % 21)]

        return cypher
