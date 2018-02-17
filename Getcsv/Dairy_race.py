import requests
from bs4 import BeautifulSoup

def getDairyRaceURL(THEDAYURL):
    """
    ハズレだったら空リストを返します．
    """
    r = requests.get(THEDAYURL)
    r.encoding = r.apparent_encoding
    soup = BeautifulSoup(r.text, 'lxml')
    race_table = soup.findAll("dl", {"class":"race_top_data_info fc"})
    dst = []
    for table in race_table:
        url = "http://db.netkeiba.com"+ table.find("a").attrs['href']
        dst.append(url)
    return dst

def __main__():
    r = requests.get("http://db.netkeiba.com/race/list/20171224/")
    r.encoding = r.apparent_encoding
    soup = BeautifulSoup(r.text, 'lxml')
    race_table = soup.findAll("dl", {"class":"race_top_data_info fc"})
    dst = []
    for table in race_table:
        url = "http://db.netkeiba.com"+ table.find("a").attrs['href']
        dst.append(url)

if __name__ == '__main__':
    main()
