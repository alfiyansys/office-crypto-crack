import msoffcrypto
import os
import shutil
import pwd
import itertools

filename = "juli"
fileformat = "xlsx"
maxlength = 15

characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 "
#characters = "0123"
maxlength += 1
stop = False

def pw_guess(i):
	res = itertools.product(characters, repeat=i)
	for guess in res:
		yield guess

path = "./target/temp"
if os.path.exists(path) == False:
	print("creating temp folder")
	try:
		original_umask = os.umask(0)
		os.mkdir(path, 777)
	finally:
		os.umask(original_umask)
		shutil.chown(path, user=os.getuid(), group=os.getgid())

file = msoffcrypto.OfficeFile(open("./target/"+filename+"."+fileformat, "rb"))

for i in range(1,maxlength):
	guess_generator = pw_guess(i)
	for guess in guess_generator:
		passwd = ''.join(guess)
		gen_path = "target/temp/"+filename+"-"+passwd+"."+fileformat

		try:
			file.load_key(password=passwd)

			file.decrypt(open(gen_path, "wb"))
			print("ketemu password: "+passwd)
			stop = True
			break
		except:
			print("salah password: "+passwd)
			
			try:
				os.remove(gen_path)
			except:
				continue

	if stop == True:
		break
