import itertools

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

if __name__ == '__main__':
    main()
