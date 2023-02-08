import json
import requests
from bs4 import BeautifulSoup

url = "https://mib.mathinst.uz/2022.html"
html = requests.get(url)



data = dict()
list_data = list()

soup = BeautifulSoup(html.content, 'html.parser')
all_spans = soup.find_all("span", attrs={"class":"fs10lh1-5"})


i = 0
for one_spans in all_spans[1:16]:

    a_tag = one_spans.a
    b_tag = one_spans.b

    author = one_spans.b.text

    link = one_spans.a["href"]
    a_title = one_spans.a.text  # pdf
    #
    a_tag.decompose()
    pages = one_spans.text.split(" ")[-2]

    b_tag.decompose()
    body = one_spans.text.split(" Bull")[0]

    mydata = {
        "id": i,
        "author":author,
        "body": body,
        "link": link,
        "pages": pages,
        "a_title": a_title
    }
    list_data.append(mydata)
    i += 1



data = list_data

json_data = json.dumps(data, indent=4)
print(json_data)
