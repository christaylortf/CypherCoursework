import sys, collections
from random import randrange

letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9"]

#random number gen 
num = randrange(37)
print num

#generate key
key = collections.deque(letters)
key.rotate(num)

print letters
print "Shift by " + key[0]
print key
