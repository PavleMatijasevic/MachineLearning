from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import numpy as np

# Generisanje podataka - simulirani primeri pozitivnih i negativnih brojeva
X = np.array([[1], [2], [3], [-1], [-2], [-3], [4], [100], [-5]])  # ulazni podaci
y = np.array([1, 1, 1, 0, 0, 0, 1, 1, 0])  # oznake (1 za pozitivne brojeve, 0 za negativne)

# Podela podataka na skup za treniranje i testiranje
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Kreiranje i treniranje modela logisticke regresije
model = LogisticRegression()
model.fit(X_train, y_train)

# Evaluacija modela
accuracy = model.score(X_test, y_test)
print("Tacnost modela:", accuracy)

# Testiranje na novim podacima
new_data = np.array([[5], [-5], [9], [-8]])
predictions = model.predict(new_data)
print("Predikcije za nove podatke:", predictions)

user_input = float(input("Unesite broj: "))
user_data = np.array([[user_input]])

# Predikcija za korisnicki unos
prediction = model.predict(user_data)
if prediction == 1:
    print("Uneseni broj je pozitivan.")
else:
    print("Uneseni broj je negativan.")



