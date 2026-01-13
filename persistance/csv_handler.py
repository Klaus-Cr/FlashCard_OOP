from csv import reader, writer
from config import PREFIX, CSV_ENCODING, DATA_DIR

class CsvHandler():
    def __init__(self, filename):
        self.words = []
        #* read the csv file
        with open(file=DATA_DIR / filename, mode="r", encoding=CSV_ENCODING) as fp:
             self.words = list(reader(fp))


    def write_csv(self, filename, languages):
        if PREFIX not in filename:
            filename = PREFIX + filename
        #* write csv file
        with open(file=DATA_DIR / filename, mode="w", encoding=CSV_ENCODING, newline="") as fp:
            write_csv = writer(fp)
#            write_csv.writerow(languages)
            write_csv.writerows(self.words)

