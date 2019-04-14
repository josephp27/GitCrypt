#!/bin/env/python

import os
from cryptography.fernet import Fernet

key = os.environ['ENCRYPTION_TOOLS_KEY']
print('Using key: ' + key)

def decrypt(path):
	print('Decrypting: ' + path)

	fernet = Fernet(key)
	with open(path, 'rb+') as file:
		data = file.read()
		header = b'ENCRYPTED_'

		if b'ENCRYPTED_' not in header:
			raise Exception()

		decrypt = fernet.decrypt(data[10:])
		
		file.seek(0)
		file.write(decrypt)
		file.truncate()
	

def decrypt_all_yml(path):

	for type_ in os.listdir(path):

		full_path = path + '/' + type_

		try:
			if 'application-' in type_:
				decrypt(full_path)
		except:
			print('File not encrypted aborting...MF')

		if os.path.isdir(full_path):
			decrypt_all_yml(full_path)


decrypt_all_yml(os.getcwd())