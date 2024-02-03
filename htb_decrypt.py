from pwn import *

key = list(b"SUPERSECURE")
ENCRYPTED = read('login.xlsx.enc')

count = 0
flag = []

for byte in encrypted:
	flag.append(byte - key[count % len(key)])
	count += 1

print(flag)