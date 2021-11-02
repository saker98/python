#import codecs
#f=codecs.open("C:\\Users\\Samer\\Desktop\\Coin Market Cap\\1.html", 'r','utf-8')
#d=f.read()
#print (d)
try:
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup

html = '''<html>
<head>Heading</head>
<body attr1='val1'>
    <div class='container'>
        <div id='class'>Something here</div>
        <div>Something else</div>
    </div>
</body>
</html>'''

parsed_html = BeautifulSoup(html)
print(parsed_html.body.find('div', attrs={'class':'container'}).text)