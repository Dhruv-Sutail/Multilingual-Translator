import bs4, requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
webpage = 'https://1000mostcommonwords.com/1000-most-common-marathi-words/'
fetch_url = urlopen(webpage)
html = fetch_url.read()
soup = BeautifulSoup(html, features = 'html.parser')
results = soup.find('table')
trs = results.find_all('td')

l = list()
for i in range(3, 3003):
    if i % 3 != 0:
        l.append(trs[i].text.strip())

marathiWords = list()
englishWords = list()
for i in range(0, 2000):
    if i % 2 == 0:
        marathiWords.append(l[i])
    else:
        englishWords.append(l[i])

eng_to_mara = {}
for i in range(0, 1000):
    eng_to_mara[englishWords[i]] = marathiWords[i]
