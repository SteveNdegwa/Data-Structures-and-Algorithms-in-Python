import pdfplumber
import re
import csv

transaction_date = []
value_date = []
description = []
credits = []
debits = []
balance = []

line_re = re.compile(r'^\d{2}-\d{2}-\d{4}')
with pdfplumber.open("MILCA WAITHERA WACHIRA.pdf") as pdf:
    for page in pdf.pages:
        text_list = page.extract_text().split("\n")
        for x in range(len(text_list)):
            if line_re.search(text_list[x]):
                split_line = text_list[x].split()
                transaction_date.append(split_line[0])
                desc = ' '.join(split_line[2: -4])
                print(desc)
                if x+1 in range(len(text_list)) and (not line_re.search(text_list[x+1])):
                    desc += " "
                    desc += ' '.join(text_list[x+1].split()[0:])
                description.append(desc)
                value_date.append(split_line[1])
                balance.append(split_line[-2])
                credits.append(split_line[-3])
                debits.append(split_line[-4])

print(transaction_date)
print(value_date)
print(debits)
print(credits)
print(balance)
print(description)

with open('employee_file.csv', mode='w') as statement_data:
    statement_writer = csv.writer(statement_data, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    statement_writer.writerow(['Transaction Date', 'Value Date', 'Description', 'Debits', 'Credits', 'Balance'])
    for x in range(len(transaction_date)):
        statement_writer.writerow([transaction_date[x], value_date[x], description[x], debits[x], credits[x], balance[x]])








