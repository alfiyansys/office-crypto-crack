import msoffcrypto
import os

path = "./target/temp"
if os.path.exists(path):
	print("")
else:
	print("creating temp folder")
	os.mkdir(path, 777)

filename = "test"
file = msoffcrypto.OfficeFile(open("./target/"+filename+".xlsx", "rb"))

passwd="1234"

file.load_key(password=passwd)

try:
	file.decrypt(open("target/temp/"+filename+"-"+passwd+".xlsx", "wb"))
	print("ketemu password: "+passwd)
except:
	print("salah password: "+passwd)
