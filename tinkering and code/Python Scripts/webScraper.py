import requests
from bs4 import BeautifulSoupA
from scrape


bookshelf = "https://www.gutenberg.org/wiki/Science_Fiction_(Bookshelf)"



bookUrls, titles, authors, soup = getBookURLsFromBookShelf(bookshelf)

books = pd.DataFrame({'url': bookUrls, 'title':titles, 'authors(s)':authors})

books = getCategories(soup, books)

display(books.shape)
books.head()
