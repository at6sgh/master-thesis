# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 16:25:20 2018

@author: gagat
"""

import pandas  as pd
import seaborn as sns
import matplotlib.pyplot as plt

url = 'C:/Users/gagat/Documents/magisterka/daneUSA_final.csv'
homes_rooms_shuffle = pd.read_csv(url, sep=',', na_values ='')
order = ["low-cost","medium-priced","high-priced","expensive"]

plt.style.use('ggplot')

#%%
fig, ax = plt.subplots(figsize=(12,8))
sns.countplot(x = 'city', data = homes_rooms_shuffle, order = homes_rooms_shuffle['city'].value_counts().index)
plt.title('Wykres obserwacji w podziale na miasta')
plt.ylabel('Liczebnosć')
plt.xlabel('Miasto')
plt.xticks(rotation=45)
plt.savefig('C:/Users/gagat/Documents/magisterka/wykresy/CountPlotCity.png')
plt.show()



fig, ax = plt.subplots(figsize=(12,8))
homes_rooms_shuffle.boxplot(column='price', by='city', ax=ax, showfliers=False)
plt.ylabel('Price Level')
plt.xlabel('City')
plt.xticks(rotation=45)
plt.savefig('C:/Users/gagat/Documents/magisterka/wykresy/boxPlotPrice.png')
plt.show()



#%%
fig, ax = plt.subplots(figsize=(10,8))
plt.hist(homes_rooms_shuffle.price_quantile, color='steelblue')
plt.xlabel('Poziom cenowy za dobę oferty')
plt.ylabel('Liczebnosć')
plt.title('Podzial ze względu na cenę oferty za dobę')
plt.savefig('C:/Users/gagat/Documents/magisterka/wykresy/histPriceQuantile.png')
plt.show()

# naturalne zmienne kategoryczne
fig, ax = plt.subplots(figsize=(10,8))
sns.countplot(x='room_type', hue='price_quantile', data=homes_rooms_shuffle, hue_order = order, palette='Paired')
plt.xlabel('Rodzaj oferty')
plt.ylabel('Liczebnosć')
plt.title('Podzial na rodzaj oferty')
plt.savefig('C:/Users/gagat/Documents/magisterka/wykresy/histRoomtype.png')
plt.show()

fig, ax = plt.subplots(figsize=(10,8))
sns.countplot(x='instant_bookable', hue='price_quantile', data=homes_rooms_shuffle, hue_order = order, palette='Paired')
plt.xlabel('Natychmiastowa rezerwacja')
plt.ylabel('Liczebnosć')
plt.title('Podzial Natychmiastowa rezerwacja True/False')
plt.savefig('C:/Users/gagat/Documents/magisterka/wykresy/histInstantBookable.png')
plt.show()

fig, ax = plt.subplots(figsize=(10,8))
sns.countplot(x='host_is_superhost', hue='price_quantile', data=homes_rooms_shuffle, hue_order = order, palette='Paired')
plt.xlabel('Host is superhost')
plt.ylabel('Liczebnosć')
plt.title('Podzial na superhost True/False')
plt.savefig('C:/Users/gagat/Documents/magisterka/wykresy/histSuperhost.png')
plt.show()

fig, ax = plt.subplots(figsize=(10,8))
sns.countplot(x='cancellation_policy', hue='price_quantile', data=homes_rooms_shuffle, hue_order = order, palette='Paired')
plt.xlabel('Polityka rezygnacji')
plt.ylabel('Liczebnosć')
plt.title('Podzial na rodzaj polityki rezygnacji')
plt.savefig('C:/Users/gagat/Documents/magisterka/wykresy/histCancellation.png')
plt.show()

fig, ax = plt.subplots(figsize=(10,8))
sns.countplot(x='accommodation_type', hue='price_quantile', data=homes_rooms_shuffle, hue_order = order, palette='Paired')
plt.xlabel('Rodzaj budynku')
plt.ylabel('Liczebnosć')
plt.title('Podzial na rodzaj budynku')
plt.savefig('C:/Users/gagat/Documents/magisterka/wykresy/histPropertyType.png')
plt.show()


fig, ax = plt.subplots(figsize=(10,8))
sns.countplot(x='free_parking', hue='price_quantile', data=homes_rooms_shuffle, hue_order = order, palette='Paired')
plt.xlabel('Bezpłatny Parking')
plt.ylabel('Liczebnosć')
plt.title('Czy jest bezpłatny parking? Yes/ No')
plt.savefig('C:/Users/gagat/Documents/magisterka/wykresy/histParking.png')
plt.show()

fig, ax = plt.subplots(figsize=(10,8))
sns.countplot(x='elevator', hue='price_quantile', data=homes_rooms_shuffle, hue_order = order, palette='Paired')
plt.xlabel('Winda')
plt.ylabel('Liczebnosć')
plt.title('Czy jest winda? Yes/ No')
plt.savefig('C:/Users/gagat/Documents/magisterka/wykresy/histElevator.png')
plt.show()

fig, ax = plt.subplots(figsize=(10,8))
sns.countplot(x='fitness', hue='price_quantile', data=homes_rooms_shuffle, hue_order = order, palette='Paired')
plt.xlabel('Hot tube, pool or gym')
plt.ylabel('Liczebnosć')
plt.title('Czy jest dostęp do jacuzzi, basenu lub siłowni? Yes/ No')
plt.savefig('C:/Users/gagat/Documents/magisterka/wykresy/histFitness.png')
plt.show()

#%%
#histogramy

plt.figure(1)
fig, ax = plt.subplots(figsize=(10,8))
plt.suptitle('')
homes_rooms_shuffle.plot(y='distance', kind='hist', bins =80, range=(0,40), ax=ax, color='steelblue')
#dfAA['Distance'].plot(kind='hist', bins =30, range=(0,3000))
plt.xlabel('Distance')
plt.ylabel('Density')
plt.title('Histogram of Distance Distribution')
plt.savefig('C:/Users/gagat/Documents/magisterka/wykresy/histDistance.png')
plt.show()



plt.figure(2)
fig, ax = plt.subplots(figsize=(10,8))
plt.suptitle('')
homes_rooms_shuffle.plot(y='accommodates', kind='hist', bins =16, range=(0,16), ax=ax, color='steelblue')
plt.xlabel('Accommodates')
plt.ylabel('Density')
plt.title('Histogram of Accommodates Distribution')
plt.savefig('C:/Users/gagat/Documents/magisterka/wykresy/histAccommodates.png')
plt.show()


plt.figure(3)
fig, ax = plt.subplots(figsize=(10,8))
plt.suptitle('')
homes_rooms_shuffle.plot(y='bathrooms', kind='hist', bins =16, range=(0,8), ax=ax, color='steelblue')
plt.xlabel('Bathrooms')
plt.ylabel('Density')
plt.title('Histogram of Bathrooms Distribution')
plt.savefig('C:/Users/gagat/Documents/magisterka/wykresy/histBathroms.png')
plt.show()

plt.figure(4)
fig, ax = plt.subplots(figsize=(10,8))
plt.suptitle('')
homes_rooms_shuffle.plot(y='reviews_per_month', kind='hist', bins =32, range=(0,10), ax=ax, color='steelblue')
plt.xlabel('Reviews per month')
plt.ylabel('Density')
plt.title('Histogram of Number of Reviews per month Distribution')
plt.savefig('C:/Users/gagat/Documents/magisterka/wykresy/histReviews_per_month.png')
plt.show()



plt.figure(5)
fig, ax = plt.subplots(figsize=(10,8))
plt.suptitle('')
homes_rooms_shuffle.plot(y='review_scores_rating', kind='hist', bins =30, range=(70,100), ax=ax, color='steelblue')
plt.xlabel('Review score raiting')
plt.ylabel('Density')
plt.title('Histogram of Review score raiting Distribution')
plt.savefig('C:/Users/gagat/Documents/magisterka/wykresy/histReview_score_raiting.png')
plt.show()


plt.figure(6)
fig, ax = plt.subplots(figsize=(10,8))
plt.suptitle('')
homes_rooms_shuffle.plot(y='price', kind='hist', bins =100, range=(20,2000), ax=ax, color='steelblue')
plt.xlabel('Price')
plt.ylabel('Density')
plt.title('Histogram of Price Distribution')
plt.savefig('C:/Users/gagat/Documents/magisterka/wykresy/histPrice.png')
plt.show()


plt.figure(15)
fig, ax = plt.subplots(figsize=(10,8))
plt.suptitle('')
homes_rooms_shuffle.plot(y='bedrooms', kind='hist', bins =11, range=(0,10), ax=ax, color='steelblue')
plt.xlabel('Beds')
plt.ylabel('Density')
plt.title('Histogram of Beds Distribution')
plt.savefig('C:/Users/gagat/Documents/magisterka/wykresy/histBedrooms.png')
plt.show()

#%%
columns=['room_type','price', 'price_quantile', 'reviews_per_month', 'distance', 'accommodates', 'bathrooms', 'bedrooms', 'host_is_superhost', 'cancellation_policy', 
         'instant_bookable', 'review_scores_rating', 'accommodation_type', 'free_parking', 'elevator', 'fitness']
df=homes_rooms_shuffle.copy()
df=df[columns]

nrows = df.shape[0]

df.describe()
df.room_type.value_counts()/nrows
df.accommodation_type.value_counts()/nrows
df.cancellation_policy.value_counts()/nrows
df.host_is_superhost.value_counts()/nrows
df.free_parking.value_counts()/nrows
df.elevator.value_counts()/nrows
df.fitness.value_counts()/nrows
df.instant_bookable.value_counts()/nrows
df.price_quantile.value_counts()/nrows

sns.heatmap(df.corr(), square=True, cmap='YlGn')
plt.title('Heatmap of Correlation')

plt.savefig('C:/Users/gagat/Documents/magisterka/wykresy/histHeatmap.png')