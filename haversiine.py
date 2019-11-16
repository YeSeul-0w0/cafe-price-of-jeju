#주변 카페 수 세기
from haversine import haversine
import pandas as pd

data=pd.read_csv('cafe_data.csv', encoding='cp949')

for i in data.index:
    count=-1 #본인도 같이 세므로 -1
    for j in data.index:
        point1 = ( data.loc[i,'위도'], data.loc[i, '경도']) #기준점
        point2 = ( data.loc[j,'위도'], data.loc[j, '경도']) #비교할위치
        if haversine(point1,point2) <= 0.25: #거리 구해서 비교 / 1=1km 0.5=500m
            count = count+1
    print(count)