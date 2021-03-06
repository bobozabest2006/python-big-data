import pandas as pd
import numpy as np
import pprint
import datetime
import json
from influxdb import InfluxDBClient, DataFrameClient
import time
import timeit
import os

#
# df = pd.DataFrame(data=list(range(30)),
#                   index=pd.date_range(start='2014-11-16',
#                                       periods=30, freq='H'))
#
# influx_client = InfluxDBClient(host='cldmaster.local', port=9998, username='root',
#                                password='toor')
#
influx_client_df = DataFrameClient(host='cldmaster.local', port=9998, username='root',
                                   password='toor')
#
# pprint.pprint(df)
# print(type(df))
#
# data = pd.DataFrame(
#     {'Timestamp': [1313331280.654563843684, 1313334917.654563843684,
#                    1313334917.654563843684, 1313340309.654563843684, 1313340309.654563843684],
#      'Price': [10.4]*3 + [10.5]*2, 'Volume': [0.779, 0.101, 0.316, 0.150, 1.8]})
# data = data.set_index(['Timestamp'])
# #             Price  Volume
# # Timestamp
# # 1313331280   10.4   0.779
# # 1313334917   10.4   0.101
# # 1313334917   10.4   0.316
# # 1313340309   10.5   0.150
# # 1313340309   10.5   1.800
#
# data.index = pd.to_datetime(data.index, unit='us')
#
# print(data)
#
# fields = ["groupdate",
#           "simulationdate",
#           "Localdate",
#           "eng",
#           "dec",
#           "raw",
#           "timestamp"]
#
# tags = {
#     "confid": None, #str(2),
#     "appid": None, #int(32),
#     "vcid": int(2),
#     "subsystem": str(2),
#     "puss": int(2),
#     "pusss": int(3),
#     "status_processed": bool(1),
#     "status_invalid": bool(1),
#     "status_obsolete": bool(1),
#     "status_caution": bool(1),
#     "status_action": bool(1),
#     "status_alarm": bool(1),
#     "source": str(9),
#     "sbd": str(9),
#     "unit": str(9),
#     "type": str(9)
# }
#
# df2 = pd.DataFrame(data=[[1, 2, 3, 4, 5, 6, 1522920989746], [1, 2, 3, 4, 5, 6, 1522920989747],
#                          [1, 2, 3, 4, 5, 6, 1522920989748], [1, 2, 3, 4, 5, 6, 1522920989749]],
#                    index=[i for i in range(4)],
#                    columns=fields)
#
# df2_new_index = df2.set_index(['timestamp'])
#
# df2_new_index.index = pd.to_datetime(df2_new_index.index, unit='us', utc=True)
#
# print(df2_new_index.index)
# print(df2)
# print(df2_new_index)
# pprint.pprint(df2_new_index.to_json(orient='split'))
#
# influx_client_df.write_points(df2_new_index, measurement='AT1030Z',
#                               tags=tags,
#                               database='details',
#                               time_precision='u',
#                               numeric_precision='full')
#
#
# def influxdb_write(client, dataframe, m_name, db_name, optional=False):
#
#     if optional is True:
#         fields = {"groupdate": int(),
#                   "simulationdate": int(),
#                   "Localdate": int(),
#                   "eng": None,
#                   "dec": float(),
#                   "raw": str(),
#                   "timestamp": datetime.datetime()}
#
#         tags = {
#             "confid": str(),
#             "appid": int(),
#             "vcid": int(),
#             "subsystem": str(),
#             "puss": int(),
#             "pusss": int(),
#             "status_processed": bool(),
#             "status_invalid": bool(),
#             "status_obsolete": bool(),
#             "status_caution": bool(),
#             "status_action": bool(),
#             "status_alarm": bool(),
#             "source": str(),
#             "sbd": str(),
#             "unit": str(),
#             "type": str()
#         }
#
#     else:
#         fields = {"eng": None,
#                   "dec": float(),
#                   "timestamp": datetime.datetime()}
#
#         tags = {
#             "confid": str(),
#         }
#
#     client.write_points(df2_new_index, measurement=m_name,
#                         tags=tags,
#                         database=db_name,
#                         time_precision='u',
#                         numeric_precision='full')
#     pass

# a = [np.zeros((224,224,3)), np.zeros((224,224,3)), np.zeros((10,224,3))]
# print(np.array(a))

# data = np.array([['','Col1','Col2'],['Row1',1,2],['Row2',3,4]])
# df = pd.DataFrame(data=data[1:, 1:],    # values
#                   index=data[1:, 0],    # 1st column as index
#                   columns=data[0, 1:])
# print(df)

# headers = ["Date", "Ticker", "Close", "Volume"]
# data = [["2018-04-05 09:36:29.746678", "MSFT", 1.3, 2.5],
#         ["2018-04-06 09:36:29.746678", "MSFT", 3.5, 4.24],
#         ["2018-04-05 09:37:29.746678", "AAPL", 7, 11],
#         ["2018-04-06 09:37:29.746678", "AAPL", 6, 1]]

