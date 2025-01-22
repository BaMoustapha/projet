import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#  Charger les données nettoyées
file_path = "covid19_data_cleaned.csv"
df = pd.read_csv(file_path)

#  Vérification des colonnes disponibles
print("🔹 Noms des colonnes :")
print(df.columns)

#  Suppression des espaces dans les noms de colonnes
df.columns = df.columns.str.strip()

#  Aperçu des données nettoyées
print("\n🔹 Aperçu des données :")
print(df.head())

# Vérification et gestion des valeurs manquantes
print("\n🔹 Vérification des valeurs manquantes :")
print(df.isnull().sum())

# Remplissage des valeurs manquantes (exemple : âge et cas)
if 'age' in df.columns:
    df['age'] = df['age'].fillna(df['age'].median())
if 'cases' in df.columns:
    df['cases'] = df['cases'].fillna(df['cases'].median())

#  Statistiques de base 
print("\n🔹 Statistiques descriptives :")
print(df.describe())

if 'age' in df.columns:
    print(f"\n📊 Moyenne d'âge : {df['age'].mean():.2f}")
    print(f"📊 Médiane d'âge : {df['age'].median():.2f}")
    print(f"📊 Étendue d'âge : {df['age'].min()} - {df['age'].max()} (Différence : {df['age'].max() - df['age'].min()})")

if 'cases' in df.columns:
    print(f"\n📊 Nombre total de cas : {df['cases'].sum()}")
    print(f"📊 Nombre moyen de cas : {df['cases'].mean():.2f}")

#  Histogramme de l'âge
if 'age' in df.columns:
    plt.figure(figsize=(8, 5))
    plt.hist(df['age'], bins=20, color="blue", edgecolor="black", alpha=0.7)
    plt.title("Distribution des âges")
    plt.xlabel("Âge")
    plt.ylabel("Fréquence")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.savefig("distribution_age.png", format="png")  
    plt.show()  

#  Histogramme du nombre de cas
if 'cases' in df.columns:
    plt.figure(figsize=(8, 5))
    plt.hist(df['cases'], bins=20, color="red", edgecolor="black", alpha=0.7)
    plt.title("Distribution des cas de COVID-19")
    plt.xlabel("Nombre de cas")
    plt.ylabel("Fréquence")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.savefig("distribution_cases.png", format="png")  
    plt.show()  

#  Boxplot de l'âge
if 'age' in df.columns:
    plt.figure(figsize=(6, 4))
    sns.boxplot(y=df['age'], color="lightblue")
    plt.title("Boxplot des âges")
    plt.ylabel("Âge")
    plt.savefig("boxplot_age.png", format="png") 
    plt.show()  

#  Boxplot du nombre de cas
if 'cases' in df.columns:
    plt.figure(figsize=(6, 4))
    sns.boxplot(y=df['cases'], color="lightcoral")
    plt.title("Boxplot des cas de COVID-19")
    plt.ylabel("Nombre de cas")
    plt.savefig("boxplot_cases.png", format="png")  
    plt.show()  

df_numeric = df.select_dtypes(include=['number'])

#  Matrice de corrélation
plt.figure(figsize=(8, 6))
sns.heatmap(df_numeric.corr(), annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.title("Matrice de corrélation")
plt.savefig("correlation_matrix.png", format="png")  
plt.show() 


