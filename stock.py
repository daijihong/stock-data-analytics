

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


def pull_all_stock_kline(start):
    for fq in ['afq', 'hfq', None]:
        pull_stock_kline(start, fq)





'''
功能：拉取A股股票数据，保存到mongoDb(可以拉全量数据，也可以拉增量数据)

autype:string
                  复权类型，qfq-前复权 hfq-后复权 None-不复权，默认为qfq

'''


def pull_stock_kline(start, autype):

    client = MongoClient("mongodb://localhost:32017/")

    suffix = autype if autype is not None else 'none'
    k_table = client.kdatabase["ktable" + "_" + suffix]

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





'''
#00585

犯了个错误，照着港股票的页面写的，解析了港股的页面
A股也类似解析，没时间改了:)

'''


def pull_dividends(code):

    client = MongoClient("mongodb://localhost:32017/")
    k_table = client.kdatabase['ktable' + "_dividends"]

    url = "http://stock.finance.sina.com.cn/hkstock/dividends/%s.html" % code

    resp = requests.get(url)

    content = resp.content.decode("gb2312")

    tbody = content.split("<tbody>")[1].split("</tbody>")[0]

    rows = tbody.split("</tr>")[1:]


    for row in rows:
        tds = row.split("<td>")[1:]

        values = list()
        for td in tds:
            value = td.split("</td>")[0]
            values.append(value)


        if len(values) >= 8:
            row_data = {
                'code':code,
                '公布日期': values[0],
                '年度':     values[1],
                '派息事项': values[2],
                '派息内容': values[3],
                '方式':     values[4],
                '除净日':   values[5],
                '截止过户日期': values[6],
                '派息日期': values[7]
                       }

            print(row_data)

            k_table.insert_one(row_data)

    # rowTd = map(lambda row: row.split("</td>")[0], rows)









'''
从mongoDb查询股票数据
'''
def get_kline_by_code(code, start, autype='qfq'):

    client = MongoClient("mongodb://localhost:32017/")

    suffix = autype if autype is not None else 'none'
    k_table = client.kdatabase["ktable" + "_" + suffix]
    # k_table = client.kdatabase["ktable" + "_" + autype]
    result = k_table.find({"code": code, "date": {"$gt": datetime.strptime(start, '%Y-%m-%d')}})

    seq = []
    for d in result:
        seq.append(d)

    data = pd.DataFrame(seq, columns=['date', 'code', 'open', 'close', 'high', 'low', 'volume'])
    print (data)
    return data


def get_dividends_by_code(code):
    client = MongoClient("mongodb://localhost:32017/")
    k_table = client.kdatabase.ktable_dividends

    result = k_table.find({"code": code})
    seq = []
    for d in result:
        seq.append(d)

    data = pd.DataFrame(seq, columns=['code',
            '公布日期',
            '年度',
            '派息事项',
            '派息内容',
            '方式',
            '除净日',
            '截止过户日期',
            '派息日期'])
    print(data)
    return data


# test code
if __name__ == "__main__":

    pull_all_stock_kline('2017-02-08')

    get_kline_by_code('399808', '2017-02-15')


    pull_dividends('00585')
    get_dividends_by_code('00585')



