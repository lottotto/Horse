import requests
from bs4 import BeautifulSoup
import csv
import itertools

def getRaceCondition(soup):
    racecondition = []
    race_name = soup.find_all('h1')[1].getText()
    racecondition.append(race_name)
    race_data = soup.find_all('span')[7].getText()
    race_data = race_data.replace(' ', '')
    race_data = race_data.replace('\xa0', '')
    race_data = race_data.split('/')
    print(race_data)
    #race_data = [race_data[0], race_data[4], race_data[8]]
    racecondition += race_data
    race_date = soup.find_all("p")[4].getText().split()
    racecondition += race_date
    return racecondition

def scrapeRow(row,result):
    row = row.find_all("td")
    temp = []
    temp += result
    for data in row:
        temp.append(data.getText().replace('\n', ''))
    return temp

def getRaceResult(RACEPAGEURL):
    r = requests.get(RACEPAGEURL)
    r.encoding = r.apparent_encoding
    soup = BeautifulSoup(r.text, 'lxml')
    result = getRaceCondition(soup)
    result_table = soup.find_all('table')[0]
    result_table = result_table.find_all('tr')
    result_table = result_table[1:]
    ans = []
    for row in result_table:
        ans.append(scrapeRow(row, result))
    return ans

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

def getUrlList(year):
    """
    input :　year(int)
    output : dateLink(List)
    ------
    年を引数に，その年の日付のnetkeibaのURLのリストを返す．
    """
    dateLink = []
    for i, j in itertools.product(range(1,13), range(1,32)):
        url = 'http://db.netkeiba.com/race/list/' + year + str(i).zfill(2) + str(j).zfill(2) + '/'
        dateLink.append(url)
    return dateLink

def main():
    result = []
    DATELINK = getUrlList("2017")
    for datelink in DATELINK:
        DAIRYRACEURL = getDairyRaceURL(datelink)
        for dairyraceurl in DAIRYRACEURL:
            temp = getRaceResult(dairyraceurl)
            result += temp
            print("FINISH {0}".format(dairyraceurl))

    with open('./result20180217_2.csv','w') as f:
        writer = csv.writer(f)
        writer.writerows(result)


if __name__ == '__main__':
    main()
