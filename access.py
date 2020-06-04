import requests
from urllib.parse import urlparse
import re
path = "list.txt"
# 国立大学一覧　= https://www.mext.go.jp/b_menu/link/daigaku1.htm
def read_list():
	with open(path,"r") as f:
		urllist = []
		for url in f:
			url = url.rstrip('\n')
			parsed_url=urlparse(url)
			url = '{uri.scheme}://{uri.netloc}/'.format(uri=urlparse(url))
			urllist.append(url)
	return urllist

def access(url):
	try:
		r = requests.get(url)
		code = r.status_code
	except:
		code = -1 
	return code

def main():
	urllist = read_list()

	for i in urllist:
		print(i[:-4],end=" ")
		print(access(i[:-4]))

if __name__ == '__main__':
	main()