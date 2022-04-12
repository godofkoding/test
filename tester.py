import pandas as pd

dfa = pd.read_csv('./data/MARINE_BUOY_22103_HR_2020_2020_2021.csv', encoding='cp949')
dfb = pd.read_csv('./data/MARINE_BUOY_22104_HR_2020_2020_2021.csv', encoding='cp949')
dfc = pd.read_csv('./data/MARINE_BUOY_22297_HR_2020_2020_2021.csv', encoding='cp949')
dfa = dfa[['일시', '유의파고(m)']]
dfb = dfb[['일시', '유의파고(m)']]
dfc = dfc[['일시', '유의파고(m)']]
dfa.rename(columns={'유의파고(m)':'거문도'}, inplace=True)
dfb.rename(columns={'유의파고(m)':'가거도'}, inplace=True)
dfc.rename(columns={'유의파고(m)':'거제도'}, inplace=True)

a = pd.merge(dfa,dfb,how='outer')
a= a.sort_values(by= '일시')
b = pd.merge(a,dfc,how='outer')
b = b.sort_values(by='일시')
print(b)