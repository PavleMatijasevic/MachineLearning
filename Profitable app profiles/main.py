from csv import reader
from idlelib.iomenu import encoding
from idlelib.sidebar import LineNumbers

from Tools.scripts.nm2def import export_list
from tensorflow import unique

opened_file = open('googleplaystore.csv', encoding="utf8")
read_file = reader(opened_file)
android = list(read_file)
android_header = android[0]
android = android[1:]


opened_file = open('AppleStore.csv', encoding="utf8")
read_file = reader(opened_file)
ios = list(read_file)
ios_header = ios[0]
ios = ios[1:]

ios_header = ios_header[1:]

def explore_data(dataset, start, end, rows_and_columns=False):
    dataset_slice = dataset[start:end]
    for row in dataset_slice:
        print(row)
        print('\n')

    if rows_and_columns:
        print('Number of rows: ', len(dataset))
        print('Number of columns: ', len(dataset[0]))


print(android_header)
print('\n')
explore_data(android, 0, 3, True)


print(ios_header)
print('\n')
explore_data(ios, 0, 3, True)


print(android[10472])
print('\n')
print(android_header)
print('\n')
print(android[0])


print(len(android))
#del android[10472]
#print(len(android))


for app in android:
    name = app[0]
    if name == 'Instagram':
        print(app)


duplicate_apps = []
unique_apps = []

for app in android:
    name = app[0]
    if name in unique_apps:
        duplicate_apps.append(name)
    else:
        unique_apps.append(name)

print('Number of duplicate apps: ', len(duplicate_apps))
print('\n')
print('Examples of duplicate apps: ', duplicate_apps[:15])

reviews_max = {}

for app in android:
    name = app[0]
    n_reviews = float(app[2])
    if name in reviews_max and reviews_max[name] < n_reviews:
        reviews_max[name] = n_reviews
    elif name not in reviews_max:
        reviews_max[name] = n_reviews

print('Expected length: ', len(android) - 1181)
print('Actual length: ', len(reviews_max))


android_clean = []
already_added = []

for app in android:
    name = app[0]
    n_reviews = float(app[2])

    if(reviews_max[name] == n_reviews) and (name not in already_added):
        android_clean.append(app)
        already_added.append(name)

explore_data(android_clean, 0, 3, True)

def is_english(string):
    non_ascii = 0

    for character in string:
        if ord(character) > 127:
            non_ascii += 1

    if non_ascii > 3:
        return False
    else:
        return True

print(is_english('Instagram'))
print(is_english('爱奇艺PPS -《欢乐颂2》电视剧热播'))

print(is_english('Docs To Go™ Free Office Suite'))
print(is_english('Instachat 😜'))

android_english = []
ios_english = []

for app in android_clean:
    name = app[0]
    if is_english(name):
        android_english.append(app)

for app in ios:
    name = app[1]
    if is_english(name):
        ios_english.append(app)

explore_data(android_english, 0, 3, True)
print('\n')
explore_data(ios_english, 0, 3, True)


android_final = []
ios_final = []

for app in android_english:
    price = app[7]
    if price == '0':
        android_final.append(app)

for app in ios_english:
    # change from app[4] to app[5]
    price = app[5]
    if price == '0':
        ios_final.append(app)

print(len(android_final))
print(len(ios_final))


def freq_table(dataset, index):
    table = {}
    total = 0

    for row in dataset:
        total += 1
        value = row[index]
        if value in table:
            table[value] += 1
        else:
            table[value] = 1
    table_percentages = {}
    for key in table:
        percentage = (table[key] / total) *100
        table_percentages[key] = percentage
    return table_percentages

def display_table(dataset, index):
    table = freq_table(dataset, index)
    table_display = []
    for key in table:
        key_val_as_tuple = (table[key], key)
        table_display.append(key_val_as_tuple)

    table_sorted = sorted(table_display, reverse=True)
    for entry in table_sorted:
        print(entry[1], ':', entry[0])

#display_table(ios_final, -5)
#display_table(android_final, 1)
#display_table(android_final, -4)



# find most popular apps by genre
genres_ios = freq_table(ios_final, -5)

for genre in genres_ios:
    total = 0
    len_genre = 0
    for app in ios_final:
        genre_app = app[-5]
        if genre_app == genre:
            n_ratings = float(app[5])
            total += n_ratings
            len_genre += 1
    avg_n_ratings = total / len_genre
    print(genre, ':', avg_n_ratings)

print('\n')

for app in ios_final:
    if app[-5] == 'Navigation':
        print(app[2], ':', app[6])

print('\n')
for app in ios_final:
    if app[-5] == 'Reference':
        print(app[2], ':', app[6])

print('\n')
display_table(android_final, 5)
print('\n')


categories_android = freq_table(android_final, 1)
for category in categories_android:
    total = 0
    len_category = 0
    for app in android_final:
        category_app = app[1]
        if category_app == category:
            n_installs = app[5]
            n_installs = n_installs.replace(',', '')
            n_installs = n_installs.replace('+', '')
            total += float(n_installs)
            len_category += 1
    avg_n_installs = total / len_category
    print(category, ':', avg_n_installs)

print('\n')

for app in android_final:
    if app[1] == 'COMMUNICATION' and (app[5] == '1,000,000,000+' or app[5] == '500,000,000+' or app[5] == '100,000,000+'):
        print(app[0], ':', app[5])


under_100_m = []
for app in android_final:
    n_installs = app[5]
    n_installs = n_installs.replace(',', '')
    n_installs = n_installs.replace('+', '')
    if(app[1] == 'COMMUNICATION') and (float(n_installs)<100000000):
        under_100_m.append(float(n_installs))

print(sum(under_100_m) / len(under_100_m))

print('\n')

for app in android_final:
    if app[1] == 'BOOKS_AND_REFERENCE':
        print(app[0], ':', app[5])


print('\n')
for app in android_final:
    if app[1] == 'BOOKS_AND_REFERENCE' and (app[5] == '1,000,000,000+' or app[5] =='500,000,000+' or app[5] == '100,000,000+'):
        print(app[0], ':', app[5])