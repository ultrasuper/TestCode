import re 
import requests
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') #改变标准输出的默认编码

def getHtml(url):
    html = requests.get(url)
    html.encoding = 'utf-8'
    return html.text

testurl = "https://www.sciencedirect.com/journal/journal-of-housing-economics"
print(getHtml(testurl))


def getImg(html):
    reg = r'src="(.*\.jpg)"'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    return imglist
html = getHtml(testurl)
print(getImg(html))



