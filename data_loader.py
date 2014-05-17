import csv

def read_data(filename):

    with open(filename, 'rb') as csvfile:
        datareader = csv.reader(csvfile, delimiter=',', quotechar='|')
        headers = next(datareader)
        metadata = {}
        traindata = []
        for name in headers:
            metadata[name] = []
            
        for row in datareader:
            traindata.append(row)
            for pos in range(len(row)):
                bucket = metadata[headers[pos]]
                val = row[pos]
                if val not in bucket:
                    bucket.append(val)

    return (metadata, traindata)