# data = {"eng": [int(i + 50) for i in range(5)],
#         "dec": [float(i + 30.5) for i in range(5)],
#         "Date": ["2018-04-05 09:36:2{}.746678".format(i) for i in range(5)],
#         # tags
#         "confid": [str(hex(i + 100)) for i in range(5)]
#         }
# headers = list(data.keys())
#
# df = pd.DataFrame.from_dict(data)
# df.Date = pd.to_datetime(df["Date"])
# df = df.set_index("Date")
# print(df)
# influx_client_df.write_points(df, 'AT1030Z', tag_columns=['confid'], database='details')

import pprint
import time
import subprocess

import happybase
import pdhbase as pdh
from influxdb import DataFrameClient

from pyspark import SparkContext
from pyspark.sql import SQLContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
from hdfs3 import HDFileSystem
from hdfs import InsecureClient
import itertools


# Bytes format decoder
def iso_8859_1(s):
    if s is None:
        return None
    return s.decode('ISO-8859-1')


def hdfs_remove_file(path):
    if hdfs.exists(path):
        hdfs.rm(path)
        print("Removed {}".format(path))
    else:
        print("{} file does not exist.".format(path))


def hdfs_write_file(path, rdd):
    if hdfs.exists(path):
        path = hdfs.glob(os.path.join(path, "part*"))[0]
        # print(path)
        # print(hdfs.glob(os.path.join(path, "part*")))
        file = hdfs.open(path=path, mode="ab")
        for key, value in rdd.toLocalIterator():
            file.write(data=value)

        if not file.closed:
            file.close()

    else:
        # hdfs.touch(path)
        # file = hdfs.open(path=path, mode="wb")
        # for k, v in rdd.toLocalIterator():
        #     file.write(data=v)

        # rdd.saveAsTextFile(path)
        rdd.saveAsNewAPIHadoopFile(path,
                                   outputFormatClass="org.apache.hadoop.mapreduce.lib.output.SequenceFileOutputFormat")


def ceva_misto(rdd):

    if rdd.isEmpty():
        print("[NO DATA RECEIVED]")

        if hdfs.exists(hdfs.glob(os.path.join("/user/cloudera/*", "part*"))[0] if len(
                hdfs.glob("/user/cloudera/*")) > 0 else None):

            hdfs_file = hdfs.open(hdfs.glob(os.path.join("/user/cloudera/*", "part*"))[0])
            print(hdfs_file.readlines())

    else:
        hdfs_write_file("/user/cloudera/test_1/part-{}".format(next(counter)), rdd)

        # rdd.saveAsTextFile("/user/cloudera/new_haddop_api_file/part-00001")


if __name__ == "__main__":

    topic1 = "CCSDS"
    counter = itertools.count(start=0, step=1)

    # spark object
    sc = SparkContext("local[2]", "SparkKafkaStreaming", batchSize=5000)

    # streaming object
    ssc = StreamingContext(sc, 10)

    # dataframe object
    sqlContext = SQLContext(sc)

    hdfs = HDFileSystem()

    print(hdfs.glob(os.path.join("/user/cloudera/*", "part*")))
    print("Is Dir:", hdfs.isdir(hdfs.glob(os.path.join("/user/cloudera/*", "part*"))[0]
                                if len(hdfs.glob("/user/cloudera/*")) > 0 else None))
    print("Is File:", hdfs.isfile(hdfs.glob(os.path.join("/user/cloudera/*", "part*"))[0]
                                  if len(hdfs.glob("/user/cloudera/*")) > 0 else None))

    # if hdfs.exists(hdfs.glob(os.path.join("/user/cloudera/*", "part*"))[0] if len(hdfs.glob("/user/cloudera/*")) > 0 else None):
    #     hdfs_file = hdfs.open(hdfs.glob(os.path.join("/user/cloudera/*", "part*"))[0])
    #     print(hdfs_file.readlines())

    print(hdfs.glob(os.path.join("/user/cloudera/*", "part*"))[0] if len(hdfs.glob("/user/cloudera/*")) > 0 else None)

    hdfs_remove_file(hdfs.glob("/user/cloudera/*")[0] if len(hdfs.glob("/user/cloudera/*")) > 0 else None)

    # Kafka Consumer client, connect to Kafka producer server
    kvs = KafkaUtils.createDirectStream(ssc, topics=[topic1],
                                        valueDecoder=iso_8859_1,
                                        keyDecoder=iso_8859_1,
                                        kafkaParams={'metadata.broker.list': 'cldmaster.local:9092'})

    # test = kvs.filter(lambda y: len(y) > 0).map(lambda x: x[1])  # .repartition(2)
    test = kvs.filter(lambda y: len(y) > 0).map(lambda x: x)  # .repartition(2)

    test.foreachRDD(ceva_misto)

    test.count().pprint()

    # Print to console
    ssc.start()
    ssc.awaitTermination()

spw_ts_sec = 1522920989
spw_ts_usec = 746678112

(spw_ts_sec + (float("{0:.4f}".format(spw_ts_usec / 10**9)))) * 10**3
