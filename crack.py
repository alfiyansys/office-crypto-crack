import msoffcrypto
import os
import shutil
import pwd

filename = "test"
fileformat = "xlsx"

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

passwd="1234"

file.load_key(password=passwd)

try:
	file.decrypt(open("target/temp/"+filename+"-"+passwd+"."+fileformat, "wb"))
	print("ketemu password: "+passwd)
except:
	print("salah password: "+passwd)
	
