# url=https://movie.douban.com/top250?start=25
# https://movie.douban.com/top250?start=50
## define function download_html
## parameter url
## return html web page
def download_html(url):
    import urllib.request
    #url="https://movie.douban.com/top250?start=25"
    header={
    'User-Agent':
    'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Mobile Safari/537.36'


    }

    req=urllib.request.Request(url=url,headers=header)
    #print(response)
    response=urllib.request.urlopen(req)
    html=response.read().decode("utf-8")
    #print(html)
    return html
# end of function


### defin get_url function
### parameter html
### return url by re pattern
def get_url(html):
    
    html=download_html(url)
    import re
    pattern="https://movie.douban.com/subject/[0-9]+/"
    urls=re.findall(pattern,html)
    return set(urls)
#print("urls count=%d"%(len(urls)))

#for url in urls:
 #   print(url)

### main program
import pprint
file=open('douban.txt','r')
output=open('doubanmove1212.txt','w')
lines=file.readlines()
#print(lines)
#pprint.pprint(lines)
for url in lines:
    url=url.strip()
    #pprint.pprint(url)
    html=download_html(url)
    urls=get_url(html)
    for url in urls:
        output.write(url+'\n')
    file.close()
    output.close()