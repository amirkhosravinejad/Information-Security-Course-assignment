import requests

target = "http://10.10.16.87"
wordlist = "../../Downloads/lab1/wordlist"

with open(wordlist, "r") as f:
	for word in f:
		word = word.strip()
		url = f"{target}/{word}"
		try:
			r = requests.get(url)
			if r.status_code in [200, 301, 302, 403]:
				print(f"Found directory: {url}")
		except:
			pass		
