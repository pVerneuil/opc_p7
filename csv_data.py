import csv
from decimal import Decimal


def import_data_from_csv(filename):
    """import and clen data from a cvs file

    Args:
        filename (str): filename.csv file

    Returns:
        list: [['share',price,profit%],...]
    """
    data = []
    with open(f"csv_data/{filename}", newline="") as dataset:
        action_reader = csv.reader(dataset, delimiter=",")
        next(action_reader)
        for row in action_reader:
            if row[0] and float(row[1]) > 0 and float(row[2]) > 0:
                row[0] = row[0][6:]
                row[1] = float(row[1])
                row[2] = float(row[2])
                data.append(row)
    return data


data_raw = import_data_from_csv("dataset1.csv")
