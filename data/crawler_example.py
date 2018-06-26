import urllib
import re
from bs4 import BeautifulSoup

URL = 'https://laws.mol.gov.tw/FLAW/FLAWDAT0201.aspx?lsid=FL014930'
TARGET_FILE = 'labor_law.json'


def crawler(target):
    page = urllib.request.urlopen(target)
    soup = BeautifulSoup(page, 'html.parser')

    titles = map(str, soup.find_all('div', attrs={'class': 'col-no'}))
    contents = map(str, soup.find_all('pre'))

    pattern = '<[/\.\-\=\"\&\;\? a-zA-Z0-9]+>'
    data = map(lambda x, y: {'title': re.sub(
        pattern, '', x), 'content': re.sub(pattern, '', y)}, titles, contents)

    with open(TARGET_FILE, 'w', encoding='utf-8') as dst:
        for d in data:
            dst.write(str(d) + '\n')
