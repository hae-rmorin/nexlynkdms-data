# artifact:  generateCSV.py
# author:    robyn.morin@haemonetics.com

import csv

def export(csv_header, rows, output_file_path):
    file = open(output_file_path, 'w', newline = '')
    with file:
        header = csv_header
        writer = csv.DictWriter(file, fieldnames = header)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)
