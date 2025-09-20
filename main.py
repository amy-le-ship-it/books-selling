import pandas as pd

df = pd.read_csv('bestsellers.csv')

# Drop duplicates
df.drop_duplicates(inplace=True)

# Renaming Columns
df.rename(columns={"Name": "Title","Year": "Publication Year","User Rating": "Rating"}, inplace= True)

print(df.head())
print(df.columns)

# Convert the Data Types
df["Price"] = df["Price"].astype(float)

# Author Popularity
author_counts = df['Author'].value_counts()
print(author_counts)

# Average Rating By Genre
avg_rating_by_genre = df.groupby("Genre")["Rating"].mean()
print(avg_rating_by_genre)

author_counts.head(10).to_csv("top_authors.csv")

avg_rating_by_genre.to_csv("avg_rating_by_genre.csv")