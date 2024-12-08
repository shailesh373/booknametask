import requests as rq

from bs4 import BeautifulSoup
import pandas as pd

Burl = 'https://books.toscrape.com/'

BHeader = {
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
    
    }
BResq = rq.get(url=Burl , headers=BHeader)

BSoup = BeautifulSoup (BResq.content,'html.parser')

Bookname = BSoup.findAll('h3')


BooknameList = [Bname.text for Bname in Bookname]

Bname = pd.DataFrame(BooknameList)
Bname.to_csv('bookname.csv')
    