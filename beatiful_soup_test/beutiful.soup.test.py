from re import findall

from bs4 import BeautifulSoup

html_doc = """<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie&quot; class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie&quot; class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie&quot; class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc, 'html.parser')

print(soup.title)
print(soup.p)
print()
print(soup.find('p'))
print(

)

print(soup.find_all('p'))