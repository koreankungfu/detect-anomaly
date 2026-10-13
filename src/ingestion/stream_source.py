"Read a time-series CSV as a simulated stream of readings."

import csv
from datetime import datetime
from pathlib import Path


class CSVStreamSource:
    "Yields (timestamp, value) one row at a time from a CSV."
    
    def __init__(self, path):
        self.path = Path(path)
        if not self.path.exists():
            raise FileNotFoundError(f"no such file: {self.path}")

    def __iter__(self):
        with self.path.open(newline="") as f:
            reader = csv.reader(f)
            header = next(reader)
            for row in reader:
                if not row:
                    continue
                timestamp = datetime.fromisoformat(row[0])
                value = float(row[1])
                yield timestamp, value
