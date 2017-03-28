# stock-data-analytics
1、拉取A股行情数据存储到MongoDB

2、从MongoDB取行情数据

3、为以后模型回测用，还没开始:)


MongoDb 存储如下：

 db.ktable_afq.find()
{ "_id" : ObjectId("58da7af688163c7e1451dc89"), "high" : 14.02, "open" : 13.98, "low" : 13.85, "volume" : 8687, "code" : "000856", "date" : ISODate("2017-02-08T00:00:00Z"), "close" : 14.01 }
{ "_id" : ObjectId("58da7af688163c7e1451dc8a"), "high" : 14.22, "open" : 14, "low" : 13.95, "volume" : 13262, "code" : "000856", "date" : ISODate("2017-02-09T00:00:00Z"), "close" : 14.19 }
{ "_id" : ObjectId("58da7af688163c7e1451dc8b"), "high" : 14.9, "open" : 14.2, "low" : 14.15, "volume" : 22810, "code" : "000856", "date" : ISODate("2017-02-10T00:00:00Z"), "close" : 14.45 }
{ "_id" : ObjectId("58da7af688163c7e1451dc8c"), "high" : 14.45, "open" : 14.4, "low" : 14.22, "volume" : 10926, "code" : "000856", "date" : ISODate("2017-02-13T00:00:00Z"), "close" : 14.32 }
{ "_id" : ObjectId("58da7af688163c7e1451dc8d"), "high" : 14.36, "open" : 14.24, "low" : 14.1, "volume" : 13062, "code" : "000856", "date" : ISODate("2017-02-14T00:00:00Z"), "close" : 14.1 }
{ "_id" : ObjectId("58da7af688163c7e1451dc8e"), "high" : 14.14, "open" : 14.14, "low" : 13.8, "volume" : 23900, "code" : "000856", "date" : ISODate("2017-02-15T00:00:00Z"), "close" : 13.84 }
{ "_id" : ObjectId("58da7af688163c7e1451dc8f"), "high" : 13.99, "open" : 13.81, "low" : 13.77, "volume" : 13735, "code" : "000856", "date" : ISODate("2017-02-16T00:00:00Z"), "close" : 13.94 }
{ "_id" : ObjectId("58da7af688163c7e1451dc90"), "high" : 14.08, "open" : 13.98, "low" : 13.82, "volume" : 11936, "code" : "000856", "date" : ISODate("2017-02-17T00:00:00Z"), "close" : 13.95 }
{ "_id" : ObjectId("58da7af688163c7e1451dc91"), "high" : 13.97, "open" : 13.88, "low" : 13.7, "volume" : 11880, "code" : "000856", "date" : ISODate("2017-02-20T00:00:00Z"), "close" : 13.93 }
{ "_id" : ObjectId("58da7af688163c7e1451dc92"), "high" : 14, "open" : 13.95, "low" : 13.82, "volume" : 16561, "code" : "000856", "date" : ISODate("2017-02-21T00:00:00Z"), "close" : 13.95 }
{ "_id" : ObjectId("58da7af688163c7e1451dc93"), "high" : 14.39, "open" : 13.94, "low" : 13.89, "volume" : 24666, "code" : "000856", "date" : ISODate("2017-02-22T00:00:00Z"), "close" : 14.26 }
{ "_id" : ObjectId("58da7af688163c7e1451dc94"), "high" : 14.36, "open" : 14.28, "low" : 13.99, "volume" : 21545, "code" : "000856", "date" : ISODate("2017-02-23T00:00:00Z"), "close" : 14.18 }
{ "_id" : ObjectId("58da7af688163c7e1451dc95"), "high" : 14.21, "open" : 14.15, "low" : 14.08, "volume" : 17405, "code" : "000856", "date" : ISODate("2017-02-24T00:00:00Z"), "close" : 14.21 }
{ "_id" : ObjectId("58da7af688163c7e1451dc96"), "high" : 14.48, "open" : 14.19, "low" : 14.17, "volume" : 28365, "code" : "000856", "date" : ISODate("2017-02-27T00:00:00Z"), "close" : 14.34 }
{ "_id" : ObjectId("58da7af688163c7e1451dc97"), "high" : 14.66, "open" : 14.3, "low" : 14.3, "volume" : 21303, "code" : "000856", "date" : ISODate("2017-02-28T00:00:00Z"), "close" : 14.5 }
{ "_id" : ObjectId("58da7af688163c7e1451dc98"), "high" : 15.03, "open" : 14.52, "low" : 14.45, "volume" : 40502, "code" : "000856", "date" : ISODate("2017-03-01T00:00:00Z"), "close" : 14.8 }
{ "_id" : ObjectId("58da7af688163c7e1451dc99"), "high" : 15.07, "open" : 14.87, "low" : 14.74, "volume" : 34996, "code" : "000856", "date" : ISODate("2017-03-02T00:00:00Z"), "close" : 14.81 }
{ "_id" : ObjectId("58da7af688163c7e1451dc9a"), "high" : 15.06, "open" : 14.86, "low" : 14.72, "volume" : 23289, "code" : "000856", "date" : ISODate("2017-03-03T00:00:00Z"), "close" : 15.02 }
{ "_id" : ObjectId("58da7af688163c7e1451dc9b"), "high" : 15.32, "open" : 15.05, "low" : 14.99, "volume" : 29021, "code" : "000856", "date" : ISODate("2017-03-06T00:00:00Z"), "close" : 15.31 }
{ "_id" : ObjectId("58da7af688163c7e1451dc9c"), "high" : 15.29, "open" : 15.29, "low" : 15.04, "volume" : 31320, "code" : "000856", "date" : ISODate("2017-03-07T00:00:00Z"), "close" : 15.09 }
Type "it" for more

