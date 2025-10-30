#task 1-1

import urllib.request as request
import json

chinese_url = "https://resources-wehelp-taiwan-b986132eca78c0b5eeb736fc03240c2ff8b7116.gitlab.io/hotels-ch"
english_url = "https://resources-wehelp-taiwan-b986132eca78c0b5eeb736fc03240c2ff8b7116.gitlab.io/hotels-en"

with request.urlopen(chinese_url) as response:
    chinese_data = json.load(response)
with request.urlopen(english_url) as response:
    english_data = json.load(response)
chinese_list = chinese_data["list"]
english_list = english_data["list"]

english_dict={} #做一個english的字典

#把english_list中的資料存到 english_item 中
for english_item in english_list:
    english_dict[english_item["_id"]] = english_item
    
with open("hotels.csv", "w", encoding="utf-8") as file:
    for chinese_item in chinese_list:
        chinese_id = chinese_item["_id"]
        english_match = english_dict.get(chinese_id)
        if english_match:
                file.write(
                    chinese_item["旅宿名稱"] + ","+
                    english_match["hotel name"]+","+ 
                    chinese_item["地址"]+","+ 
                    english_match["address"]+","+ 
                    english_match["tel"]+","+ 
                    chinese_item["房間數"] + "\n"
                )

#task 1-2

import urllib.request as request
import json

chinese_url = "https://resources-wehelp-taiwan-b986132eca78c0b5eeb736fc03240c2ff8b7116.gitlab.io/hotels-ch"

with request.urlopen(chinese_url) as response:
    chinese_data = json.load(response)

district_data = {}

chinese_list = chinese_data["list"]
count = 0

for item in chinese_list:
    address = item["地址"]
    district = address.split("市")[1].split("區")[0] + "區"
    rooms = int(item["房間數"])
    if district not in district_data:
        district_data[district] = {"飯店數":0,"房間數":0}

    district_data[district]["飯店數"] += 1
    district_data[district]["房間數"] += rooms

with open("districts.csv", "w", encoding="utf-8") as file:
    for district, stats in district_data.items():
        file.write(f"{district},{stats['飯店數']},{stats['房間數']}\n")

# task 2

import urllib.request as req
import bs4 #beautiful4
import re

def get_root(url):
    # 建立一個 Request 物件 ， 附加 Request Headers 的資訊
    request = req.Request(url,headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36"
    }) # 為了要模仿真實的使用者，所以要加上這一行 User-Agent 在 google Chrome 中
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")
    #print(data)
    # 在成功抓到資料後，就要開始解析資料！
    root = bs4.BeautifulSoup(data,"html.parser") 
    return root

def get_titles(root):
    title_list = []
    titles = root.find_all("div",class_= "title") #用來尋找 class="title" 的 div 標籤 ， find 會找到其中一個 符合條件的標籤
    for title in titles:
        if title.a != None: #如果標題包含 a 標籤 (沒有被刪除) 就印出來
            title_list.append(title.a.string.strip())
        else:
            title_list.append("(已刪除)")
    return title_list

def get_likecount(root):
    likecount_list = []
    likecount = root.find_all("div", class_="nrec")
    for nrec in likecount:
        if nrec.span != None:
            likecount_list.append(nrec.span.string)
        else:
            likecount_list.append("0")
    return likecount_list

def get_time(root):

    links = ["https://www.ptt.cc" + a["href"] for a in root.select("div.title a")]
    times = []
    for link in links:
        post_request = req.Request(link,headers={
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36"
        })
        with req.urlopen(post_request) as response:
            post_html = response.read().decode("utf-8")
        post_root = bs4.BeautifulSoup(post_html,"html.parser")

        post_time = "(no time found)"

        metalines = post_root.select(".article-metaline")
        for m in metalines:
            tag = m.select_one(".article-meta-tag")
            value = m.select_one(".article-meta-value")
            if tag and tag.text == "時間":
                post_time = value.text
                break

        if post_time == "(no time found)":
            spans = post_root.select("div#main-content span")
            for i in range(len(spans) - 1):
                label = spans[i].get_text(strip=True)
                if label == "時間":
                    candidate = spans[i+1].get_text(strip=True)
                    post_time = candidate
                    break

        
        times.append(post_time)
    return times

def get_nextlink(root):
    next_link = root.find("a", string="‹ 上頁") #找到內文是 ‹ 上頁 的 a 標籤
    return "https://www.ptt.cc" + next_link["href"]

page_URL= "https://www.ptt.cc/bbs/Steam/index.html" #這是原始頁
count = 0
all_titles = []
all_likes = []
all_times = []

while count<3:
    root = get_root(page_URL)
    titles = get_titles(root)
    likes = get_likecount(root)
    article_times = get_time(root)
    all_titles.extend(titles)
    all_likes.extend(likes)
    all_times.extend(article_times)
    next_link = get_nextlink(root)
    page_URL = next_link
    count +=1
with open ("articles.csv" , "w" , encoding="utf-8") as file:
    for title,like,time in zip(all_titles, all_likes, all_times):
        task2 = f"{title},{like},{time}\n"
        file.write(task2)
