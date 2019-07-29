import csv
import requests
import pprint
key = '2047d49e66779dd099ae7cc8e9d9bfd2'
movie_detail = {}
code_list=[]

with open('boxoffice.csv','r',encoding='utf-8') as f:
    
    csv_reader = csv.DictReader(f)
    for j in csv_reader:
        code_list.append(j['영화코드'])

        
for code in code_list:
    api_url = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?key={key}&movieCd={code}'
    response = requests.get(api_url).json()
    movie = response['movieInfoResult']['movieInfo']
    movie_detail[code] = {
        '영화 대표코드':movie['movieCd'],
        '영화명':movie['movieNm'],
        '영화명(국문)':movie['movieNm'],
        '영화명(영문)':movie['movieNmEn'],
        '영화명(원문)':movie['movieNmOg'],
        '관람등급':movie['audits'][0]['watchGradeNm'] if movie['audits'] else None,
        '개봉연도':movie['openDt'],
        '상영시간':movie['showTm'],
        '장르':movie['genres'][0]['genreNm'], 
        '감독명':movie['directors'][0]['peopleNm'] if movie['directors'] else None
        
        
    }
    
with open('movie.csv','w',encoding='utf-8') as f:
    fieldnames = ['영화 대표코드','영화명','영화명(국문)','영화명(영문)','영화명(원문)','관람등급','개봉연도','상영시간','장르','감독명'] # 여기만 변경
    csv_writer = csv.DictWriter(f, fieldnames=fieldnames)
    csv_writer.writeheader()
    for item in movie_detail.values():
        csv_writer.writerow(item)