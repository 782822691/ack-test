import requests
from bs4 import BeautifulSoup as Be
import lxml
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'}
url = 'https://www.shicimingju.com/book/sanguoyanyi.html'
r = requests.get(url=url,headers=headers)
r.encoding='utf-8'
soup = Be(r.text,'lxml')
lst_soup = soup.select('.book-mulu > ul > li')
# print(lst_soup)

for li in lst_soup[:4]:
    print(li.a['href'])

# with open('./1.txt','w',encoding='utf-8') as fp:
#     for li in lst_soup[:3]:
#         fp.write(li.text + '\n')
#         detail_url = 'https://www.shicimingju.com/'+li.a['href']
#         r = requests.get(url=detail_url,headers=headers)
#         r.encoding = 'utf-8'
#         detali_soup = Be(r.text,'lxml')
#         # print(len(detali_soup.select('.bookmark-list  div')))
#         # print(detali_soup.select('.bookmark-list > div')[0].text)
#         fp.write(detali_soup.select('.bookmark-list > h1')[0].string+'\n')
#         fp.write(detali_soup.select('.chapter_content')[0].text+'\n')
#         print('{} is over'.format(li.text))


