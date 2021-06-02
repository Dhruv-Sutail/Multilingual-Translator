import bs4, requests
from bs4 import BeautifulSoup
from urllib.request import urlopen

#words:
webpage = 'https://1000mostcommonwords.com/1000-most-common-gujarati-words/'
fetch_url = urlopen(webpage)
html = fetch_url.read()
soup = BeautifulSoup(html, features = 'html.parser')
results = soup.find('table')
trs = results.find_all('td')

l = list()
for i in range(3, 3003):
    if i % 3 != 0:
        l.append(trs[i].text.strip())

gujaratiWords = list()
englishWords = list()
for i in range(0, 2000):
    if i % 2 == 0:
        gujaratiWords.append(l[i])
    else:
        englishWords.append(l[i])

eng_to_guj = {}
for i in range(0, 1000):
    eng_to_guj[englishWords[i]] = gujaratiWords[i]

#alphabets:
webpage2 = 'http://learn-gujarati-from-english.blogspot.com/2013/11/alphabets-in-gujarati-script.html'
fetch_url2 = urlopen(webpage2)
html2 = fetch_url2.read()
soup2 = BeautifulSoup(html2, features = 'html.parser')
results1 = soup2.find('table')
trs1 = results1.find_all('td')
results2 = soup2.find('table', {'style': 'border-collapse: collapse; border: none; mso-border-alt: solid windowtext .5pt; mso-border-insideh: .5pt solid windowtext; mso-border-insidev: .5pt solid windowtext; mso-padding-alt: 0in 5.4pt 0in 5.4pt; mso-yfti-tbllook: 480; width: 305px;'})

trs2 = results2.find_all('td')

trsList = []
for i in range(0, 111):
    trsList.append(trs1[i].text.strip())
trsList = trsList[3:]

trsList1 = []
for i in range(0, 39):
    trsList1.append(trs2[i].text.strip())
trsList1 = trsList1[3:]

totalList = trsList + trsList1

trsGuj = []
trsEng = []
for i in range(0, 144):
    if i % 3 == 0:
        trsGuj.append(totalList[i])
    elif i % 3 == 2:
        trsEng.append(totalList[i])

eng_to_guj2 = {}
for i in range(0, 48):
    eng_to_guj2[trsEng[i]] = trsGuj[i]

