from PyPDF2 import PdfReader
import re
from write_csv_file import write_csv

reader = PdfReader("./pdfs/nippon energy sidian statements3.pdf")
pages = reader.pages

date = []
value_date = []
description = []
narrative = []
debit_credit = []
balance = []

for page in pages:
    page_text = page.extract_text((0, 90, 180)).split("\n")
    for x in range(len(page_text)):
        line = page_text[x]
        if re.search("NO CHEQUE", page_text[x]):
            line = line.replace("NO CHEQUE", "")

        if re.search(r'^\d{2}-\d{2}-\d{4}', line):
            split_line = line.split()
            date.append(split_line[0])
            value_date.append(split_line[1])
            desc = ""
            if re.search(r'\d*[.]\d{2}$', line):
                balance.append(split_line[-1])
                debit_credit.append(split_line[-2])
                narrative.append(split_line[-3])
                desc += ' '.join(split_line[2: -3])
                desc += " "
            else:
                desc += ' '.join(split_line[2:])
                desc += " "
                y = 1
                while not re.search(r'\d*[.]\d{2}$', page_text[x+y]):
                    current_line = page_text[x + y]
                    if re.search("NO CHEQUE", current_line):
                        current_line = current_line.replace("NO CHEQUE", "")
                    current_line = current_line.split()
                    desc += ' '.join(current_line[0:])
                    desc += " "
                    y += 1
                current_line = page_text[x+y]
                if re.search("NO CHEQUE", current_line):
                    current_line = current_line.replace("NO CHEQUE", "")
                current_line = current_line.split()
                balance.append(current_line[-1])
                debit_credit.append(current_line[-2])
                if len(current_line) == 3:
                    narrative.append(current_line[-3])
                else:
                    narrative.append("")
                desc += ' '.join(current_line[0: -3])
                balance.append(current_line[-1])
            description.append(desc)

print(date)
print(value_date)
print(description)
print(narrative)
print(debit_credit)
print(balance)

write_csv(['Date', 'Value Date', 'Description', 'Narrative', 'Debit/Credit', 'Balance'], [date, value_date, description, narrative, debit_credit, balance], "nippon")

