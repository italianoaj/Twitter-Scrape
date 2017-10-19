
import urllib
import urllib.request
from bs4 import BeautifulSoup

handle = input("Whose tweets would you like to see? ")
url = "https://twitter.com/"+handle
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page, "html.parser")



print(soup.title.text)
"""
for foo in soup.findAll('a'):
    print(foo.get('href'))
"""
    
print(soup.find('div',{"class":"ProfileHeaderCard"}).find('p').text)

i=1
for tweets in soup.findAll('div',{"class":"content"}):
    print(i)
    print(tweets.find('p').text)
    i=i+1



