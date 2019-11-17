import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.font_manager as fm
import folium # 지도 사용시 필요한 모듈듈
from folium import plugins

import warnings
warnings.filterwarnings('ignore')
warnings.filterwarnings('ignore', 'This pattern has match groups')
warnings.filterwarnings('ignore', 'The iterable function was deprecated in Matplotlib')

data=pd.read_csv('cafe_data.csv', encoding='cp949')

mpl.rcParams['axes.unicode_minus'] = False

plt.rcParams["font.family"] = 'Malgun Gothic'
plt.rcParams["font.size"] = 15
plt.rcParams["figure.figsize"] = (14,4)

data[['위도', '경도']].describe(include=np.number)
data['위도']=data['위도'].astype(float)
data['경도']=data['경도'].astype(float)

sns.relplot(data=data, x="경도", y="위도", hue="동", palette=sns.color_palette("colorblind", 19)) #sns.color_palette("팔레트 이름", 색 수)

plt.title('위도, 경도별 카페 분포',fontsize=20) #타이틀
# plt.show() #show함수로 받은 위도 경도 갑

dong_one=data.loc[data['동']==1]  #동 번호 1인 데이터만 저장

map_one_alt=[];
map_one_long=[];

for i in range(len(dong_one)):
    map_one_alt.append(dong_one['위도'].iloc[i])
    map_one_long.append(dong_one['경도'].iloc[i])

map_one=folium.Map(location=[dong_one['위도'].iloc[0],dong_one['경도'].iloc[0]],zoom_start=13)

for i in range(len(dong_one)):
    # map_one=folium.Map(location=[map_one_alt[i],map_one_long[i]],zoom_start=13)
    folium.Marker([map_one_alt[i],map_one_long[i]],popup=i,icon_color='red').add_to(map_one)

map_one.save('dong_one.html',encoding='utf-8')

print(map_one_alt[16])

'''
map_one=folium.Map(location=[dong_one['위도'].iloc[0],dong_one['경도'].iloc[0]],zoom_start=13)
folium.Marker([dong_one['위도'].iloc[0],dong_one['경도'].iloc[0]],popups='이도동').add_to(map_one)
map_one.save('dong_one.html',encoding='utf-8')
'''