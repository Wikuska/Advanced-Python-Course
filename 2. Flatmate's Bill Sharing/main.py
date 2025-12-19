from bill import Bill
from flatmete import Flatmate
from pdf_report import PdfReport

bill_amount = int(input("Hello user, enter the bill amount: "))
bill_period = input("Now please enter bill period: ")
fm1_name = input("What is first flatmate name?: ")
fm1_days = int(input("And how many days did they stay in flat?: "))
fm2_name = input("What is second flatmate name?: ")
fm2_days = int(input("And how many days did they stay in flat?: "))
report_name = input("How should i name generated report?: ")

bill = Bill(bill_amount, bill_period)
flatmate1 = Flatmate(fm1_name, fm1_days)
flatmate2 = Flatmate(fm2_name, fm2_days)
pdf_report = PdfReport(report_name)
pdf_report.generate(flatmate1, flatmate2, bill)
print("Your report was successfully generated!")
