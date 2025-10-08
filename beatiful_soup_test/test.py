import bs4 as bs
import requests as req
"""
response = req.get("http://example.com/")
print(response)
doc = bs.BeautifulSoup(response.text , "html.parser")
print(doc.title)"""

base_url = "https://example.com/"
response = req.get(base_url)
if response.status_code == 200:
    print("request was successful")
    doc = bs.BeautifulSoup(response.text , "html.parser")
    print(doc.find("h1").text)
else:
    print("request failed")


