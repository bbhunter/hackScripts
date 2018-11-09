import socket
import sys

f = open(sys.argv[1])
data = f.readlines()
f.close()
out = ""
for host in data:
	host = host.strip()
	try:
		ip = socket.gethostbyname(host)
	except:
		continue
	out += ", ".join([host, ip])+"\n"
j = open("resolved"+sys.argv[1], "w")
j.writelines(out)
j.close()

