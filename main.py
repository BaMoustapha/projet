import pandas as pd

# Charger le fichier CSV dans un DataFrame
file_path = "covid19_data.csv"  
df = pd.read_csv(file_path)

# Vérifier les premières lignes
print("🔹 Aperçu des premières lignes du dataset :")
print(df.head())

# Vérifier la taille du dataset
print(f"\n🔹 Nombre de lignes: {df.shape[0]}, Nombre de colonnes: {df.shape[1]}")

# Vérifier les informations générales sur les colonnes
print("\n🔹 Informations générales sur les données :")
print(df.info())

# Statistiques de base sur les valeurs numériques
print("\n🔹 Statistiques descriptives :")
print(df.describe())

# Vérification des valeurs uniques dans les colonnes catégorielles
print("\n🔹 Valeurs uniques pour les colonnes catégorielles :")
for col in df.select_dtypes(include=['object']).columns:
    print(f"{col}: {df[col].unique()}") 
    
# Vérifier les valeurs manquantes
print("\n🔹 Nombre de valeurs manquantes par colonne :")
print(df.isnull().sum())

# Supprimer les lignes avec trop de valeurs manquantes (si plus de 20% des valeurs sont nulles)
df = df.dropna(thresh=df.shape[1] * 0.8)

# Remplacer les valeurs nulles par des valeurs par défaut
if 'age' in df.columns:
    df['age'].fillna(df['age'].median(), inplace=True) 
if 'classification' in df.columns:
    df['classification'].fillna('Inconnu', inplace=True)  

# Vérification des valeurs aberrantes (ex : âge négatif ou trop élevé)
if 'age' in df.columns:
    print("\n🔹 Vérification des valeurs aberrantes (âge) :")
    print(df['age'].describe()) 

    # Suppression des âges invalides
    df = df[df['age'] > 0]

# Transformer les dates en format datetime si nécessaire
if 'date' in df.columns:
    df['date'] = pd.to_datetime(df['date'], errors='coerce')

if 'age' in df.columns:
    df['groupe_age'] = pd.cut(df['age'], bins=[0, 18, 35, 60, 120], labels=['Enfant', 'Jeune', 'Adulte', 'Senior'])

# Afficher un aperçu final après nettoyage
print("\n🔹 Aperçu des données après nettoyage :")
print(df.head())

# Vérifier les valeurs manquantes après traitement
print("\n🔹 Valeurs manquantes après nettoyage :")
print(df.isnull().sum())

# Sauvegarder le dataset nettoyé (optionnel)
df.to_csv("covid19_data_cleaned.csv", index=False)
print("\n Données nettoyées et sauvegardées sous 'covid19_data_cleaned.csv'")
