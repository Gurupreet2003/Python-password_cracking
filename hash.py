#!/usr/bin/python

import hashlib

hashvalue = input("Enter a String To Hash: ")	# variable to get input the string which user want to hash

hashobj1 = hashlib.md5()			# hashobject is created for md5
hashobj1.update(hashvalue.encode())		# add sring/value to hash object then encode string to bytes
print(hashobj1.hexdigest())			# turn it into the md5 hash(hexadecimal string)


hashobj2 = hashlib.sha1()
hashobj2.update(hashvalue.encode())
print(hashobj2.hexdigest())

hashobj3 = hashlib.sha224()
hashobj3.update(hashvalue.encode())
print(hashobj3.hexdigest())


hashobj4 = hashlib.sha256()
hashobj4.update(hashvalue.encode())
print(hashobj4.hexdigest())


hashobj5 = hashlib.sha512()
hashobj5.update(hashvalue.encode())
print(hashobj5.hexdigest())
