import sys 

import numpy as np
import pandas as pd
from pandas.tseries.offsets import BDay
import tushare as ts

from utils import get_all_stock_id

#60000-604000
#00000-003000

def find_mouse(all_codes, date_start, date_end):
    print "[+] Finding Mouse from %s to %s" % (date_start, date_end)
    codes = []
    for code in all_codes:
        code = str(code).zfill(6)
        try:
            df=ts.get_k_data(code, start=date_start, end=date_end)
            df['open'] = df['open'].astype(float)
            df['close'] = df['close'].astype(float)
            df['high'] = df['high'].astype(float)
            df['low'] = df['low'].astype(float)
            df['bottom'] = np.where(df['open']>=df['close'], df['close'], df['open']).astype(float)
            df['percent'] = (df['bottom'] - df['low']) * 100 / df['bottom']
            if df['percent'].max() > 5:
                print "[+] Found %s" % code
                codes.append(code)
        except Exception, e:
            print "[-] Error (%s) = %s" % (code, str(e))
    print "----------FINISHED RUNNING----------"
    return codes


def write_to_file(filename, codes):
    output_file = open(filename, 'w')
    for code in codes:
	output_file.write("%s\n" % code)
    output_file.close()


if __name__ == '__main__':
    if len(sys.argv) > 1:
        start = sys.argv[1]
        end = sys.argv[2]
    else:
        today = pd.datetime.today()
        start = str((today - BDay(1)).date())
        end = str(today.date())
    all_codes = get_all_stock_id()
    codes = find_mouse(all_codes, start, end)
    write_to_file('output.txt', codes)
