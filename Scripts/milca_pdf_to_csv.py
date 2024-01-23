import re
import pdfplumber
from Scripts.write_csv_file import write_csv

tran_date = []
value_date = []
tran_particulars = []
debit_credit = []
balance = []
tran_type = []

with pdfplumber.open("./pdfs/MILCA WAITHERA WACHIRA.pdf") as pdf:
    for page in pdf.pages:
        page_text = page.extract_text().split("\n")
        for x in range(len(page_text)):
            line = page_text[x]
            if re.search(r'^\d{2}-\d{2}-\d{4}', line):
                split_line = line.split()
                tran_date.append(split_line[0])
                value_date.append(split_line[1])
                debit_credit.append(split_line[-2])
                if not balance:
                    tran_type.append("unknown")
                elif balance[-1] < split_line[-1]:
                    tran_type.append("credit")
                else:
                    tran_type.append("debit")
                balance.append(split_line[-1])
                particulars = ' '.join(split_line[2: -2])

                y = 1
                while not re.search(r'^\d{2}-\d{2}-\d{4}', page_text[x+y]) and (x+y in range(len(page_text)-2)):
                    particulars += " "
                    particulars += ' '.join(page_text[x+y].split()[0:])
                    y += 1
                x = re.search(r'\s[0]\d{9}', particulars)
                y = re.search(r'\s[254]\d{9}', particulars)

                if x:
                    tran_particulars.append(particulars[x.span()[0]: x.span()[1]])
                elif y:
                    tran_particulars.append(particulars[y.span()[0]: y.span()[1]])
                else:
                    tran_particulars.append(particulars)

write_csv(header_row=["Transaction Date", "Value Date", "Transaction Particulars", "Credit/Debit", "Balance", "Transaction Type"], data=[tran_date, value_date, tran_particulars, debit_credit, balance, tran_type], output_file="new_milca_csv")