#!/usr/bin/python


import crypt		# for crypt.crypt function
from termcolor import colored

def CrackPass(cryptWord,dict):
	salt = cryptWord[0:2]	# variable = crypt.crypt('word_to_encryot','salt'), where salt = 'any_two_alphabets'
	dictionary = open(dict, 'r')		# variable store and encrypted word with first two digit is salt
	for word in dictionary.readlines():
		word = word.strip('\n')
		crypt_Pass = crypt.crypt(word, salt)	# converting dictionary alphabets to encryption
		if(cryptWord == crypt_Pass):
			print(colored("Found Password: " + word, 'green'))
			return
	print("Password Not Found!")
	return



def main():
	pFile = input("Enter The Password File: ")
	passfile = open(pFile, 'r')
	dict = input("Enter The Dictionary File Path: ")
	for line in passfile.readlines():
		if ":" in line:
			user = line.split(':')[0]
			cryptWord = line.split(':')[1].strip(' ').strip('\n')
			print(colored("Cracking Password For: " + user, 'red'))
			CrackPass(cryptWord,dict)

main()
