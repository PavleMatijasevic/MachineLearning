import numpy as np
import pandas as pd

np.random.seed(42)  # za ponovljivost

n = 10000

age = np.random.randint(18, 61, size=n)
education_levels = np.random.choice(['primary', 'high_school', 'bachelor', 'master', 'phd'], size=n, p=[0.1, 0.3, 0.35, 0.2, 0.05])
experience_years = np.clip((age - 18) + np.random.randint(-5, 6, size=n), 0, 40)
num_certificates = np.random.poisson(1.5, size=n)
english_level = np.random.choice(['basic', 'intermediate', 'advanced'], size=n, p=[0.3, 0.5, 0.2])
score_test = np.clip(np.random.normal(65, 15, size=n), 0, 100)
has_recommendation = np.random.choice([0, 1], size=n, p=[0.6, 0.4])
city_size = np.random.choice(['small', 'medium', 'large'], size=n, p=[0.3, 0.4, 0.3])

# Na osnovu pravila generišemo target "hired"
# (složenija logika da bi bilo realno)
hired = []
for i in range(n):
    score = 0
    if education_levels[i] in ['master', 'phd']:
        score += 2
    elif education_levels[i] == 'bachelor':
        score += 1
    if experience_years[i] > 5:
        score += 1
    if num_certificates[i] >= 2:
        score += 1
    if english_level[i] == 'advanced':
        score += 1
    if score_test[i] > 70:
        score += 1
    if has_recommendation[i]:
        score += 1
    hired.append(1 if score >= 4 else 0)

df = pd.DataFrame({
    'age': age,
    'education_level': education_levels,
    'experience_years': experience_years,
    'num_certificates': num_certificates,
    'english_level': english_level,
    'score_test': score_test,
    'has_recommendation': has_recommendation,
    'city_size': city_size,
    'hired': hired
})

print(df.head())

df.to_csv("candidate_dataset.csv", index=False)

