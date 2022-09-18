import bs4 as bs
import urllib.request

sauce = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()
soup = bs.BeautifulSoup(sauce)

# print(soup.title.text)

# print(soup.p)

# print(soup.find_all('p'))


# for paragraph in soup.find_all('p'):
# print(paragraph.string)
#    print(paragraph.text)
# print(soup.get_text())

# for url in soup.find_all('a'):
#   print(url.get('href'))

nav = soup.nav
print(nav)
