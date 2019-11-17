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

sns.relplot(data=data, x="경도", y="위도", hue="동", palette=sns.color_palette("colorblind", 19))


plt.title('위도, 경도별 카페 분포',fontsize=20)
# plt.show()


map_alt=[];
map_long=[];

for i in range(len(data)):
    map_alt.append(data['위도'].iloc[i])
    map_long.append(data['경도'].iloc[i])


map_one=folium.Map(location=[data['위도'].iloc[0],data['경도'].iloc[0]],zoom_start=13)

for i in range(len(data)):
    # map_one=folium.Map(location=[map_one_alt[i],map_one_long[i]],zoom_start=13)
    if(data['동'].iloc[i]==1):
        folium.CircleMarker([map_alt[i],map_long[i]],radius=7,popup=i, color='#FF0000', fill_color='#FF0000').add_to(map_one)
    if(data['동'].iloc[i]==2):
        folium.CircleMarker([map_alt[i],map_long[i]],radius=7,popup=i, color='#F29661', fill_color='#F29661').add_to(map_one)
    if(data['동'].iloc[i]==3):
        folium.CircleMarker([map_alt[i],map_long[i]],radius=7,popup=i, color='#980000', fill_color='#980000').add_to(map_one)
    if(data['동'].iloc[i]==4):
        folium.CircleMarker([map_alt[i],map_long[i]],radius=7,popup=i, color='#FFBB00', fill_color='#FFBB00').add_to(map_one)
    if(data['동'].iloc[i]==5):
        folium.CircleMarker([map_alt[i],map_long[i]],radius=7,popup=i, color='#E5D85C', fill_color='#E5D85C').add_to(map_one)
    if(data['동'].iloc[i]==6):
        folium.CircleMarker([map_alt[i],map_long[i]],radius=7,popup=i, color='#997000', fill_color='#997000').add_to(map_one)
    if(data['동'].iloc[i]==7):
        folium.CircleMarker([map_alt[i],map_long[i]],radius=7,popup=i, color='#1F3456', fill_color='#1F3456').add_to(map_one)
    if(data['동'].iloc[i]==8):
        folium.CircleMarker([map_alt[i],map_long[i]],radius=7,popup=i, color='#ABF200', fill_color='#ABF200').add_to(map_one)
    if(data['동'].iloc[i]==9):
        folium.CircleMarker([map_alt[i],map_long[i]],radius=7,popup=i, color='#86E57F', fill_color='#86E57F').add_to(map_one)
    if(data['동'].iloc[i]==10):
        folium.CircleMarker([map_alt[i],map_long[i]],radius=7,popup=i, color='#6B9900', fill_color='#6B9900').add_to(map_one)
    if(data['동'].iloc[i]==11):
        folium.CircleMarker([map_alt[i],map_long[i]],radius=7,popup=i, color='#00D8FF', fill_color='#00D8FF').add_to(map_one)
    if(data['동'].iloc[i]==12):
        folium.CircleMarker([map_alt[i],map_long[i]],radius=7,popup=i, color='#6799FF', fill_color='#6799FF').add_to(map_one)
    if(data['동'].iloc[i]==13):
        folium.CircleMarker([map_alt[i],map_long[i]],radius=7,popup=i, color='#008299', fill_color='#008299').add_to(map_one)
    if(data['동'].iloc[i]==14):
        folium.CircleMarker([map_alt[i],map_long[i]],radius=7,popup=i, color='#0100FF', fill_color='#0100FF').add_to(map_one)
    if(data['동'].iloc[i]==15):
        folium.CircleMarker([map_alt[i],map_long[i]],radius=7,popup=i, color='#A566FF', fill_color='#A566FF').add_to(map_one)
    if(data['동'].iloc[i]==16):
        folium.CircleMarker([map_alt[i],map_long[i]],radius=7,popup=i, color='#D26C9F', fill_color='#D26C9F').add_to(map_one)
    if(data['동'].iloc[i]==17):
        folium.CircleMarker([map_alt[i],map_long[i]],radius=7,popup=i, color='#FF00DD', fill_color='#FF00DD').add_to(map_one)
    if(data['동'].iloc[i]==18):
        folium.CircleMarker([map_alt[i],map_long[i]],radius=7,popup=i, color='#F361A6', fill_color='#F361A6').add_to(map_one)
    if(data['동'].iloc[i]==19):
        folium.CircleMarker([map_alt[i],map_long[i]],radius=7,popup=i, color='#990085', fill_color='#990085').add_to(map_one)





map_one.save('dong_one.html',encoding='utf-8')

# print(map_one_alt[15])
