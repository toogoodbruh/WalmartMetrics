import glob
import re
import csv
import pandas as pd

input_file = "Data/TestTextInput/ByAssociateView.txt"
output_file = "Data/TestTextInput/ByAssociateView_FromTextFile.csv"
#header = "Store #,Associate,Day of Pick Date,FTPR,FTP Expected,FTP Actual,Pick Rate,Pick Hours,Picked As Req Qty,Substitution Qty,Ovrd Qty,Nil Pick Qty,Exception Qty Req to Pick,Exception Picked As Req Qty,Exception Substitution Qty,Exception Nil Pick Qty,SFS Pack Hours,    SFS Packed Qty,    SFS Pack Rate,    SFS Pack Expected,    SFS Pack Actual,    SFS Pack Exception Qty\n"


def text_to_csv(text_file_path, csv_file_path, delimiter=','):
    """
    Reads data from a text file and writes it to a CSV file.

    Args:
        text_file_path (str): The path to the input text file.
        csv_file_path (str): The path to the output CSV file.
        delimiter (str, optional): The delimiter used in the text file. Defaults to ','.
    """
    try:
        with open(text_file_path, 'r') as infile, open(csv_file_path, 'w', newline='') as outfile:
            reader = csv.reader(infile, delimiter=delimiter)
            writer = csv.writer(outfile)
            for row in reader:
                writer.writerow(row)
        print(f"Successfully converted '{text_file_path}' to '{csv_file_path}'")
    except Exception as e:
         print(f"An error occurred: {e}")

#text_to_csv(input_file, output_file, delimiter='\t')

#df = pd.read_csv(input_file, sep="\t", engine='python')
#df.to_csv(output_file, index=False)


# Open and process the file

with open(input_file, 'r', encoding='utf-8') as infile, \
     open(output_file, 'w', newline='', encoding='utf-8') as outfile:
    
    writer = csv.writer(outfile)

    # Read header and determine column count
    header_line = next(infile)
    header = re.split(r'\s{2,}', header_line.strip())  # Split by 2 or more spaces
    expected_len = len(header)
    
    writer.writerow(header)  # write header to CSV

    for line in infile:
        # Clean line: remove trailing spaces and split on 2+ spaces
        line = line.rstrip()  # Remove trailing whitespace
        row = re.split(r'\s{2,}', line.strip())

        # Skip rows with too few or too many columns than expected
        if len(row) >= expected_len:
            print(f"Skipping malformed row: {row}")  # Optional: Log malformed rows
            continue

        # Write the row only if it's correctly formatted
        writer.writerow(row)
print(f"Conversion complete. File saved as {output_file}")