import json
import numpy as np
import pandas as pd
from pymongo import MongoClient
from stockstats import StockDataFrame
from tqdm import tqdm

client = MongoClient()
db=client.stock
cursor=db.tickdata_60.find({'code':{'$regex':'^300*'}})

documents = []
for document in tqdm(cursor):
    document.pop('_id')
    documents.append(document)

json_str = json.dumps(documents)

df = pd.read_json(json_str, orient='records')
stock = StockDataFrame.retype(df) 
stock['kdjk']
df['promising'] = np.where(
    (df['kdjk'].astype(int) == df['kdjd'].astype(int)) & 
    (df['kdjk'].astype(int) == df['kdjj'].astype(int)), df['kdjk'], np.nan)
