# -*- coding: utf-8 -*-
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET


class SpellingChecker:
    def __init__(self):
        self.cx = '012080660999116631289:zlpj9ypbnii'

    def Counter(self, text):
        return len(text.split(' '))

    def Checker(self, query):
        url = ('http://www.google.com/search?'
               'q=%s'
               '&hl=zh'
               '&output=xml'
               '&client=google-csbe'
               '&cx=%s') % (urllib.parse.quote(query), self.cx)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36'}
        TargetPage = urllib.request.urlopen(urllib.request.Request(url=url, headers=headers))

        xmlp = ET.XMLParser(encoding="utf-8")
        content = TargetPage.read()
        tree = ET.ElementTree(ET.fromstring(content, parser=xmlp))
        root = tree.getroot()
        checker = root.findall("./Spelling/Suggestion")
        if len(checker) == 0:
            return True
        else:
            result = checker[0].get('q')
            return result


if __name__ == '__main__':
    test = SpellingChecker()
    TimeCount = 0
    # keyword = input('請輸入句子 = ')
    keyword = 'Having read mixed reviedws on trip advisor we wecre a littttle codancerned about what wfe woulgd find. Once we had arrived into the grand reception area our concerns started to disappear. The reception staff were very efficient and the bell boys were very friendly and eager to help. The bedrooms were very large and comfortable if a little tired in terms of decor BUT if you are going to New York to experience the sights and wonderful landmarks@[CMA] then how much time are you going to spend in your room? We used our rooms to sleep in and shower@[CMA] the rest of the time we were up and out and when we were in the hotel we would spend time in the plush reception and bar area people watching. The only reason I have not given it a 5 is due to the bedroom decor but I would have no hesitation in staying at the Roosevelt again if I am lucky enough to go back to New York in the future.'.replace(
        '@[CMA]', ',')
    while (True):
        TimeCount += 1
        print('times=', TimeCount)
        temp = test.Checker(keyword)
        if (type(temp) == bool):
            break
        else:
            keyword = temp
    print(keyword)
