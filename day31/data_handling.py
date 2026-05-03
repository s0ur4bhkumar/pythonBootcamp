import pandas as pd

data = pd.read_csv("./day31/data/french_words.csv")
vocabulary = data.to_dict(orient="records")
