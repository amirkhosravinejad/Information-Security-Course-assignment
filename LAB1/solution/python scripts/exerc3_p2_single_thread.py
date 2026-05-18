import requests

target = "http://10.10.16.87"
wordlist = "../../Downloads/lab1/wordlist"
extensions = [".php", ".html", ".txt", ".bat", ".sh", ".py"]

def iterate_extract_url(root_or_subdir, listt):
	with open(wordlist, "r") as f:
		for word in f:
			word = word.strip()
			if word == "":
				continue
			if root_or_subdir == 0:
				#print("salam")
				for ext in listt:
					url = f"{target}/{word}{ext}"
					send_req(url)
			else:
				for res in listt:
					url = f"{target}/{res}{word}{ext}"
					send_req(url)
						
def send_req(url):
	try:
		r = requests.get(url)
		if r.status_code in [200, 301, 302, 403]:
			print(f"Found file: {url}") 
	except:
		pass				
				
def files_in_root():
	
	print("...finding the files in root path...")
	iterate_extract_url(0, extensions)
				
def scan_subdirs():
	results_from_part1 = ["/test", "/sources", "/inprogress"]
	print("...scanning sub directories...")
	iterate_extract_url(1, results_from_part1)
	
def main():
	files_in_root()
	scan_subdirs()								
if __name__ == "__main__":
    main()
