import json                                                                    
import tushare as ts                                                           
from pymongo import MongoClient                                                
from tqdm import tqdm
from utils import get_all_stock_id                                             
                                                                               
                                                                               
client = MongoClient()                                                         
db = client.stock                                                              
all_codes = get_all_stock_id()                                                 
for code in tqdm(all_codes):
    code = str(code).zfill(6)                                                  
    try:
        df = ts.get_k_data(code, ktype='60', start='2016-12-01', end='2016-12-31') 
        result = json.loads(df.to_json(orient='records'))                          
        db.tickdata_60.insert(result)  
    except Exception, e:
        print "[-] Error (%s) = %s" % (code, str(e))
