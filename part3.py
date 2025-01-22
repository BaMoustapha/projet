import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

file_path = "covid19_data_cleaned.csv"
df = pd.read_csv(file_path)



###  Âge moyen des patients ###
if 'age' in df.columns:
    age_mean = df['age'].mean()
    print(f"\n Réponse 1 : L'âge moyen des patients atteints du COVID-19 est de {age_mean:.2f} ans.")

###   Variation des cas selon les mois ###
# Vérification et conversion de la colonne date
if 'date' in df.columns:
    df['date'] = pd.to_datetime(df['date'])
    df['month'] = df['date'].dt.month  # Extraction du mois

    # Regroupement par mois et somme des cas
    cases_per_month = df.groupby('month')['cases'].sum()

    # Affichage du graphique
    plt.figure(figsize=(8, 5))
    sns.barplot(x=cases_per_month.index, y=cases_per_month.values, palette="viridis")
    plt.xlabel("Mois")
    plt.ylabel("Nombre total de cas")
    plt.title(" Répartition des cas de COVID-19 par mois")
    plt.show()

    print("\n Réponse 2 : Le nombre de cas varie fortement selon les mois, avec un pic à certains moments de l'année.")

###  Pays avec le plus de cas ###
if 'country' in df.columns:
    top_countries = df.groupby('country')['cases'].sum().sort_values(ascending=False).head(10)

    # Affichage du graphique
    plt.figure(figsize=(8, 5))
    sns.barplot(x=top_countries.values, y=top_countries.index, palette="Reds_r")
    plt.xlabel("Nombre total de cas")
    plt.ylabel("Pays")
    plt.title("Top 10 des pays avec le plus de cas de COVID-19")
    plt.show()

    print("\n Réponse 3 : Les pays les plus touchés sont principalement les grandes nations industrialisées.")

if 'age' in df.columns and 'severity' in df.columns:
    plt.figure(figsize=(8, 6))
    sns.boxplot(x=df['severity'], y=df['age'], palette="coolwarm")
    plt.xlabel("Gravité du cas")
    plt.ylabel("Âge")
    plt.title(" Corrélation entre l'âge et la gravité du COVID-19")
    plt.show()

    print("\n Réponse 4 : Il semble y avoir une tendance où les cas graves concernent davantage les personnes âgées.")
