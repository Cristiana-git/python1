

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score

data = {
    "customer_id": [1, 2, 3, 4, 5],
    "invoice_amount": [100, 200, 300, 400, 500],
    "payment_delay": [0, 1, 0, 1, 0]  # Ce vrei să prezici
}

# Crează un DataFrame și salvează-l ca CSV
df_train = pd.DataFrame(data)
df_train.to_csv("train.csv", index=False)

# 1. Citirea fișierelor
train = pd.read_csv("train.csv")
test = pd.read_csv("test.csv")

# 2. Explorare de bază
print(train.head())
print(train.info())
print(train.describe())

# 3. Vizualizări
plt.figure(figsize=(8, 4))
sns.countplot(data=train, x="payment_delay")
plt.title("Distribuția întârzierilor la plată")
plt.show()

# Corelații
plt.figure(figsize=(12, 8))
correlation = train.corr(numeric_only=True)  # Adăugăm numeric_only=True pentru a evita erori
sns.heatmap(correlation, annot=True, cmap="coolwarm")
plt.title("Heatmap corelații")
plt.show()

# Boxplot sumă factură vs întârzieri
plt.figure(figsize=(8, 4))
sns.boxplot(data=train, x="payment_delay", y="invoice_amount")
plt.title("Suma facturii vs întârzieri")
plt.show()

# 4. Preprocesare
# Eliminăm coloanele irelevante
features_to_drop = ["payment_delay", "customer_id"]
X = train.drop(columns=features_to_drop, errors='ignore')
y = train["payment_delay"]

# Separare date
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardizare
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_val_scaled = scaler.transform(X_val)

# 5. Antrenare model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train_scaled, y_train)

# Predicții
y_pred = model.predict(X_val_scaled)
y_prob = model.predict_proba(X_val_scaled)[:, 1]

# Evaluare
print(classification_report(y_val, y_pred))
print("ROC AUC:", roc_auc_score(y_val, y_prob))

# 6. Predicții pe test
X_test = test.drop(columns=["customer_id"], errors='ignore')
X_test_scaled = scaler.transform(X_test)
test_prob = model.predict_proba(X_test_scaled)[:, 1]
test["probability"] = test_prob

# 7. Export top 300
top_300 = test.sort_values(by="probability", ascending=False).head(300)

# Dacă vrei indexul original + 1 (ca ID în competiție, de ex.)
top_300_indices = top_300.index + 1
top_300_indices.to_csv("top_300_submission.csv", index=False, header=False)
