import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import Lock
lock = Lock()
count = 0

target = "http://10.10.16.87"
wordlist = "../../Downloads/lab1/wordlist"
extensions = [".php", ".html", ".txt"]
MAX_THREADS = 20

def send_req(url):
    global count
    try:
        r = requests.get(url, timeout=5)
        if r.status_code in [200, 301, 302, 403]:
            print(f"[{r.status_code}] Found: {url}")
    except:
        pass
    with lock:
        count += 1
        print(f"\r  Progress: {count}", end="", flush=True)

def build_urls_root(extensions):
    urls = []
    with open(wordlist, "r") as f:
        for word in f:
            word = word.strip()
            if not word:
                continue
            for ext in extensions:
                urls.append(f"{target}/{word}{ext}")
    return urls

def build_urls_subdirs(subdirs):
    urls = []
    with open(wordlist, "r") as f:
        words = [w.strip() for w in f if w.strip()]
    for subdir in subdirs:
        for word in words:
            for ext in extensions:
                urls.append(f"{target}/{subdir}/{word}{ext}")
    return urls

def run_threaded(urls):
    with ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
        futures = {executor.submit(send_req, url): url for url in urls}
        for future in as_completed(futures):
            pass  # results already printed inside send_req

def files_in_root():
    print("...finding files in root path...")
    urls = build_urls_root(extensions)
    print(f"  -> {len(urls)} URLs queued")
    run_threaded(urls)

def scan_subdirs():
    subdirs = ["test", "sources", "inprogress"]
    print("...scanning subdirectories...")
    urls = build_urls_subdirs(subdirs)
    print(f"  -> {len(urls)} URLs queued")
    run_threaded(urls)

def main():
    files_in_root()
    scan_subdirs()

if __name__ == "__main__":
    main()
