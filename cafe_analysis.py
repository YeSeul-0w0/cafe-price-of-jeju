import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.font_manager as fm
import folium # 지도 사용시 필요한 모듈듈
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



sns.relplot(data=data, x="경도",y="위도",hue="동")

'''
plt.scatter(data.경도,data.위도,alpha=0.2,s=30, c=data.위도, cmap='viridis') 
(x값, y값, alpha는 뭔지 모르겠고 s는 동그라미 사이즈 c는 색상 cmap은 뭔지 모름)
plt.colorbar() #옆에 색 bar 뜨는거
'''

plt.title('위도, 경도별 카페 분포',fontsize=20) #타이틀
plt.show() #show함수로 받은 위도 경도 갑

#지금 한 건 그 동 별로 묶어서 색깔 다르게 만든거 주석처리한건 그 위도인가 경도인가 그거 기준으로 색 다르게 출력되는거.