from __future__ import division, unicode_literals
import codecs
from bs4 import BeautifulSoup
#from ehp import *
import Html
f=codecs.open("C:\\Users\\Samer\\Desktop\\Coin Market Cap\\1.html", 'r','utf-8')
html=f.read()
html=Html()
parsed_html = BeautifulSoup(html)
print(parsed_html.body.div.find('p', attrs={'class': 'sc-16r8icm-0 sc-1teo54s-1 dNOTPP'}).text)