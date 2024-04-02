import csv

def convert_trivy_to_csv(input_file, output_file):
    # Read Trivy output from the input file
    with open(input_file, 'r') as file:
        trivy_output = file.readlines()

    # Remove | and - characters and split the lines into CSV rows
    csv_rows = []
    for line in trivy_output:
        if '|' not in line:
            continue
        csv_row = line.replace('|', '').strip().split()
        csv_rows.append(csv_row)

    # Write CSV rows to the output file
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(csv_rows)

# Example usage:
input_file = 'trivy_output.txt'
output_file = 'trivy_output.csv'
convert_trivy_to_csv(input_file, output_file)
