from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
soup = BeautifulSoup(html_doc, 'html.parser')
# Running the “three sisters” document through Beautiful Soup gives us a BeautifulSoup object, which represents the document as a nested data structure
# print(soup.prettify())


# One common task is extracting all the URLs found within a page’s <a> tags
for link in soup.find_all('a'):
    print(link.get('href'))

# Another common task is extracting all the text from a page
print(soup.get_text())
