from functools import reduce
from multiprocessing import Pool

test_file = 'baby-names-state.csv'
list_of_names = [["Maria", "Pedro", "Juan"], ["Pedro"], ["Maria"]]

def chunks(file_name, size=10000):
    with open(file_name) as f:
        while content := f.readline():
            for _ in range(size - 1):
                content += f.readline()

            yield content.splitlines()


def process_batch(batch):
    result = []
    count_names = {}
    for item in batch:
        elements = item.split(',')
        if elements[0] == '"CA"':
            if not elements[3] in count_names:
                count_names[elements[3]] = 0
            count_names[elements[3]] += 1

    return count_names



# reduce function
# dict1: es el resultado previo que se va acumulando
# dict2: es el nuevo diccionario
def calculate(dict1, dict2):
    combined = {}

    #print(dict1, dict2)

    for key in dict1:
        combined[key] = dict1[key]

    for key in dict2:
        if key in combined:
            combined[key] += dict2[key]
        else:
            combined[key] = dict2[key]

    return combined


if __name__ == "__main__":
    split_files = chunks(test_file)
    
    with Pool() as pool:
        results = pool.map(process_batch, split_files)
        #results = pool.map(count_words, list_of_names) # MAP

    #print(results[5])
    words = reduce(calculate, results)
    #print(words)
    max_score = max(words, key=words.get)
    print("El máximo puntaje es:", max_score, "con", words[max_score])
    #for key, val in words.items():
       #print("El total para {} es {}".format(key, val))