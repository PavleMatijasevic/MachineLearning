from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import numpy as np

# Ulazni podaci - numerički brojevi
X = np.array([[1], [2], [3], [-1], [-2], [-3], [4], [100], [-5], [6], [10], [7], [8], [9]])  
y = np.array([0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0])  # oznake (1 za parne brojeve, 0 za neparne)

# Podjela podataka na skupove za treniranje i testiranje
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Kreiranje i treniranje modela logističke regresije
model = LogisticRegression()
model.fit(X_train, y_train)

# Evaluacija modela
accuracy = model.score(X_test, y_test)
print("Točnost modela:", accuracy)

# Testiranje na novim podacima
new_data = np.array([[91], [-8], [11], [103]])
predictions = model.predict(new_data)
print("Predikcije za nove podatke:", predictions)

user_input = float(input("Unesite broj: "))
user_data = np.array([[user_input]])

# Predikcija za korisnički unos
prediction = model.predict(user_data)
if prediction == 1:
    print("Uneseni broj je paran.")
else:
    print("Uneseni broj je neparan.")
