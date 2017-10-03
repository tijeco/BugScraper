from bs4 import BeautifulSoup as bs
import requests as rq
import random


while True:
    num = random.randint(2000000,3000000)

    bugguide = "http://bugguide.net/node/view/"+str(num)+"/bgimage" 
    # bugguide ="http://bugguide.net/node/view/1446859/bgimage"

    page = rq.get(bugguide)
    contents = page.content

    # print(contents)

    soup = bs(contents,'html.parser')

    # print(soup.find_all('img',"bgimage-image"))
    bug_pic = soup.find_all('img',"bgimage-image")
    data = {}
    # print(bug_pic)
    try:

        print(bug_pic[0].get("title"))
    except:
        print(bugguide," doesn't exist")
    # usedBefore[num] =True
    # title = a.string.strip()
    # print(a)
    # data[title]=a.attrs('href')
