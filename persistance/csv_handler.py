from csv import reader, writer
from config import PREFIX, CSV_ENCODING, DATA_DIR

class CsvHandler():
    """
    Persistence component for reading and writing vocabulary data in CSV format.

    CsvHandler is responsible for loading vocabulary word pairs from a CSV file
    and writing updated training data back to disk. It does not contain any
    domain logic and does not interact with the user interface directly.

    Responsibilities:
    - Read vocabulary data from a CSV file
    - Write updated vocabulary data back to a CSV file with prefix "training_"
    - Ensure consistent file encoding and output format

    The class acts as a thin abstraction over CSV I/O and is designed to be
    stateless with respect to application logic.
    """

    def __init__(self, filename: str):
        self.words = []
        #* read the csv file
        with open(file=DATA_DIR / filename, mode="r", encoding=CSV_ENCODING) as fp:
             self.words = list(reader(fp))


    def write_csv(self, filename: str) -> None:
        if PREFIX not in filename:
            filename = PREFIX + filename
        #* write csv file
        with open(file=DATA_DIR / filename, mode="w", encoding=CSV_ENCODING, newline="") as fp:
            write_csv = writer(fp)
            write_csv.writerows(self.words)
