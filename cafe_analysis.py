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

#sns.relplot(data=data, x="경도", y="위도", hue="동", palette=sns.color_palette("colorblind", 19))


plt.title('위도, 경도별 카페 분포',fontsize=20)
# plt.show()


map_alt=[];
map_long=[];

for i in range(len(data)):
    map_alt.append(data['위도'].iloc[i])
    map_long.append(data['경도'].iloc[i])


map_three=folium.Map(location=[data['위도'].iloc[0], data['경도'].iloc[0]], zoom_start=13)
'''

string_price=[];

for a in range(len(data)):
    temp=str(data['가격'].iloc[i])
    string_price.append((temp))


for i in range(len(data)):
    # map_one=folium.Map(location=[map_one_alt[i],map_one_long[i]],zoom_start=13)
    if(data['가격'].iloc[i]==1):
        folium.CircleMarker([map_alt[i],map_long[i]],radius=7,popup=data['아메리카노'].iloc[i], color='#FFA46C', fill_color='#FFA46C').add_to(map_three)
    if(data['가격'].iloc[i]==2):
        folium.CircleMarker([map_alt[i],map_long[i]],radius=7,popup=data['아메리카노'].iloc[i], color='#CF6E36', fill_color='#CF6E36').add_to(map_three)
    if(data['가격'].iloc[i]==3):
        folium.CircleMarker([map_alt[i],map_long[i]],radius=7, color='#993800', fill_color='#993800').add_child(folium.Popup(data['업소명'].iloc[i]+"\n"+string_price[i])).add_to(map_three)
    if(data['가격'].iloc[i]==4):
        folium.CircleMarker([map_alt[i],map_long[i]],radius=7,popup=data['아메리카노'].iloc[i], color='#630200', fill_color='#630200').add_to(map_three)
    if(data['가격'].iloc[i]==5):
        folium.CircleMarker([map_alt[i],map_long[i]],radius=7,popup=data['아메리카노'].iloc[i], color='#2D0000', fill_color='#2D0000').add_to(map_three)
    if(data['가격'].iloc[i]==6):
        folium.CircleMarker([map_alt[i],map_long[i]],radius=7,popup=data['아메리카노'].iloc[i], color='#1B0000', fill_color='#1B0000').add_to(map_three)
    if(data['가격'].iloc[i]==0):
        folium.CircleMarker([map_alt[i],map_long[i]],radius=7,popup=data['아메리카노'].iloc[i], color='#FFFFFF', fill_color='#FFFFFF').add_to(map_three)

map_three.save('page/dong_three.html', encoding='utf-8')



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
'''

data_heatmap = data[["아메리카노", "근처 카페 수", "면적", "카페밀도", "인구밀도", "동 카페 수"]].copy()
plt.title('위도, 경도별 카페 분포 - 전체',fontsize=20)
sns.heatmap(data_heatmap.corr(), annot=True,cmap="YlGnBu")
plt.show()
#data_heatmap = data[["아메리카노", "근처 카페 수", "면적", "동 면적", "인구" , "동 카페 수"]].copy()





# plt.show()

data_heatmap1 = data_heatmap[(data["체인점"]==0)].copy()
plt.title('위도, 경도별 카페 분포 - 체인점 제외',fontsize=20)
sns.heatmap(data_heatmap1.corr(), annot=True,cmap="YlGnBu")
plt.show()

data_heatmap2 = data_heatmap[(data['아메리카노']!=0) ].copy()
plt.title('위도, 경도별 카페 분포 - 가격정보無 제외',fontsize=20)
sns.heatmap(data_heatmap2.corr(), annot=True,cmap="YlGnBu")
plt.show()

data_heatmap3 = data_heatmap1[(data['아메리카노']!=0) ].copy()
plt.title('위도, 경도별 카페 분포 - 체인점, 가격정보無 제외',fontsize=20)
sns.heatmap(data_heatmap3.corr(), annot=True,cmap="YlGnBu")
plt.show()

'''
data_heatmap = data[(data["체인점"]==0) & (data['아메리카노']!=0)].copy()
data_heatmap = data_heatmap[["아메리카노", "근처 카페 수", "면적", "동 면적", "인구" , "동 카페 수", "동"]].copy()

sns.heatmap(data_heatmap.corr(), annot=True,cmap="YlGnBu")
# plt.show()
'''
