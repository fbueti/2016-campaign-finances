__author__ = 'fbueti'
import csv

def grandTotal(candidate):
        total = 0.0
        path =  candidate + '.csv'
        with open(path) as csvfile:
            all_expenses = csv.DictReader(csvfile)
            for expense in all_expenses:
                total += float(expense['disb_amt'])
        return round(total,2)

bernie = grandTotal('bernie')
trump = grandTotal('trump')
hillary = grandTotal('hillary')
grandTotal = bernie + trump + hillary

totals = [hillary, trump, bernie]
candidates = ['Clinton', 'Trump', 'Sanders']
print(bernie, trump, hillary, grandTotal)

csv_format = [candidates, totals]

zipped = zip(*csv_format)
with open('amountPer.csv', 'w') as f:
     writer = csv.writer(f)
     writer.writerows(zipped)
