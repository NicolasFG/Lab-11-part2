import csv
import pandas as pd
from collections import Counter
from joblib import Parallel, delayed

def count(array):
    counts = {}
    for value in array:
        if value in counts:
            counts[value] += 1
        else:
            counts[value] = 1
    return counts

def process_batch(data_list):
    batch_names = []
    for item in data_list:
        if (item[0] == "CA"):
            batch_names.append(item[3])
    name_counts = count(batch_names)
    return name_counts



fileName = 'baby-names-state.csv'
batchSize = 1000
array=[]
for df in pd.read_csv(fileName, chunksize=batchSize):
    data_list = df.values.tolist()
    array.append(data_list)

batch_names = Parallel(n_jobs=3)(delayed(process_batch)(i) for i in array)

combined_counts = Counter()
for counts in batch_names:
    combined_counts.update(counts)
most_common_name, count = combined_counts.most_common(1)[0]
print("Nombre", most_common_name)
print("Count:", count)