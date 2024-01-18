import pdfplumber
import re
from write_csv_file import write_csv

line_re = re.compile(r'\d*[.]\d{2}$')

transaction_details = []
payment_reference = []
value_date = []
credit_debit = []
balance = []
transaction_type = []

with pdfplumber.open("pdfs/EQUITY TILL STMT-KIMBERLY TERRIFFER WANJIRU-1.pdf") as pdf:
    for page in pdf.pages:
        page_text = page.extract_text().split("\n")
        for x in range(len(page_text)):
            if line_re.search(page_text[x]):
                line = page_text[x].split()
                if not balance:
                    transaction_type.append("unknown")
                elif line[-1] >= balance[-1]:
                    transaction_type.append("credit")
                else:
                    transaction_type.append("debit")
                balance.append(line[-1])
                credit_debit.append(line[-2])
                value_date.append(line[-3])
                payment_reference.append(line[-4])
                trans_details = ' '
                if len(line) > 4:
                    trans_details += ''.join(line[0])
                trans_details = ' '.join(page_text[x-1].split()[0:]) + trans_details
                trans_details += " "
                trans_details += ' '.join(page_text[x+1].split()[0:])
                transaction_details.append(trans_details)

write_csv(['Transaction Date', 'Payment Reference', 'Value Date', 'Credit/Debit', 'Balance', 'Transaction Type'], [transaction_details, payment_reference, value_date, credit_debit, balance, transaction_type], "equity4")