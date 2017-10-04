from bs4 import BeautifulSoup as bs
import requests as rq
import random


for num in range(2000000):
    bugguide = "http://bugguide.net/node/view/"+str(num)+"/bgimage"
    page = rq.get(bugguide)
    contents = page.content
    soup = bs(contents,'html.parser')
    bug_pic = soup.find_all('img',"bgimage-image")
    # print(bug_pic)
    try:

        title=bug_pic[0].get("title")
        src=bug_pic[0].get("src")
        titleSplit = title.split(' - ')
        titleFields = len(titleSplit)

        if titleFields == 1:
            title2write = "wget -O bg_"+str(num) +'_'+title.replace(" ", "-")+".jpeg "+src
        # elif titleFields == 2:
        #     title2write = titleSplit[1]
        # elif "female" not in titleFields[:-1] and "male" not in titleFields[:-1]:
        #     title2write = titleFields[:-1]
        # else:
        #     print("FUCK: ",title)
        print(title2write)

        src=bug_pic[0].get("src")
        # print(len(title.split(' - ' )),title)
    except:
        None
    # print(num)
        # print(bugguide," doesn't exist")
    # usedBefore[num] =True
    # title = a.string.strip()
    # print(a)
    # data[title]=a.attrs('href')
