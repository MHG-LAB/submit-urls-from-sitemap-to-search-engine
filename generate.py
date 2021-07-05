import re
import json
import urllib
import requests

site = 'https://blog.mhuig.top'
sitemaps = ['/post-sitemap.xml','/page-sitemap.xml']

result = []
bingUrllist = []
bingData = {}
i=0

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}  

for sitemap in sitemaps:
    sitemap = site+sitemap
    req = urllib.request.Request(url=sitemap, headers=headers)
    html = urllib.request.urlopen(req).read().decode('utf-8')
    data = re.findall(re.compile(r'(?<=<loc>).*?(?=</loc>)'), html)
    result=result+data

with open('urls.txt', 'w') as file:
    for data in result:
        i=i+1
        print(data, file=file)
        # bing 提交前10条
        if i <= 10:
            bingUrllist.append(data)
        # baidu google 提交前100条
        if i == 100:
            break

bingData["siteUrl"] = site
bingData["urlList"] = bingUrllist
with open("bing.json", "w") as f:
    json.dump(bingData,f)

# with open('all-urls.txt', 'w') as file:
#     for data in result:
#         print(data, file=file)