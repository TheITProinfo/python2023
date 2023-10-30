# url=https://movie.douban.com/top250?start=25
# https://movie.douban.com/top250?start=50

import urllib.request
url="https://movie.douban.com/top250?start=25"
header={
'User-Agent':
'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Mobile Safari/537.36'


}

req=urllib.request.Request(url=url,headers=header)
#print(response)
response=urllib.request.urlopen(req)
html=response.read().decode("utf-8")
print(html)
import re
pattern="https://movie.douban.com/subject/[0-9]+/"
urls=re.findall(pattern,html)
urls=set(urls)
print("urls count=%d"%(len(urls)))

for url in urls:
    print(url)