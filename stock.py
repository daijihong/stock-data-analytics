

# -*- coding: utf-8 -*-


import pandas as pd
import tushare as tu
from tushare.stock import cons as ct
from datetime import datetime
from pymongo import *
import requests





'''
功能：拉取A股股票数据，保存到mongoDb(可以拉全量数据，也可以拉增量数据)
'''

def save_all_data(start):
    for fq in ['afq', 'hfq', None]:
        save_all_data(start, fq)





'''
功能：拉取A股股票数据，保存到mongoDb(可以拉全量数据，也可以拉增量数据)

autype:string
                  复权类型，qfq-前复权 hfq-后复权 None-不复权，默认为qfq

'''
def save_all_data(start, autype='qfq'):

    client = MongoClient("mongodb://localhost:32017/")
    k_table = client.kdatabase.ktable + "_" + autype

    start = "2017-02-08" if start is None else start

    #从配置表里取股票代码
    for (k, v) in ct.INDEX_SYMBOL.items():

        try:

            data = tu.get_k_data(code=k, start=start, autype='qfq')

        except Exception as err:
            print(err)
            continue

        for row in data.T.to_dict().items():
            # print("--------------------------%s" % type(row))
            row_data = row[1]
            row_data['date'] = datetime.strptime(row_data['date'], '%Y-%m-%d')
            print(row_data)
            k_table.insert_one(row_data)




#00585
def get(code):

    client = MongoClient("mongodb://localhost:32017/")
    k_table = client.kdatabase.ktable + "_paixi"

    url = "http://stock.finance.sina.com.cn/hkstock/dividends/%s.html" % code

    resp = requests.get(url)

    content = resp.content.decode("gb2312")

    tbody = content.split("<tbody>")[1].split("</tbody>")[0]

    rows = tbody.split("</tr>")[1:]

    tb = list()
    for row in rows:
        tds = row.split("<td>")[1:]

        values = list()
        for td in tds:
            value = td.split("</td>")[0]
            values.append(value)


        row_data = {'公布日期': values[0],
                   '年度':     values[1],
                   '派息事项': values[2],
                   '派息内容': values[3],
                   '方式':     values[4],
                   '除净日':   values[5],
                   '截止过户日期': values[6],
                   '派息日期': values[7],
                   }

        k_table.insert_one(row_data)

    # rowTd = map(lambda row: row.split("</td>")[0], rows)





    return tb



'''
从mongoDb查询股票数据
'''
def get_data(code, start, autype='qfq'):

    client = MongoClient("mongodb://localhost:32017/")
    k_table = client.kdatabase.ktable + "_" + autype
    result = k_table.find({"code": code, "date": {"$gt": datetime.strptime(start, '%Y-%m-%d')}})

    seq = []
    for d in result:
        seq.append(d)

    data = pd.DataFrame(seq, columns=['date', 'code', 'open', 'close', 'high', 'low', 'volume'])
    print (data)
    return data


# test code
if __name__ == "__main__":

    save_all_data('2017-02-08')

    get_data('399808', '2017-02-15')
