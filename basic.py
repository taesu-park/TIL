import requests
import pprint
import csv
key = '----'
targetDt = '20190713' #yyyymmdd
weekGb = '0'

api_url = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key={key}&targetDt={targetDt}&multiMovieYn={multiMovieYn}&repNationCd={repNationCd}&wideAreaCd={wideAreaCd}'
pprint.pprint(api_url)
response = requests.get(api_url).json()
pprint.pprint(response)

with open('boxoffice.csv','w',encoding='utf-8') as f:
    fieldnames = ['movieCd','movieNm','audiAcc']
    csv_writer = csv.DictWriter(f,fieldnames=fieldnames)
    csv_writer.writeheader()
    for item in api_url['boxOfficeResult']['weeklyBoxOfficeList'](fieldname for fieldname in fieldnames if fieldname['']).values():
        csv_writer.writerow(item)