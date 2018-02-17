import requests
from bs4 import BeautifulSoup

def getRaceCondition(soup):
    racecondition = []
    race_name = soup.find_all('h1')[1].getText()
    racecondition.append(race_name)
    race_data = soup.find_all('span')[7].getText().split()
    race_data = [race_data[0], race_data[4], race_data[8]]
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
    result_table = soup.find_all('tr')
    result_table = result_table[-35:-19]
    ans = []
    for row in result_table:
        ans.append(scrapeRow(row, result))
    return ans

def main():
    target_url = 'http://db.netkeiba.com/race/201706050811/'
    r = requests.get(target_url)
    r.encoding = r.apparent_encoding
    soup = BeautifulSoup(r.text, 'lxml')
    result = []
    race_name = soup.find_all('h1')[1].getText()
    result.append(race_name)
    race_data = soup.find_all('span')[7].getText().split()
    race_data = [race_data[0], race_data[4], race_data[8]]
    result += race_data
    race_date = soup.find_all("p")[4].getText().split()
    result += race_date
    ans = []
    for row in result_table:
        row = row.find_all("td")
        temp = []
        temp += result
        for data in row:
            temp.append(data.getText().replace('\n', ''))
        ans.append(temp)
        temp =[]


if __name__ == '__main__':
    main()
