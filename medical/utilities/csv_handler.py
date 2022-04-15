import csv

def load_column_from_dataset(column_name):
    filename = open('dataset.csv', 'r')
    file = csv.DictReader(filename)
    values = []
    for row in file:
        value = row[column_name]
        if value:
            values.append(value)
    return values