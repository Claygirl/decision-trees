# -*- coding: utf-8 -*-

import csv

def read_data(filename):

    with open(filename, 'r') as csvfile:
        datareader = csv.reader(csvfile, delimiter=',')
        headers = next(datareader)
        metadata = []
        traindata = []
        for name in headers:
            metadata.append(name)
            
        for row in datareader:
            traindata.append(row)

    return (metadata, traindata)