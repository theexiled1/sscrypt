#!/usr/bin/env python
"Instagram: @SSploit\nTwitter: @SecuritySploit\nYouTube: Blackhole Security\nGithub: BlackholeSec\n\nSSCrypt (SecSploit Encryption)\nThis Encryption uses custom mathematical algoritms to ensure the privacy of your data whether it be clandestine or merely for privacy"
import random
import os
import sys
import binascii
class desolation_error(Exception):
	pass
def __encode_data(data):
	enc_str = ""
	for char in data:
		enc_str = enc_str + binascii.hexlify(char) + " "
	end_val = ""
	for val in enc_str.split(' '):
		end_val = end_val + binascii.hexlify(val) + " "
	return end_val
def __decode_data(data):
	dec_str = ""
	for char in data.split(" "):
		dec_str = dec_str + binascii.unhexlify(char)
	dec_str = binascii.unhexlify(dec_str)
	return dec_str
def __gen_key(key):
	key_val = str(__encode_data(key))
	key_value = ""
	for c in key_val.split(" "):
		key_value = key_value + c
	key_value = int(key_value)
	calc = key_value ** (len(key) % key_value) / (len(str(key_value)) % key_value)
	calc = calc / (2 + (16 % len(key))) // (8 + (len(str(key_value)) / 32 + (len(str(calc)) ** 2)))
	calc = calc - 82 + len(str(calc)) * (key_value / 32) ^ 256 >> 6
	calc = calc | 32 / (len(str(key_value)) % 512) << 2 * (512 * len(str(key_value)[:2])) + 1024 / len(str(calc))
	calc = (calc + calc) % len(str(calc)) / len(str(key_value)) << len(key) ^ (16 ** len(str(key_val)))
	calc = (calc ** 32) % len(str(key_value)) + 16 ** len(str(key_val)) + 1024 ^ len(str(key_val))
	calc = calc ** len(str(key_value)) + 128 >> len(str(key_val)) + (len(str(key_value)) + 16) / 1024
	calc = calc / len(str(key_val)) - len(str(key_val)) + 2
	return calc
def __encrypt_data(key_calc,data):
	enc_msg = ""
	for val in str(data.strip()).split(" "):
		enc_msg = enc_msg + str(int(val) * key_calc) + ":"
	return enc_msg
def __decrypt_data(key_calc,data):
	dec_msg = ""
	for val in str(data).strip().split(":"):
		try:
			dec_msg = dec_msg + str(int(str(val)) / key_calc)
		except:
			pass
	dec_msg = __decode_data(dec_msg)
	return dec_msg
def encrypt(data,key):
	"Use this function for encrypting clandestine data\nUsage encrypt('message','password')"
	enc_data = __encrypt_data(__gen_key(key),__encode_data(data))
	return enc_data
def decrypt(data,key):
	"Use this function for decrypting encrypted data\nUsage decrypt('encrypted message','password')"
	dec_data = __decrypt_data(__gen_key(key),data)
	return dec_data
def encrypt_file(file,key):
	"Use this function for encrypting clandestine files\nUsage encrypt_file('filename.ext','password')"
	try:
		with open(file, 'r') as fhandler:
			data = fhandler.read()
			if(len(str(data).strip()) == 0):
				raise desolation_error("File is empty, there is nothing to encrypt.")
				exit(1)
			fhandler.close()
	except Exception as e:
		sys.stdout.write(str(e))
		sys.stdout.flush()
		exit(1)
	try:
		for i in range(80):
			with open(file, 'w+') as fhandler:
				fhandler.truncate()
				fhandler.write(str(random.SystemRandom().getrandbits(1024)))
				fhandler.close()
		lname = file
		for i in range(80):
			nname = str('0' * int(random.SystemRandom().randint(1,15)))
			os.rename(lname,nname)
			lname = nname
		os.remove(lname)
	except:
		raise
	try:
		with open(file,'w+') as fhandler:
			fhandler.write(encrypt(data,key))
			fhandler.close()
	except:
		raise
def decrypt_file(file,key):
	"Use this function for decrypting encrypted files\nUsage decrypt_file('filename.ext','password')"
	try:
		with open(file, 'r') as fhandler:
			data = fhandler.read()
			if(len(str(data).strip()) == 0):
				raise desolation_error("File is empty, there is nothing to decrypt.")
				exit(1)
			fhandler.close()
	except Exception as e:
		sys.stdout.write(str(e))
		sys.stdout.flush()
		exit(1)
	try:
		for i in range(80):
			with open(file, 'w+') as fhandler:
				fhandler.truncate()
				fhandler.write(str(random.SystemRandom().getrandbits(1024)))
				fhandler.close()
		lname = file
		for i in range(80):
			nname = str('0' * int(random.SystemRandom().randint(1,15)))
			os.rename(lname,nname)
			lname = nname
		os.remove(lname)
	except:
		raise
	try:
		with open(file,'w+') as fhandler:
			fhandler.write(decrypt(data,key))
			fhandler.close()
	except:
		raise
