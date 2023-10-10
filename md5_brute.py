#!/usr/bin/python

from termcolor import colored
import hashlib


def tryopen(wordlist):		# function to check if pass file exist if exist it will open the pass file
	global pass_file
	try:
		pass_file = open(wordlist, "r")
	except:
		print("No Suh File At That Path!")
		quit()

pass_hash = input("Enter MD5 Hash Value to decrypt: ")
wordlist = input("Enter Path To The Password File: ")
tryopen(wordlist)

for word in pass_file:
	print(colored("Trying: " + word.strip("\n"), 'red'))
	enc_wrd = word.encode('utf-8') 	#encoding need to word in utf 8 before making md5 hash of each word
	md5digest = hashlib.md5(enc_wrd.strip()).hexdigest() # hash generated from utf 8 encoded word

	if md5digest == pass_hash:	# check given hash with hash generated from wordlist
		print(colored("Password Found: " + word, 'green'))
		exit(0)

print(colored("Password Is Not In The List", 'yellow'))
