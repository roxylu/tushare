import datetime
import os
import sys 

import pandas as pd
import tushare as ts


DOWNLOAD_DIR = os.path.curdir + '/stockdata/'
STOCK_BASIC_CSV = DOWNLOAD_DIR + 'stock_basic_list.csv'

#60000-604000
#00000-003000

def download_stock_basic_info():
    df = ts.get_stock_basics()
    df.to_csv(STOCK_BASIC_CSV)
    print 'Download csv finished'


def get_all_stock_id():
    df = pd.DataFrame.from_csv(STOCK_BASIC_CSV)
    ids = []
    for i in df.index:
        ids.append(i)
    return ids

"""
def download_stock_kline(code, date_start='', date_end=datetime.date.today()):
    code = str(code).zfill(6)

    try:
        file_name = 'h_kline_' + str(code) + '.csv'
        write_mode = 'w'

        if os.path.exists(
"""
