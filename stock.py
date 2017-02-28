

# -*- coding: utf-8 -*-


import pandas as pd
import tushare as tu
from tushare.stock import cons as ct
from datetime import datetime
from pymongo import *


def load_all_data(start):

    client = MongoClient("mongodb://localhost:32017/")
    k_table = client.kdatabase.ktable

    start = "2017-02-08" if start is None else start

    for (k, v) in ct.INDEX_SYMBOL.items():

        try:

            data = tu.get_k_data(code=k, start=start)

        except Exception as err:
            print(err)
            continue

        for row in data.T.to_dict().items():
            # print("--------------------------%s" % type(row))
            row_data = row[1]
            row_data['date'] = datetime.strptime(row_data['date'], '%Y-%m-%d')
            print(row_data)
            k_table.insert_one(row_data)


def get_data(code, start):

    client = MongoClient("mongodb://localhost:32017/")
    k_table = client.kdatabase.ktable
    result = k_table.find({"code": code, "date": {"$gt": datetime.strptime(start, '%Y-%m-%d')}})

    seq = []
    for d in result:
        seq.append(d)

    data = pd.DataFrame(seq, columns=['date', 'code', 'open', 'close', 'high', 'low', 'volume'])
    print (data)
    return data


# test code
if __name__ == "__main__":

    # load_all_data('2017-02-08')

    get_data('399808', '2017-02-15')
