import os
import pandas as pd
from pymongo import MongoClient
import unidecode

def processing(text):
    text = text.lower()
    text = unidecode.unidecode(text)

    return text

dir_path = os.path.dirname(os.path.abspath(__file__))
DATA = dir_path + "/res/train.tsv"
MONGO = os.environ.get("MONGO", "localhost:27017")

client = MongoClient(MONGO)
client.drop_database("sentiment")
db = client['sentiment']

df = pd.read_csv(DATA, sep="\t")

print("... Importing data into database (around 3 min)")
counter = 0
for index, row in df.iterrows():
    db["text"].insert_one({"_id": counter, "sentence": processing(row["Phrase"]), "polarity": row["Sentiment"]})
    counter+=1
