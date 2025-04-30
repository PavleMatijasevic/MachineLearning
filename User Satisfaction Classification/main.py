
# Na osnovi karakteristika korisnika i usluge
# potrebno je predvideti da li ce korisnik biti zadovoljan ili ne

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import roc_curve, roc_auc_score


# ucitavanje podataka

df = pd.read_csv("customer_satisfaction.csv")
df.info()
df.head()


X = df.drop("satisfaction", axis = 1)
y = df["satisfaction"]

# Podela na numericke i kategorijske kolone
categorical_col = ["gender", "service_type"]
numeric_col = ["age", "response_time", "num_interactions"]

preprocessor = ColumnTransformer(transformers=[
    ("cat", OneHotEncoder(drop="first"), categorical_col),
    ("num", StandardScaler(), numeric_col)
])

# Podela na train i test skup
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size= 0.2, stratify=y, random_state= 42
)

model_pipeline = Pipeline(steps = [
    ("preprocessing", preprocessor),
    ("classifier", LogisticRegression())
])

# Treniranje modela
model_pipeline.fit(X_train, y_train)

# Evaluacija na test skupu
y_pred = model_pipeline.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
report = classification_report(y_test, y_pred, output_dict=True)


print("Accuracy: ", accuracy)
print("\nConfusion matrix: ", conf_matrix)
print("\nClassification report: ", report)


# Zamena modela u pipeline-u sa Random Forest klasifikatorom

rf_pipeline = Pipeline(steps=[
    ("preprocessing", preprocessor),
    ("classifier", RandomForestClassifier(n_estimators=100, random_state=42))
])

# Treniranje Random Forest modela
rf_pipeline.fit(X_train, y_train)


y_pred_rf = rf_pipeline.predict(X_test)
accuracy_rf = accuracy_score(y_test, y_pred_rf)
conf_matrix_rf = confusion_matrix(y_test, y_pred_rf)
report_rf = classification_report(y_test, y_pred_rf)

print(accuracy_rf)
print(conf_matrix_rf)
print(report_rf)



# ROC kriva za Random forest model:

# Predikcija verovatnoca za ROC krivu random forest modela
y_prob_rf = rf_pipeline.predict_proba(X_test)[:,1]

# Izracunavanje ROC krive
fpr, tpr, thresholds = roc_curve(y_test, y_prob_rf)
auc_score = roc_auc_score(y_test, y_prob_rf)

# Prikazivanje ROC krive
plt.figure(figsize=(8, 6))
plt.plot(fpr, tpr, label = f"Random Forest (AUC = {auc_score:.2f})")
plt.plot([0,1], [0,1], linestyle = "--", color="gray")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Kriva - Random forest")
plt.legend(loc="lower right")
plt.grid(True)
plt.show()


# Rucno testiranje nekog korisnika
new_data = pd.DataFrame([{
    "age": 35,
    "gender": "female",
    "service_type": "standard",
    "response_time": 4.2,
    "num_interactions": 3
}])


# Predikcija zadovoljstva korisnika
predicted_class = int(rf_pipeline.predict(new_data)[0])
predicted_prob = rf_pipeline.predict_proba(new_data)[0][1]

predicted_class, predicted_prob

if predicted_class == 1:
    print("Korisnik ce biti zadovoljan i to je verovatno ", predicted_prob)
else:
    print("Korisnik nece biti zadovoljan i to je verovatno ", predicted_prob)



# Vizuelizacija vaznosti osobina
# Dohvatanje kolona nakon OneHotEncoding-a

encoded_feature_names = rf_pipeline.named_steps["preprocessing"].get_feature_names_out()
feature_importances = rf_pipeline.named_steps["classifier"].feature_importances_

# Kreiranje DataFrame-a za sortiranje i prikaz
importance_df = pd.DataFrame({
    "Feature": encoded_feature_names,
    "Importance": feature_importances
}).sort_values(by="Importance", ascending=False)

top_features = importance_df.head(6)

plt.figure(figsize=(10, 6))
sns.barplot(data=top_features, x = "Importance", y = "Feature")
plt.title("Top 10 najvaznijih osobina za predikciju zadovoljstva")
plt.xlabel("Znacaj")
plt.ylabel("Osobina")
plt.grid(True)
plt.tight_layout()
plt.show()



