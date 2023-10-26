import urllib.request
def download_html(url):
    #url="https://movie.douban.com/top250?start=25"
    header={
        "user-Agent" :"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"

    }
    req=urllib.request.Request(url=url,headers=header)

    response=urllib.request.urlopen(req)
    html=response.read().decode("utf-8")
    return html
url=url="https://movie.douban.com/top250?start=25"
html=download_html(url)
import re
pattern="https://movie.douban.com/subject/[0-9]+/"
urls=re.findall(pattern,html)
urls=set(urls)
print("urls count=%d"%(len(urls)))
for url in urls:
    print(url)