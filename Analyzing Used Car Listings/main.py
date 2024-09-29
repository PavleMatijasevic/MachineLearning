# jupyter notebook
import pandas as pd
import numpy as np


autos = pd.read_csv('autos.csv', encoding='Latin-1')
print(autos.info())
print(autos.head())


print(autos.columns)
print(autos.head())


autos.describe(include='all')

#print(autos["nrOfPictures"].value_counts())

# It looks like the num_photos column has 0 for every column
autos = autos.drop(["nrOfPictures", "seller", "offerType"], axis=1)


#There are two columns(price and auto) which are numeric values with extra characters being stored as text. We'll clean and convert these
autos["price"].replace("$","").replace(",","").astype(int)
print(autos["price"].head())

###

autos["kilometer"] = (autos["kilometer"].replace("km","").replace(",","").astype(int))
autos.rename({"kilometer":"kilometer_km"}, axis=1, inplace=True)

print(autos["kilometer_km"].head())

print("Print: ")
print(autos["kilometer_km"].value_counts())

print(autos["price"].unique().shape)
print(autos["price"].describe())
print(autos["price"].value_counts().head(20))


print(autos["price"].value_counts().sort_index(ascending=False).head(20))
print(autos["price"].value_counts().sort_index(ascending=True).head(20))


autos = autos[autos["price"].between(1,351000)]
print(autos["price"].describe())


print(autos[['dateCrawled', 'dateCreated', 'lastSeen']][0:5])

print(autos["dateCrawled"].str[:10].value_counts(normalize=True, dropna=False).sort_index())

print(autos["dateCrawled"].str[:10].value_counts(normalize=True, dropna=False).sort_values())

print(autos["dateCreated"].str[:10].unique().shape)
print(autos["dateCreated"].str[:10].value_counts(normalize=True, dropna=False).sort_index())

print(autos["yearOfRegistration"].describe())

print("Percentage of our data with invalid values in column yearOfRegistration: ")
print((~autos["yearOfRegistration"].between(1900,2016)).sum() / autos.shape[0])


autos = autos[autos["yearOfRegistration"].between(1900,2016)]
print(autos["yearOfRegistration"].value_counts(normalize=True).head(10))

print("Exploring price by brand: ")
print(autos["brand"].value_counts(normalize=True))

brand_counts = autos["brand"].value_counts(normalize=True)
common_brands = brand_counts[brand_counts > .05].index
print(common_brands)

brand_mean_prices = {}
for brand in common_brands:
    brand_only = autos[autos["brand"] == brand]
    mean_price = brand_only["price"].mean()
    brand_mean_prices[brand] = int(mean_price)

print(brand_mean_prices)



print("Exploring mileage")
bpm_series = pd.Series(brand_mean_prices)
print(pd.DataFrame(bpm_series, columns=["mean_price"]))


brand_mean_mileage = {}
for brand in common_brands:
    brand_only = autos[autos["brand"] == brand]
    mean_mileage = brand_only["kilometer_km"].mean()
    brand_mean_mileage[brand] = int(mean_mileage)

mean_mileage = pd.Series(brand_mean_mileage).sort_values(ascending=False)
mean_prices = pd.Series(brand_mean_prices).sort_values(ascending=False)

brand_info = pd.DataFrame(mean_mileage, columns=['mean_mileage'])
print(brand_info)

brand_info["mean_price"] = mean_prices
print(brand_info)










