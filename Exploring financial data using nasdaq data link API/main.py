from cProfile import label

import requests
import json
import pandas as pd
import config

import matplotlib.pyplot as plt

## configuring the api_key
api_key = config.Config

api_url = 'https://data.nasdaq.com/api/v3/datatables/MER/F1.json'

parameters = {
    'api_key' : api_key,
    'qopts.per_page' : 10 # number of rows to fetch
}

#fetching the data and converting it to json
json_data = requests.get(api_url, params=parameters).json()

print(json_data)



api_url = 'https://data.nasdaq.com/api/v3/datatables/MER/F1.json'
parameters = {
    'api_key': api_key,
    'qopts.per_page': 10000
}
json_data = requests.get(api_url, params=parameters).json()
data = json_data['datatable']['data']
columns = [col['name'] for col in json_data['datatable']['columns']]

df_metric = pd.DataFrame(data, columns=columns)
print('\n')
print(df_metric.head())

print(df_metric.head(0))
necessary_columns=['reportid', 'reportdate', 'reporttype', 'amount', 'longname', 'country', 'region', 'indicator', 'statement']

df_metric = df_metric[necessary_columns]
filtered_df = df_metric[df_metric['indicator'] == 'Accrued Expenses Turnover']
print(filtered_df['indicator'].describe())

#Enhancing the dataFrame

def update_country_name(name):
    if name == 'USA':
        name = 'United State of America'
    elif name == 'JPN':
        name = 'Japan'
    elif name == 'CYM':
        name = 'Cayman Islands'
    elif name == 'BHS':
        name = 'Bahamas'
    elif name == 'DEU':
        name = 'Germany'
    else:
        name = 'Ireland'
    return  name

filtered_df = filtered_df.copy()
filtered_df['country_name'] = filtered_df['country'].apply(update_country_name)
filtered_df.columns = ['report_id', 'report_date', 'report_type', 'amount', 'company_name', 'country', 'region', 'indicator', 'statement', 'country_name']
updated_df = filtered_df.copy()
print(updated_df['country_name'].value_counts())

updated_df['report_date'] = pd.to_datetime(updated_df['report_date'])
updated_df = updated_df[(updated_df['report_date'].dt.year >= 2010) & (updated_df['report_date'].dt.year <= 2015)]

relevant_data = updated_df[['company_name', 'report_date', 'amount']].copy()


plt.figure(figsize=(12,6))

for company in relevant_data['company_name'].unique():
    company_data = relevant_data[relevant_data['company_name'] == company]
    plt.plot(company_data['report_date'], company_data['amount'], label=company)

plt.title('Trend Analysis of Accrued Expenses Turnover (2010-2015)')
plt.xlabel('Report Date')
plt.ylabel('Accrued Expenses Turnover')
plt.xticks(rotation=45)
plt.legend(title='Company', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

country_avg = updated_df.groupby('country_name')['amount'].mean()
plt.figure(figsize=(12,6))
country_avg.sort_values(ascending=False).plot(kind='bar')
plt.title('Average financial metric by country')
plt.xlabel('Country')
plt.ylabel('Average Amount')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()








