__author__ = 'fbueti'
import csv
from collections import Counter

def topComp(candidate):
        categories = []
        path =  candidate + '.csv'
        with open(path) as csvfile:
            all_expenses = csv.DictReader(csvfile)
            for expense in all_expenses:
                    categories.append(expense['recipient_nm'])
            top5 = Counter(categories).most_common(5)

            for company in top5:
                company = company[0]
            print (top5)

topComp('trump')
topComp('bernie')
topComp('hillary')