# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 18:00:59 2018

@author: gagat
"""

import pandas as pd


url1= 'C:/Users/gagat/Documents/magisterka/Austin/daneAustin0.csv'
Austin= pd.read_csv(url1, sep=',', na_values='')

url2='C:/Users/gagat/Documents/magisterka/Boston/daneBoston1.csv'
Boston= pd.read_csv(url2, sep=',', na_values='')

url3='C:/Users/gagat/Documents/magisterka/Chicago/daneChicago2.csv'
Chicago= pd.read_csv(url3, sep=',', na_values='')

url4='C:/Users/gagat/Documents/magisterka/Columbus/daneColumbus3.csv'
Columbus= pd.read_csv(url4, sep=',', na_values='')

url5='C:/Users/gagat/Documents/magisterka/Denver/daneDenver4.csv'
Denver= pd.read_csv(url5, sep=',', na_values='')

url6='C:/Users/gagat/Documents/magisterka/Los Angeles/daneLos Angeles5.csv'
LosAngeles= pd.read_csv(url6, sep=',', na_values='')

url7='C:/Users/gagat/Documents/magisterka/Nashville/daneNashville6.csv'
Nashville= pd.read_csv(url7, sep=',', na_values='')

url9 = 'C:/Users/gagat/Documents/magisterka/New Orlean/daneNew Orlean7.csv'
NewOrlean= pd.read_csv(url9, sep=',', na_values='')

url8='C:/Users/gagat/Documents/magisterka/New York City/daneNew York City8.csv'
NewYork= pd.read_csv(url8, sep=',', na_values='')

url10='C:/Users/gagat/Documents/magisterka/Oakland/daneOakland9.csv'
Oakland= pd.read_csv(url10, sep=',', na_values='')

url11='C:/Users/gagat/Documents/magisterka/Portland/danePortland10.csv'
Portland= pd.read_csv(url11, sep=',', na_values='')

url12='C:/Users/gagat/Documents/magisterka/San Diego/daneSan Diego11.csv'
SanDiego= pd.read_csv(url12, sep=',', na_values='')

url13='C:/Users/gagat/Documents/magisterka/San Francisco/daneSan Francisco12.csv'
SanFrancisco= pd.read_csv(url13, sep=',', na_values='')

url14='C:/Users/gagat/Documents/magisterka/Santa Clara County/daneSanta Clara County13.csv'
SantaClara= pd.read_csv(url14, sep=',', na_values='')

url15='C:/Users/gagat/Documents/magisterka/Seattle/daneSeattle14.csv'
Seattle= pd.read_csv(url15, sep=',', na_values='')

url16='C:/Users/gagat/Documents/magisterka/Twin Cities MSA/daneTwin Cities MSA15.csv'
Minneapolis= pd.read_csv(url16, sep=',', na_values='')

url17='C:/Users/gagat/Documents/magisterka/Washington/daneWashington16.csv'
Washington= pd.read_csv(url17, sep=',', na_values='')

all_cities= pd.concat([Austin, Boston, Chicago, Columbus, Denver, LosAngeles, Minneapolis, Nashville,
                       NewOrlean, NewYork, Oakland, Portland, SanDiego, SanFrancisco, SantaClara, Seattle,
                 Washington], ignore_index=True)

#%%
all_cities.info()
all_cities.reviews_per_month=all_cities.reviews_per_month.fillna(0)
all_cities.review_scores_rating=all_cities.review_scores_rating.fillna(1)
all_cities.host_is_superhost=all_cities.host_is_superhost.fillna('f')
all_cities.bathrooms=all_cities.bathrooms.fillna(0)
all_cities.beds=all_cities.beds.fillna(0)
all_cities.bedrooms=all_cities.bedrooms.fillna(0)

all_cities.price_quantile.value_counts(dropna=False)
all_cities.city.value_counts(dropna=False)

all_cities["cancellation_policy"].value_counts(dropna= False)

all_cities.loc[all_cities.cancellation_policy == 'super_strict_30', 'cancellation_policy'] = 'strict_14+'
all_cities.cancellation_policy[all_cities['cancellation_policy']== 'super_strict_60' ] = 'strict_14+'
all_cities.cancellation_policy[all_cities['cancellation_policy']== 'strict_14_with_grace_period' ] = 'strict_14+'
all_cities.cancellation_policy[all_cities['cancellation_policy']== 'strict' ] = 'strict_14+'
all_cities["cancellation_policy"].value_counts(dropna= False)

all_cities.to_csv('C:/Users/gagat/Documents/magisterka/daneAllCities_withReviews.csv', sep=',', encoding='utf-8', index=False)


#%%
url = 'C:/Users/gagat/Documents/magisterka/daneAllCities_withReviews.csv'
df_detailed = pd.read_csv(url,  sep =',', na_values='')

df_detailed.property_type.value_counts(dropna = False)
df_detailed['accommodation_type'] = 'Hostel_like_Other'
df_detailed.loc[df_detailed.property_type == 'Loft', 'accommodation_type'] = 'Apartment'
df_detailed.loc[df_detailed.property_type == 'Apartment', 'accommodation_type'] = 'Apartment'
df_detailed.loc[df_detailed.property_type == 'Condominium', 'accommodation_type'] = 'Apartment'
#df_detailed.loc[df_detailed.property_type == 'Serviced apartment', 'accommodation_type'] = 'Apartment'

df_detailed.loc[df_detailed.property_type == 'House', 'accommodation_type'] = 'House'
df_detailed.loc[df_detailed.property_type == 'Townhouse', 'accommodation_type'] = 'House'
df_detailed.loc[df_detailed.property_type == 'Villa', 'accommodation_type'] = 'House'
#df_detailed.loc[df_detailed.property_type == 'Bungalow', 'accommodation_type'] = 'House'
#df_detailed.loc[df_detailed.property_type == 'Chalet', 'accommodation_type'] = 'House'
#df_detailed.loc[df_detailed.property_type == 'Cabin', 'accommodation_type'] = 'House'

df_detailed.accommodation_type.value_counts(dropna = False)
df_detailed.city.value_counts(dropna=False)


homes_rooms_shuffle = df_detailed.copy()
df_detailed = df_detailed.copy()
#%%
df_detailed = df_detailed.reset_index()
#type(df_detailed.amenities)
#amenities = df_detailed.amenities
amenities = amenities.astype(str)

nrows=df_detailed.shape[0]

wifi = []
for i in range(nrows):
    if 'Wifi' in df_detailed.amenities[i]:
        wifi.append('Yes')
    else: 
        wifi.append('No')

df_detailed['wifi'] = wifi
df_detailed.wifi.value_counts(dropna=False)
sns.countplot(x='wifi', hue='price_quantile', data=df_detailed, hue_order = order, palette='Paired')

smoking_allowed =[]
for i in range(nrows):
    if 'Smoking allowed' in df_detailed.amenities[i]:
        smoking_allowed.append('Yes')
    else: 
        smoking_allowed.append('No')

df_detailed['smoking_allowed'] = smoking_allowed
df_detailed.smoking_allowed.value_counts(dropna=False)
sns.countplot(x='smoking_allowed', hue='price_quantile', data=df_detailed, hue_order = order, palette='Paired')

free_parking = []
for i in range(nrows):
    if 'Free parking' in df_detailed.amenities[i]:
        free_parking.append('Yes')
    else: 
        free_parking.append('No')

df_detailed['free_parking'] = free_parking
df_detailed.free_parking.value_counts(dropna=False)
sns.countplot(x='free_parking', hue='price_quantile', data=df_detailed, hue_order = order, palette='Paired')

elevator = []
for i in range(nrows):
    if 'Elevator' in df_detailed.amenities[i]:
        elevator.append('Yes')
    else: 
        elevator.append('No')

df_detailed['elevator'] = elevator
df_detailed.elevator.value_counts(dropna=False)
sns.countplot(x='elevator', hue='price_quantile', data=df_detailed, hue_order = order, palette='Paired')


Hottub = []
for i in range(nrows):
    if 'Hot tub' in df_detailed.amenities[i]:
        Hottub.append('Yes')
    else: 
        Hottub.append('No')
df_detailed['hottub']=Hottub

Pool = []
for i in range(nrows):
    if 'Pool' in df_detailed.amenities[i]:
        Pool.append('Yes')
    else: 
        Pool.append('No')
df_detailed['pool'] = Pool

Gym = []
for i in range(nrows):
    if 'Gym' in df_detailed.amenities[i]:
        Gym.append('Yes')
    else: 
        Gym.append('No')
df_detailed['gym'] = Gym

df_detailed['fitness']='No'
df_detailed.loc[df_detailed.pool == 'Yes', 'fitness'] = 'Yes'
df_detailed.loc[df_detailed.hottub == 'Yes', 'fitness'] = 'Yes'
df_detailed.loc[df_detailed.gym == 'Yes', 'fitness'] = 'Yes'

df_detailed.fitness.value_counts(dropna=False)

sns.countplot(x='fitness', hue='price_quantile', data=df_detailed, hue_order = order, palette='Paired')


#%%
df_detailed.info()
 cols = ['id', 'room_type','price', 'price_quantile', 'number_of_reviews', 'reviews_per_month', 'distance', 'host_is_superhost', 
         'host_identity_verified', 'city', 'property_type', 'accommodates', 'bathrooms', 'bedrooms', 
         'review_scores_rating','instant_bookable', 'cancellation_policy', 
         'accommodation_type', 'free_parking', 'elevator', 'fitness']
df_detailed_final=df_detailed[cols]
df_detailed_shuffle = df_detailed_final.sample(frac=1).reset_index(drop=True)
df_detailed_shuffle.info()
df_detailed_shuffle.to_csv('C:/Users/gagat/Documents/magisterka/daneUSA_final.csv', sep=',', encoding='utf-8', index=False)


df_detailed.bedrooms.value_counts(dropna=False)
df_detailed.host_identity_verified.value_counts(dropna=False)
df_detailed.host_identity_verified = df_detailed.host_identity_verified.fillna('f')
sns.countplot(x='host_identity_verified', hue='price_quantile', data=df_detailed, hue_order = order, palette='Paired')

#%%

order = ["low-cost","medium-priced","high-priced","expensive"]
import seaborn as sns
import matplotlib.pyplot as plt
plt.style.use('ggplot')

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
plt.xlabel('Polityka rezygnacji')
plt.ylabel('Liczebnosć')
plt.title('Podzial na rodzaj polityki rezygnacji')
plt.savefig('C:/Users/gagat/Documents/magisterka/wykresy/histPropertyType.png')
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


plt.figure(1)
fig, ax = plt.subplots(figsize=(10,8))
plt.suptitle('')
homes_rooms_shuffle.plot(y='distance_log', kind='hist', bins =30, range=(0,5), ax=ax)
#dfAA['Distance'].plot(kind='hist', bins =30, range=(0,3000))
plt.xlabel('Logarithm of Distance')
plt.ylabel('Density')
plt.title('Histogram of Distance Distribution')
plt.savefig('C:/Users/gagat/Documents/magisterka/wykresy/histDistance_log.png')
plt.show()


plt.figure(2)
fig, ax = plt.subplots(figsize=(10,8))
plt.suptitle('')
homes_rooms_shuffle.plot(y='accommodates', kind='hist', bins =16, range=(0,16), ax=ax, color='steelblue')
#dfAA['Distance'].plot(kind='hist', bins =30, range=(0,3000))
plt.xlabel('Accommodates')
plt.ylabel('Density')
plt.title('Histogram of Accommodates Distribution')
plt.savefig('C:/Users/gagat/Documents/magisterka/wykresy/histAccommodates.png')
plt.show()

plt.figure(6)
fig, ax = plt.subplots(figsize=(10,8))
plt.suptitle('')
homes_rooms_shuffle.plot(y='accommodates_sqrt', kind='hist', bins =8, range=(0,3), ax=ax)
#dfAA['Distance'].plot(kind='hist', bins =30, range=(0,3000))
plt.xlabel('Logarithm of Accommodates')
plt.ylabel('Density')
plt.title('Histogram of Accommodates Distribution')
plt.savefig('C:/Users/gagat/Documents/magisterka/wykresy/histAccommodates_log.png')
plt.show()

plt.figure(3)
fig, ax = plt.subplots(figsize=(10,8))
plt.suptitle('')
homes_rooms_shuffle.plot(y='bathrooms', kind='hist', bins =16, range=(0,8), ax=ax, color='steelblue')
#dfAA['Distance'].plot(kind='hist', bins =30, range=(0,3000))
plt.xlabel('Bathrooms')
plt.ylabel('Density')
plt.title('Histogram of Bathrooms Distribution')
plt.savefig('C:/Users/gagat/Documents/magisterka/wykresy/histBathroms.png')
plt.show()

plt.figure(7)
fig, ax = plt.subplots(figsize=(10,8))
plt.suptitle('')
homes_rooms_shuffle.plot(y='bathrooms_log', kind='hist', bins =8, range=(0,3), ax=ax)
#dfAA['Distance'].plot(kind='hist', bins =30, range=(0,3000))
plt.xlabel('Logarithm of Bathrooms')
plt.ylabel('Density')
plt.title('Histogram of Bathrooms Distribution')
plt.savefig('C:/Users/gagat/Documents/magisterka/wykresy/histBathroms_log.png')
plt.show()

plt.figure(4)
fig, ax = plt.subplots(figsize=(10,8))
plt.suptitle('')
homes_rooms_shuffle.plot(y='reviews_per_month', kind='hist', bins =32, range=(0,10), ax=ax, color='steelblue')
#dfAA['Distance'].plot(kind='hist', bins =30, range=(0,3000))
plt.xlabel('Reviews per month')
plt.ylabel('Density')
plt.title('Histogram of Number of Reviews per month Distribution')
plt.savefig('C:/Users/gagat/Documents/magisterka/wykresy/histReviews_per_month.png')
plt.show()

plt.figure(8)
fig, ax = plt.subplots(figsize=(10,8))
plt.suptitle('')
homes_rooms_shuffle.plot(y='reviews_per_month_sqrt', kind='hist', bins =12, range=(0,4), ax=ax)
#dfAA['Distance'].plot(kind='hist', bins =30, range=(0,3000))
plt.xlabel('Logarithm of Reviews per month')
plt.ylabel('Density')
plt.title('Histogram of Number of Reviews per month Distribution')
plt.savefig('C:/Users/gagat/Documents/magisterka/wykresy/histReviews_per_month_log.png')
plt.show()


plt.figure(5)
fig, ax = plt.subplots(figsize=(10,8))
plt.suptitle('')
homes_rooms_shuffle.plot(y='review_scores_rating', kind='hist', bins =30, range=(70,100), ax=ax, color='steelblue')
#dfAA['Distance'].plot(kind='hist', bins =30, range=(0,3000))
plt.xlabel('Review score raiting')
plt.ylabel('Density')
plt.title('Histogram of Review score raiting Distribution')
plt.savefig('C:/Users/gagat/Documents/magisterka/wykresy/histReview_score_raiting.png')
plt.show()

plt.figure(5)
fig, ax = plt.subplots(figsize=(10,8))
plt.suptitle('')
homes_rooms_shuffle.plot(y='review_scores_rating_log', kind='hist', bins =36, range=(0,5), ax=ax)
#dfAA['Distance'].plot(kind='hist', bins =30, range=(0,3000))
plt.xlabel('Review score raiting')
plt.ylabel('Density')
plt.title('Histogram of Number of Reviews per month Distribution')
plt.savefig('C:/Users/gagat/Documents/magisterka/wykresy/histReview_score_raiting_log.png')
plt.show()

plt.figure(6)
fig, ax = plt.subplots(figsize=(10,8))
plt.suptitle('')
homes_rooms_shuffle.plot(y='price', kind='hist', bins =100, range=(20,2000), ax=ax, color='steelblue')
#dfAA['Distance'].plot(kind='hist', bins =30, range=(0,3000))
plt.xlabel('Price')
plt.ylabel('Density')
plt.title('Histogram of Price Distribution')
plt.savefig('C:/Users/gagat/Documents/magisterka/wykresy/histPrice.png')
plt.show()

plt.figure(6)
fig, ax = plt.subplots(figsize=(10,8))
plt.suptitle('')
homes_rooms_shuffle.plot(y='wifi', kind='hist', bins =100, range=(0,365), ax=ax, color='steelblue')
#dfAA['Distance'].plot(kind='hist', bins =30, range=(0,3000))
plt.xlabel('Dostępnosć w dniach w ciągu roku')
plt.ylabel('Liczebnosć w scali logarytmicznej')
plt.title('Histogram of Availability Distribution')
plt.yscale('log')
plt.savefig('C:/Users/gagat/Documents/magisterka/wykresy/histAvailability.png')
plt.show()

plt.figure(6)
fig, ax = plt.subplots(figsize=(10,8))
plt.suptitle('')
homes_rooms_shuffle.plot(y='calculated_host_listings_count', kind='hist', bins =40, range=(0,40), ax=ax, color='steelblue')
#dfAA['Distance'].plot(kind='hist', bins =30, range=(0,3000))
plt.xlabel('Ilu hostów ma daną liczbę ofert na Airbnb')
plt.ylabel('Liczebnosć w scali logarytmicznej')
plt.title('Histogram of Host Listings Count Distribution')
plt.yscale('log')
plt.savefig('C:/Users/gagat/Documents/magisterka/wykresy/histHost_Listings_count.png')
plt.show()

plt.figure(6)
fig, ax = plt.subplots(figsize=(10,8))
plt.suptitle('')
homes_rooms_shuffle.plot(y='beds', kind='hist', bins =11, range=(0,10), ax=ax, color='steelblue')
#dfAA['Distance'].plot(kind='hist', bins =30, range=(0,3000))
plt.xlabel('Beds')
plt.ylabel('Density')
plt.title('Histogram of Beds Distribution')
plt.savefig('C:/Users/gagat/Documents/magisterka/wykresy/histBeds.png')
plt.show()

plt.figure(15)
fig, ax = plt.subplots(figsize=(10,8))
plt.suptitle('')
homes_rooms_shuffle.plot(y='bedrooms', kind='hist', bins =11, range=(0,10), ax=ax, color='steelblue')
#dfAA['Distance'].plot(kind='hist', bins =30, range=(0,3000))
plt.xlabel('Beds')
plt.ylabel('Density')
plt.title('Histogram of Beds Distribution')
plt.savefig('C:/Users/gagat/Documents/magisterka/wykresy/histBedrooms.png')
plt.show()
