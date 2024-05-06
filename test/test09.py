from lxml import etree
import requests
import os
url = 'https://sc.chinaz.com/jianli/free.html'
headers = {'User-Agent':
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'}
response = requests.get(url=url,headers=headers).text
tree = etree.HTML(response)
if not os.path.exists('./introduce'):
    os.mkdir('./introduce',777)
for morden in tree.xpath('//div[@id="container"]/div/a[@target="_blank"]')[:3]:
    path = morden.xpath('./@href')[0]
    intro_name = morden.xpath('./img/@alt')[0]+'.rar'
    intro_name = intro_name.encode('iso-8859-1').decode('utf-8')
    response = requests.get(url=path,headers=headers).text
    intro_tree = etree.HTML(response)
    load_path = intro_tree.xpath('//div[@class="down_wrap"]//ul[@class="clearfix"]/li/a/@href')[0]
    intro = requests.get(url=load_path,headers=headers).content
    intropath = 'introduce/'+intro_name
    with open(intropath,'wb') as f:
        f.write(intro)
    print(intro_name+'下载完成')
