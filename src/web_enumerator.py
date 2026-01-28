import sys
import requests
try :
	if len(sys.argv)!=3:
		print("missing arguments")
except:
	sys.exit(1)
file = open(sys.argv[1],'r')
i=1
for line in file.readlines():
	print(f"Usecase n {i}")
	site=str(sys.argv[2])+'/'+line.strip('\n')
	response = requests.head(site)
	if response.status_code<400:
		print(line.strip('\n'))
	i+=1
