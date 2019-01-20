# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 16:00:29 2018

@author: gagat
"""


from geopy.distance import geodesic
import pandas as pd
import numpy as np

city =['Austin/Austin', 'Boston/Boston', 'Chicago/Chicago', 'Columbus/Columbus', 'Denver/Denver', 'Los Angeles/LosAngeles',
       'Nashville/Nashville', 'New Orlean/NewOrlean', 'New York City/NewYork', 'Oakland/Oakland', 'Portland/Portland',
       'San Diego/SanDiego', 'San Francisco/SanFrancisco', 'Santa Clara County/SantaClara','Seattle/Seattle', 
       'Twin Cities MSA/TwinCities','Washington/Washington']



#city = ['Austin/Austin', 'Boston/Boston', 'Chicago/Chicago']
city2 = ['Austin', 'Boston', 'Chicago', 'Columbus', 'Denver', 'Los Angeles','Nashville', 'New Orlean', 
       'New York City', 'Oakland', 'Portland','San Diego', 'San Francisco','Santa Clara County', 'Seattle', 'Twin Cities MSA',
       'Washington']

latCentrum= [30.263569, 42.357412, 41.876465, 39.965714, 39.743171, 34.066398, 36.159886, 29.951853, 
             40.748441, 37.802079, 45.517572, 32.799532, 37.788031, 37.376523, 47.610136, 
             44.972474, 38.897676]
longCentrum = [-97.739606, -71.053081, -87.621887, -83.002846, -104.992593, -118.412864, -86.777276, -90.067946,
               -73.985664, -122.27288, -122.680038, -117.257829, -122.401879, -122.061496, -122.342057, 
               -93.27294, -77.03653]

def count_distance(distance, nrows1, location, Centrum):
    for i in range(nrows1):
            distance.append(geodesic(location.iloc[i,:], Centrum).kilometers)


for k in range(17):
    url = 'C:/Users/gagat/Documents/magisterka/' + city[k] + '.csv'

    df= pd.read_csv(url, sep=',', na_values='')


# Empire State Building

    Centrum = (latCentrum[k], longCentrum[k])

    latitude = df['latitude'].values
    longitude = df['longitude'].values
    data = {'latitude': latitude, 'longitude': longitude}
    location = pd.DataFrame(data)
    location.head()

    nrows1 = df.shape[0]
    distance = []
        
    count_distance(distance, nrows1, location, Centrum)
  
    df['distance'] = distance
    df.distance = round(df.distance, 2)    
    #df.describe()




    cols = ['id', 'room_type','price', 'number_of_reviews', 'reviews_per_month', 
        'calculated_host_listings_count', 'availability_365', 'distance']
    df=df[cols]


    url2='C:/Users/gagat/Documents/magisterka/' + city2[k] + '/listings.csv'
    df_detailed= pd.read_csv(url2, sep=',', na_values='')



    cols_added = ['id', 'host_is_superhost', 'host_identity_verified', 'city', 'property_type', 'accommodates', 'bathrooms', 'bedrooms', 'beds', 'bed_type', 
              'amenities', 'guests_included', 'calendar_updated', 'review_scores_rating','instant_bookable', 'cancellation_policy']

    df_detailed = df_detailed[cols_added]

    df_detailed.city = city2[k]


#Lacze dwie tabele
    df_merged=pd.merge(left=df, right=df_detailed, on='id')


# usuwamy obsewacje odstajace
    df_merged = df_merged[df_merged.price<=4000]
# usuwamy obsewacje price == 0
    df_merged = df_merged[df_merged.price != 0]
#usuwamy price < 
    df_merged = df_merged[df_merged.price>=20]

    df_merged = df_merged[df_merged.number_of_reviews !=0]
    df_merged = df_merged[df_merged.room_type != 'Shared room']

    if k == 15:
        df_merged = df_merged[df_merged.distance <=5.5]
   
    df_merged = df_merged.reset_index()
    #nrows = df_merged.shape[0] 


#df_merged.reviews_per_month=df_merged.reviews_per_month.fillna(0)
#df_merged.review_scores_rating=df_merged.review_scores_rating.fillna(91)
#df_merged.host_is_superhost=df_merged.host_is_superhost.fillna('f')
#df_merged.bathrooms=df_merged.bathrooms.fillna(0)
#df_merged.beds=df_merged.beds.fillna(0)



#licze quantiles
    median_price= np.percentile(df_merged['price'], 50)
    price_25q= np.percentile(df_merged['price'], 25)
    price_75q= np.percentile(df_merged['price'], 75)

# grupuje ceny wynajmu w kategoriw dla kazdego kwantyla, <=60 to low-cost
    price_quantile = []
    price_quantile = pd.cut(df_merged['price'],
                            bins=[0, price_25q, median_price, price_75q, 10000],
                            labels=["low-cost","medium-priced","high-priced","expensive"])
    price_quantile.head()
    df_merged['price_quantile'] = price_quantile
    df_merged.price_quantile.value_counts(dropna=False)


    df_merged.info()
    url3= 'C:/Users/gagat/Documents/magisterka/'+ city2[k] + '/dane' + city2[k] + str(k) + '.csv'
    df_merged.to_csv(url3, sep=',', encoding='utf-8', index=False)

