import numpy
import datetime
import pprint
import operator

from influxdb import InfluxDBClient, DataFrameClient


def get_db_list(client):
    print(client.get_list_database())

    return client.get_list_database()


def delete_dbs(client):
    # get list of current databases
    db_list = client.get_list_database()

    for d in db_list:
        if d["name"] != "_internal":
            client.drop_database(d["name"])
    print(client.get_list_database())


def create_db(client, db_name_list):
    for name in db_name_list:
        client.create_database(name)
        client.create_retention_policy('{}_policy'.format(name), 'INF', '3', name, default=True)
    print(client.get_list_database())


def get_time(client, msr_name, db_name):
    result = client.query('select * from "{}";'.format(msr_name), database=db_name)
    records_list = list(result.get_points())
    # print(len(records_list))

    for d in records_list:
        # print(datetime.datetime.utcfromtimestamp(d["tm"]))
        print(d)


def time_measurement(client, msr_name, db_name):
    result = client.query('select * from {};'.format(msr_name), database=db_name)
    records_list = list(result.get_points())

    # print(len(records_list))
    pprint.pprint(result)
    pprint.pprint(records_list)

    # temp = []
    # for d in records_list:
    #     temp.append(d["tm"] * 1000)
    #
    # # avg = numpy.diff(temp)
    #
    # return temp


def new_test():
    # clear databases
    delete_dbs(influx_client)

    # create new empty databases
    create_db(influx_client, dbs)


# create influxdb client
influx_client = InfluxDBClient(host='cldmaster.local', port=9998, username='root',
                               password='toor', database="details")

dbs = ["details"]
measurements = ["ccsds", "spacewire"]

# get_time(influx_client, measurements[0], dbs[0])

# ccsds = time_measurement(influx_client, measurements[2], dbs[0])
# spw = time_measurement(influx_client, measurements[1], dbs[0])

# time_measurement(influx_client, "AT1030Z", dbs[0])

# all_rec = ccsds + spw
# all_rec.sort()
# all_avg = numpy.diff(all_rec)

# pprint.pprint(list(all_avg), compact=True)
# print(max(list(all_avg)), min(list(all_avg)))

# print("InfluxDB AvgTime(ms):", sum(list(all_avg)) / len(list(all_avg)))
mes = influx_client.get_list_measurements()
mes_val = list(map(operator.itemgetter('name'), mes))
print(mes_val)
# q1 = influx_client.query('select * from "{}"'.format(mes_val[0]))
# q2 = influx_client.query('select * from "{}"'.format(mes_val[1]))

# # pprint.pprint([q1, q2])
# lou = q1.items()
# print(type(lou))
#
# ed = q1.raw
# print(type(ed))
# # pprint.pprint(ed)

import json
# pprint.pprint(json.dumps(ed))

# print databases list
get_db_list(influx_client)

get_time(influx_client, db_name="details", msr_name="duration")

# clean database
new_test()
