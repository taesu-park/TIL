import csv
import pprint
import requests
from decouple import config

key = config('KEY')
movie_detail = {}

with open('boxoffice.csv','r',encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        movieCd = row['영화코드']
        api_url = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?key={key}&movieCd={movieCd}'
        response = requests.get(api_url).json
        
        movie_info = response['movieInfoResult']['movieInfo']
        movie_detail[movie_info['movieCd']] = {
        '영화코드': movie_info['movieCd'], 
        '영화명': movie_info['movieNm'], 
        '영화명(원문)': movie_info['movieNmEn'],
        '관람등급': movie_info['audits'][0]['watchGradeNm'] if movie_info['audits'] else None,
        '개봉연도': movie_info['openDt'],
        '장르': movie_info['genres'][0]['genreNm'],
        '감독명': movie_info['directors'][0]['peopleNm'] if  movie_info['directors'] else None
    }

with open('movie.csv','w',encoding='utf-8') as f:
    fieldnames = ['영화코드', '영화명', '영화명(원문)', '관람등급', '개봉연도', '장르', '감독명'] # 여기만 변경
    csv_writer = csv.DictWriter(f, fieldnames=fieldnames)
    csv_writer.writeheader()
    for item in movie_detail.values():
        csv_writer.writerow(item)
