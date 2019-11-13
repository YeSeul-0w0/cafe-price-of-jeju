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
data.plot.scatter(x='경도', y='위도') #위도 경도 값 받아서 표현
plt.show() #show함수로 받은 위도 경도 갑