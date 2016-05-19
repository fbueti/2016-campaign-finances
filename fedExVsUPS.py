__author__ = 'fbueti'
import csv

fedex = 0.0
usps = 0.0
i = 0;
with open('hillary.csv') as csvfile:
    all_expenses = csv.DictReader(csvfile)
    for expense in all_expenses:
        i += 1
    print (i)
