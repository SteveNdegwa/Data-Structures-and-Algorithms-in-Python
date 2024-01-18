import csv


def write_csv(header_row, data, output_file):
    with open(f'./csvs/{output_file}.csv', mode='w') as statement_data:
        statement_writer = csv.writer(statement_data, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        statement_writer.writerow(header_row)
        for x in range(len(data[0])):
            statement_writer.writerow([data[i][x] for i in range(len(data))])
